#!/usr/bin/env python3
"""Regenera index.html con el catálogo, fuentes y portadas integradas."""

import base64
import json
import mimetypes
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'src'
OUTPUT = ROOT / 'index.html'


def uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode('ascii')


def main() -> None:
    records = json.loads((SOURCE / 'records.json').read_text(encoding='utf-8'))
    html = (SOURCE / 'template.html').read_text(encoding='utf-8')
    marker = '/*__RECORDS__*/[]'
    assert html.count(marker) == 1
    html = html.replace(marker, json.dumps(records, ensure_ascii=False, separators=(',', ':')))

    for path in (SOURCE / 'assets').rglob('*'):
        if path.is_file():
            relative = path.relative_to(SOURCE).as_posix()
            if relative in html:
                html = html.replace(relative, uri(path))

    covers = {}
    for name in sorted({r['cover'] for r in records if r.get('cover')}):
        path = SOURCE / 'covers' / name
        if not path.is_file():
            raise FileNotFoundError(path)
        covers[name] = uri(path)

    cover_expression = 'covers/${r.cover}'
    assert html.count(cover_expression) == 2
    html = html.replace(cover_expression, '${COVER_URIS[r.cover]}')
    script_marker = '<script>\n'
    assert html.count(script_marker) == 1
    html = html.replace(script_marker, script_marker + 'const COVER_URIS = ' + json.dumps(covers, separators=(',', ':')) + ';\n')
    assert 'assets/' not in html and cover_expression not in html
    OUTPUT.write_text(html, encoding='utf-8')
    print(f'{len(records)} vinilos · {OUTPUT} · {OUTPUT.stat().st_size:,} bytes')


if __name__ == '__main__':
    main()
