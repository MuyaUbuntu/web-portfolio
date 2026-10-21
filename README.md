# Web Portfolio · Rodrigo López

Portafolio de diseño y gestión de marca. Sitio estático: HTML, CSS y JavaScript, sin dependencias ni paso de compilación.

## Estructura

```
index.html                 Landing (hero, proyectos apilados, perfil, contacto)
proyectos/
  nomada-cafe.html         Caso de estudio (plantilla para los demás casos)
assets/
  css/styles.css           Estilos y tokens de diseño (colores, tipografía, espaciado)
  js/site.js               Interacciones: cursor, menú, efecto de peso, carruseles, contadores
  img/                     Imágenes optimizadas que usa el sitio (logo, portadas, galerías)
content/                   Material fuente: textos y archivos por proyecto (no se publica como página)
  perfil/perfil.md
  logos-clientes/
  proyectos/01-nombre-del-proyecto/
    caso.md
    exploracion/
    galeria/
```

## Flujo de trabajo

1. El material en bruto (fotos en alta, PSD, videos, borradores) vive en Google Drive, en la carpeta **Web Portfolio**.
2. Los textos finales de cada caso van en `content/`, con las plantillas `caso.md` y `perfil.md`.
3. Las imágenes que usa el sitio se optimizan (máx. ~2400 px, JPG/WebP) y van en `assets/img/<proyecto>/`.
4. Cada proyecto nuevo es una copia de `proyectos/nomada-cafe.html` con su contenido.

Archivos de diseño pesados (`.psd`, `.ai`, `.mov`) están excluidos en `.gitignore`. GitHub rechaza archivos de más de 100 MB.

## Ver el sitio en local

Abre `index.html` en el navegador, o sirve la carpeta:

```
python3 -m http.server 8000
```

## Publicar

Al ser un sitio estático, puede publicarse gratis en GitHub Pages, Netlify o Vercel apuntando a la raíz del repositorio, y conectarse a un dominio propio.

## Estado

Contenido de ejemplo: los proyectos y cifras son placeholders hasta reemplazarlos con material real. El texto final irá en inglés.
