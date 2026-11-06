# Script to Screen: pasar la maqueta al portafolio

Instrucciones para continuar en otro espacio de trabajo. Se pueden pegar tal cual como primer mensaje.

## Objetivo

Convertir la maqueta aprobada en un caso completo de `rodrigolopez.studio`, sustituyendo las capturas marcadas con VIDEO por los vídeos reales. Usar la skill `anthropic-skills:portfolio-project-intake`, en especial sus apartados de flujo, técnica y publicación.

Trabajar en la rama `draft/script-to-screen` del repo `MuyaUbuntu/web-portfolio`. No hacer merge a `main` sin el visto bueno de Rodrigo.

## Punto de partida

- **Maqueta aprobada:** https://claude.ai/artifact/KdUgBe3hmwS6JX9Jd69mik (leerla con la herramienta de artefactos)
- **Código fuente de la maqueta:** `D:\Desktop\Edicion Video\Videos\Reels con Claude\Portafolio-caso\index.html`
- **Capturas:** `D:\Desktop\Edicion Video\Videos\Reels con Claude\Portafolio-caso\img\`
- **Reglas de la marca:** `D:\Desktop\Edicion Video\Videos\Reels con Claude\Mi estilo\Reglas-de-estilo.md` (solo lectura)

Mantener contenido, orden de secciones e interacciones de la maqueta. Rodrigo dijo «me encanta». Adaptar el código a los componentes y estilos del sitio solo donde haga falta.

## Audiencia y tono

- Empresa que busca a alguien que maneje flujos de trabajo con IA para producción audiovisual.
- Todo el contenido en inglés. La conversación con Rodrigo, en español.
- Rodrigo no desarrolló las herramientas: las dirige y las adapta a la marca. La revisión humana en cada etapa es parte del mensaje.

## Vídeos finales

Carpeta base: `D:\Desktop\Edicion Video\Videos\Reels con Claude\Reels\`

| Vídeo | Carpeta | Duración |
|---|---|---|
| Vid1 · This is Bracco | `2026-10-24 · This is Bracco\V2\` | 29.9 s |
| Vid2 · What is a Point Spread | `2026-10-24 · What is a Point Spread\` | 28.5 s |
| Vid3 · What is an Over/Under | `2026-10-25 · What is an Over-Under\` | 23.4 s |
| Vid4 · What is a Parlay | `2026-10-27 · What is a Parlay\` | 20.3 s |
| Vid5 · What is a Moneyline | `2026-10-27 · What is a Moneyline\` | 22.1 s |
| Vid6 · MNF Bills vs Vikings | `2026-11-02 · MNF Bills vs Vikings\` | 28.0 s |

Cada vídeo tiene 4 archivos: `FINAL - <tema> - 1080x1920.mp4`, `1080x1350`, `1080x1080` y `1920x1080`.

**Importante:** de Vid1 usar solo la carpeta `V2`. Sus versiones en `old\` y `trabajo\finales-con-bet\` contienen la palabra prohibida.

No modificar los originales: comprimir copias para la web. Límite por archivo: menos de 20 MB. Verticales con mejor calidad que los secundarios. Añadir póster a cada vídeo (se pueden reutilizar las capturas de `img\`).

## Dónde va cada vídeo

Sustituir estas posiciones, que hoy llevan la etiqueta VIDEO (clase `.isv`):

| Sección | Qué poner | Comportamiento |
|---|---|---|
| Inicio de la página (`#fan`) | Vid1, Vid6 y Vid3 en vertical | Sin sonido, en bucle |
| Diagrama «A script goes in» (`#dImg`) | Vid6 vertical | Salta al segundo de cada palabra |
| «The script drives the motion» (`#sImg`) | Vid6 vertical | Cada palabra salta a su segundo |
| «One master, three adaptations» (`#fm`) | Vid6 en los 4 formatos | Sincronizados; los botones saltan a un momento |
| «The series» (`#gal`) | Los 6 verticales | Clic para reproducir con sonido |

Se quedan como imagen: las etapas de «Inside the workflow» y los antes y después de «How the system learned».

Tiempos de salto en Vid6: los del arreglo `S` y del bloque del diagrama en `index.html`.

Al terminar, eliminar la regla `.isv::after` y la clase `.isv`.

## Decisiones ya tomadas (no volver a preguntar)

- **Permiso:** Rodrigo confirmó que puede mostrar el trabajo.
- **Tiempos, todos marcados como aproximados y sin contar esperas de revisión:**
  - Master 9:16: ~25 min con este flujo, ~5 h en After Effects.
  - Adaptaciones: ~1:30 min cada una (~4.5 min en total), ~3–4 h en total en After Effects.
  - Vídeo completo: ~30 min frente a ~8.5 h.
  - Los tiempos del flujo se reconstruyeron a partir de las horas de los archivos. Las cifras de After Effects son estimación de Rodrigo.
- **Créditos en «Tools and role»:** Whisper, FFmpeg, HyperFrames + GSAP y SynthFlow, con el texto ya aprobado de la maqueta.
- **Palabra prohibida:** «bet», «bets» y «betting» no aparecen en el texto de la página ni en ninguna imagen o vídeo. Se habla de «a restricted word». Revisar también los textos alternativos y los metadatos.
- **Enlaces:** los vídeos se publicarán, pero aún no. Mantener «Live link: pending release» en «The series» hasta que Rodrigo pase los enlaces. Es una petición suya, aunque la skill desaconseje este tipo de avisos.
- **Sin métricas de resultados:** no inventar ninguna.

## Temas abiertos para confirmar con Rodrigo

1. **Crédito a Viegas Estudio:** el método base viene de su skill, pero se quitó de «Tools and role» a petición de Rodrigo. El texto dice «a custom Claude skill». Preguntar si prefiere «an adapted Claude skill» o una línea pequeña de crédito.
2. **Logos en Vid6:** las fotos llevan logos de los Bills y la NFL. Rodrigo los aprobó para el vídeo. Confirmar que también quiere mostrarlos en el portafolio.
3. **Tipografía:** la maqueta usa Archivo Black en lugar de BN Dime Display, que tiene licencia. Usar la tipografía de títulos del sitio salvo que indique otra cosa.
4. **Posición en el home:** preguntar en qué lugar del orden de proyectos va el caso.

## Pensado para crecer a 10 vídeos

La serie va a llegar a 10. Mantener los datos de los vídeos en una sola lista, para que añadir uno sea añadir una entrada y sus archivos. Al sumar vídeos, actualizar las cifras «6 videos so far, 10 planned» y «24 final deliverables», y añadir una fila a «How the system learned» solo si hubo una regla nueva.

## Antes de pedir aprobación

- Revisar a 360 y 390 px que nada se desborde.
- Sin errores de consola.
- Vídeos cargados de forma diferida, sin descargar los 24 al abrir la página.
- Con `prefers-reduced-motion`, sin reproducción automática.
- Publicar la vista previa según indique la skill y esperar el visto bueno antes del merge.
