# Colección de Vinilos · Café de Ley

Esta carpeta es la única fuente de trabajo para la landing. Mantén el `index.html` en la raíz: GitHub y Vercel pueden publicar la página directamente desde allí. No copies el proyecto a carpetas de Codex o ChatGPT.

## Cuando Miguel envíe la foto de un nuevo vinilo

1. Identifica artista, álbum y edición concreta. Compara visualmente la portada que envió con una imagen digital de buena calidad encontrada en una fuente pública. No recortes su foto ni sustituyas la portada por otra variante.
2. Verifica año, género y canciones de esa edición con fuentes confiables. Usa un género existente en `src/template.html` si corresponde; añade un filtro solo si hace falta.
3. Guarda la portada digital en `src/covers/`, agrega el registro a `src/records.json` sin duplicados y conserva el orden alfabético por artista. La portada y las canciones deben aparecer en la ficha. Mantén el diseño, las animaciones y la interacción existentes.
4. Ejecuta `python3 build.py`. El único archivo de publicación es `index.html` en la raíz. Comprueba que el número de discos, imágenes, filtros y JavaScript sean correctos.
5. Si esta carpeta tiene remoto GitHub y autenticación disponibles, crea un commit con el cambio y envíalo a la rama conectada a Vercel; verifica el despliegue. La solicitud de añadir un vinilo autoriza esta actualización ordinaria. Si falta conexión o autorización técnica, deja el archivo listo y explica qué falta.

## Archivos

- `index.html`: página completa, con imágenes y fuentes integradas. Es el archivo que publica Vercel.
- `src/records.json`: catálogo editable.
- `src/covers/`: portadas digitales de cada vinilo.
- `src/assets/`: fuentes, logo y recursos del diseño.
- `src/template.html`: diseño y lógica de la página.
- `build.py`: reconstruye el HTML final.

El archivo `index.html` debe seguir funcionando por sí solo. No cambies la protección o visibilidad del proyecto de Vercel sin instrucción expresa.
