# Colección de vinilos de Café de Ley

Esta carpeta contiene el código, los datos y las portadas del catálogo. La versión actual tiene 95 discos.

## Publicar

`index.html` está en la raíz y contiene toda la landing. Si el repositorio de GitHub está conectado con Vercel, cada cambio enviado a la rama de producción actualizará la URL automáticamente. El proyecto de Vercel debe usar la raíz del repositorio como directorio de salida, sin comando de compilación.

## Agregar un disco

Actualizar `src/records.json` y guardar su portada exacta en `src/covers/`. Luego ejecutar:

```sh
python3 build.py
```

La foto que envíe Miguel sirve como referencia para buscar una portada digital coincidente. Verificar edición, año, género y canciones antes de publicar.

## GitHub y Vercel

Repositorio: https://github.com/cafedeleylab/Catalogo-vinilos, rama `main`. Esta carpeta se conecta directamente a ese repositorio. La landing publicada usa el `index.html` de la raíz. Cuando se agregue un disco, el flujo será: verificar datos e imagen, actualizar `src/`, ejecutar `python3 build.py`, comprobar la página y enviar el commit a `main`. Vercel debe seguir conectado a esa rama para publicar cada cambio automáticamente.
