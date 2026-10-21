"""Genera index.html y proyectos/happy-talks.html a partir de bloques compartidos.
Uso: python3 tools/build.py"""
import os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO=open(os.path.join(R,'tools','logo-inline.svg')).read().strip()
B='https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/'
HT=['684229227805201.68479f1136a54','78437e227805201.68479f11380df','1cae49227805201.68479f11379ed','09e022227805201.68479f1135bbd','a986e1227805201.68479f11372d5','c3c662227805201.68479f11361c9','b76ac6227805201.68479f1134c0e','d1dd88227805201.68479f113528b','82f81f227805201.68479f11334d1','bf5c4f227805201.68479f1133d30','66dfe8227805201.68479f11343ac']

def img(n,alt,pre,eager=False,fb='a'):
    load='eager' if eager else 'lazy'
    return (f'<span class="fallback {fb}" aria-hidden="true"></span>'
            f'<img src="{pre}assets/img/happy-talks/{n:02d}.jpg" data-fallback="{B}{HT[n-1]}.jpg" alt="{alt}" loading="{load}" decoding="async">')

def stroke(): return '<svg class="stroke" viewBox="0 0 200 20" preserveAspectRatio="none" aria-hidden="true"><path pathLength="1"/></svg>'
def hl(href,text,icon,extra=''): return f'<a class="hl" href="{href}"{extra}><span class="hl-t">{text}{stroke()}</span><span class="hl-i" aria-hidden="true">{icon}</span></a>'

def head(title,desc,pre):
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="{pre}assets/img/logo.svg">
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Instrument+Sans:wght@400..700&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{pre}assets/css/main.css">
<style>:root{{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}}[hidden]{{display:none!important}}</style>
</head>
<body>
<div class="cursor" id="cursor" aria-hidden="true"><span id="cursorLabel">Ver</span></div>
<div class="curtain" aria-hidden="true">{LOGO.replace('class="logo"','class="logo"')}</div>
'''

def chrome(pre,home):
    brand_href='#inicio' if home else f'{pre}'
    t='' if home else ' data-transition'
    return f'''<header class="top">
  <div class="wrap">
    <a class="brand" href="{brand_href}"{t} aria-label="Rodrigo López, inicio">{LOGO}</a>
    <div class="top-r">
      <a class="top-cta" href="{'' if home else pre}#contacto"{t}><span data-scramble-hover>Hablemos</span></a>
      <button class="burger" type="button" id="burger" aria-label="Abrir menú" aria-expanded="false" aria-controls="menu">
        <svg viewBox="0 0 28 28" aria-hidden="true"><path/><path/><path/></svg>
      </button>
    </div>
  </div>
</header>
<nav class="menu" id="menu" aria-label="Menú principal" aria-hidden="true">
  <div class="wrap menu-in">
    <ul>
      <li><a href="{'' if home else pre}#proyectos"{t} data-lens aria-label="Proyectos"><span class="lens-txt">Proyectos</span></a></li>
      <li><a href="{'' if home else pre}#capacidades"{t} data-lens aria-label="Capacidades"><span class="lens-txt">Capacidades</span></a></li>
      <li><a href="{'' if home else pre}#perfil"{t} data-lens aria-label="Perfil"><span class="lens-txt">Perfil</span></a></li>
      <li><a href="{'' if home else pre}#contacto"{t} data-lens aria-label="Contacto"><span class="lens-txt">Contacto</span></a></li>
    </ul>
    <div class="menu-foot mono"><span>hola@tudominio.com</span><span>CDMX · Remoto o reubicación</span></div>
  </div>
</nav>
'''

def scripts(pre):
    return f'''<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="{pre}assets/js/main.js"></script>
</body>
</html>
'''

def contact(pre):
    return f'''<section class="contact" id="contacto">
  <div class="wrap">
    <span class="mono">¿Tienes un proyecto o una vacante?</span>
  </div>
  <div class="contact-big" aria-hidden="true">Hablemos <span class="o">Hablemos</span> Hablemos</div>
  <div class="wrap">
    <h2 class="sr">Hablemos</h2>
    <div class="contact-row">
      <span class="mail" id="mail">hola@tudominio.com</span>
      <button class="btn" type="button" id="copy" data-magnetic>Copiar correo</button>
    </div>
    <div class="contact-row" style="margin-top:2.4rem;justify-content:flex-start;gap:1rem 3rem">
      {hl("https://www.linkedin.com/","LinkedIn","↗",' target="_blank" rel="noopener"')}
      {hl("https://www.behance.net/","Behance","↗",' target="_blank" rel="noopener"')}
      {hl(f"{pre}#contacto","Descargar CV","↓")}
    </div>
    <div class="foot mono"><span>© 2026 Rodrigo López</span><span>Hecho con criterio humano y un poco de código</span></div>
  </div>
</section>
'''

def proj(href,name,tags,role,kpi,kpis,media,soon=False,pre=''):
    tag=f'<a class="proj" href="{href}" data-transition data-cursor="Ver caso">' if not soon else '<div class="proj soon" data-cursor="Pronto">'
    end='</a>' if not soon else '</div>'
    pills=''.join(f'<span class="pill">{t}</span>' for t in tags)
    return f'''      {tag}
        <div class="media">{media}<div class="tags"><span class="pills">{pills}</span>{'<span class="pill">Próximamente</span>' if soon else ''}</div><span class="name"><i class="spark"></i>{name}</span></div>
        <div class="meta"><p>{role}</p><div class="kpi">{kpi}<small>{kpis}</small></div></div>
      {end}'''

# ---------------- HOME ----------------
pre=''
home=head('Rodrigo López · Brand Designer & Brand Manager','Portafolio de Rodrigo López: identidades, experiencias digitales y gestión de marca con resultados medibles.',pre)+chrome(pre,True)+f'''<main id="inicio">
  <section class="hero wrap">
    <div class="hero-kick mono"><span>Brand Designer &amp; Brand Manager</span><span>Ciudad de México · Remoto o reubicación</span></div>
    <h1 data-lens data-scramble aria-label="Creative ideas, big results"><span class="lens-txt">Creative ideas,<br>big results</span></h1>
    <a class="hero-card media" href="proyectos/happy-talks.html" data-transition data-cursor="Ver caso" aria-label="Ver caso Happy Talks">{img(1,"Landing de Happy Talks",pre,True)}</a>
    <div class="hero-foot">
      <p><span class="badge pill blue"><i class="spark"></i>Portafolio 2026</span>Diseño identidades y experiencias digitales que se ven distintas y se miden en resultados.</p>
      <div class="hero-links">
        {hl("#proyectos","Ver proyectos","↓")}
        {hl("#contacto","Descargar CV","↗")}
      </div>
      <div class="scroll-cue mono"><i></i>Scroll</div>
    </div>
  </section>

  <section class="reel-wrap wrap" aria-label="Caso destacado">
    <a class="reel" href="proyectos/happy-talks.html" data-transition data-cursor="Ver caso">
      <div class="media">{img(3,"Hero de la landing de Happy Talks",pre)}</div>
      <div class="reel-label"><div><span class="mono">Caso destacado · HDO · 2025</span><h2>Happy Talks</h2></div><span class="pill" style="color:#fff">Ver caso →</span></div>
    </a>
  </section>

  <section class="statement wrap">
    <span class="mono"><i class="spark" style="color:var(--blue)"></i>Sobre mi trabajo</span>
    <p data-words>Ocho años diseñando marcas que se reconocen al instante. Hoy sumo <em>estrategia, datos y gestión de equipos</em> para que cada decisión creativa tenga un resultado medible.</p>
  </section>

  <section class="wrap panels" id="capacidades" aria-label="Capacidades">
    <article class="panel p1" style="--i:0">
      <div><span class="mono">01 · Capacidad</span><h2>Branding &amp;<br>identidad</h2></div>
      <div>
        <div class="pills"><span class="pill">Estrategia</span><span class="pill">Identidad</span><span class="pill">Empaque</span><span class="pill">Manuales</span></div>
        <p class="lead">Marcas con carácter, construidas como sistema.</p>
        <p class="body">De la estrategia al logotipo, la paleta y el manual. Cada identidad se diseña para funcionar en cualquier punto de contacto, no solo en la presentación.</p>
        <div class="stats"><div><b data-count>30+</b><span>identidades</span></div><div><b data-count>120+</b><span>SKUs de empaque</span></div><div><b data-count>6</b><span>manuales</span></div></div>
      </div>
      <i class="steps" aria-hidden="true"></i>
    </article>
    <article class="panel p2" style="--i:1">
      <div><span class="mono">02 · Capacidad</span><h2>UX/UI &amp;<br>experiencias<br>digitales</h2></div>
      <div>
        <div class="pills"><span class="pill">UX/UI</span><span class="pill">Landing pages</span><span class="pill">Dirección de arte</span><span class="pill">3D</span></div>
        <p class="lead">Experiencias que cuentan la historia y convierten.</p>
        <p class="body">Arquitectura, interfaz y dirección de arte para sitios que se recuerdan. Como Happy Talks, donde una oferta intangible se volvió una experiencia visual que genera solicitudes.</p>
        <div style="margin-top:2rem">{hl("proyectos/happy-talks.html","Ver Happy Talks","→",' data-transition')}</div>
      </div>
      <i class="steps" aria-hidden="true"></i>
    </article>
    <article class="panel p3" style="--i:2">
      <div><span class="mono">03 · Capacidad</span><h2>Brand<br>management</h2></div>
      <div>
        <div class="pills"><span class="pill">Presupuesto</span><span class="pill">Proveedores</span><span class="pill">KPIs</span><span class="pill">Lanzamientos</span></div>
        <p class="lead">La marca, de la idea al mercado.</p>
        <p class="body">Planeación de lanzamientos, coordinación de equipos y agencias, y KPIs definidos antes de diseñar para medir después.</p>
        <div class="stats"><div><b data-count>$2.4M</b><span>MXN administrados</span></div><div><b data-count>9</b><span>proveedores coordinados</span></div><div><b data-count>4</b><span>lanzamientos medidos</span></div></div>
        <p class="mono" style="margin-top:1rem;opacity:.6">Cifras de ejemplo</p>
      </div>
      <i class="steps" aria-hidden="true"></i>
    </article>
  </section>

  <section class="giant" aria-hidden="true">
    <div class="giant-row">Trabajo <span class="o">Selecto</span> Trabajo</div>
    <div class="giant-row"><span class="o">Selecto</span> Trabajo <span class="o">Selecto</span></div>
    <div class="giant-card media">{img(6,"",pre,fb='b')}</div>
  </section>

  <section class="work" id="proyectos" aria-label="Proyectos">
    <div class="wrap work-head">
      <h2 class="sr">Proyectos</h2>
      <p>Cada caso muestra el reto, el proceso y lo que se logró.</p>
      <div class="pills"><span class="pill fill">Todos</span><span class="pill">Branding</span><span class="pill">Web</span><span class="pill">Gestión</span></div>
    </div>
    <div class="work-track">
{proj("proyectos/happy-talks.html","Happy Talks",["Web","Branding"],"Landing page para la plataforma de conferencias de HDO. UX/UI, branding, dirección de arte y 3D.","HDO","Cliente · 2025",img(1,"Happy Talks",pre))}
{proj("","Lumen Óptica",["Branding"],"Implementación de marca en 40 sucursales.","40","sucursales","<span class='fallback c'></span>",True)}
{proj("","Tierra Alta",["Branding","Empaque"],"Identidad y sistema de 8 etiquetas para mezcal artesanal.","8","etiquetas","<span class='fallback b'></span>",True)}
{proj("","Pulso",["Gestión"],"Guía de marca y producción de contenido para una fintech.","4×","contenido mensual","<span class='fallback d'></span>",True)}
    </div>
    <div class="work-progress" aria-hidden="true"><i></i></div>
  </section>

  <section class="about wrap" id="perfil">
    <div class="about-grid">
      <div data-rise>
        <span class="mono muted">Perfil</span>
        <h2 style="margin-top:1rem">Del diseño <span>a la gestión</span></h2>
      </div>
      <div data-rise>
        <p class="lead">Mi base es el diseño. En los últimos años he tomado decisiones de presupuesto, coordinado proveedores y medido resultados, y busco seguir creciendo hacia la gestión de marca.</p>
        <div class="metrics">
          <div><b data-count>8</b><span>años en diseño de marca</span></div>
          <div><b data-count>30+</b><span>marcas lanzadas o rediseñadas</span></div>
          <div><b data-count>120+</b><span>SKUs llevados a producción</span></div>
          <div><b data-count>4</b><span>lanzamientos con KPIs medidos</span></div>
        </div>
        <div class="chips"><span class="pill">Identidad visual</span><span class="pill">Estrategia de marca</span><span class="pill">UX/UI</span><span class="pill">Dirección de arte</span><span class="pill">Modelado 3D</span><span class="pill">Brand guidelines</span><span class="pill">Gestión de proveedores</span><span class="pill">Figma</span><span class="pill">Adobe CC</span></div>
      </div>
    </div>
  </section>
</main>
'''+contact(pre)+scripts(pre)
open(os.path.join(R,'index.html'),'w').write(home)

# ---------------- CASO HAPPY TALKS ----------------
pre='../'
screens=[
 (3,'Hero','Un micrófono modelado en 3D rompe la palabra HAPPY: la conferencia es protagonista desde el primer segundo.','wide dark'),
 (4,'Conferencias','Las tres conferencias como índice tipográfico, fácil de recorrer y comparar.',''),
 (5,'Historia de aprendizaje','Video y storytelling para explicar qué vive una organización en una sesión.','dark'),
 (6,'Happy Speakers','Retratos sobre formas orgánicas y cifras de asistentes.','wide'),
 (7,'Prueba social','Asistentes impactados y marcas que ya confiaron en HDO.',''),
 (8,'Nuestras conferencias','Fotografía real de eventos que hace tangible la oferta.','dark'),
 (10,'Solicitud de conferencia','El cierre convierte: un formulario corto, el objetivo principal de la landing.','wide dark'),
]
sc='\n'.join(f'''      <article class="screen {cls}">
        <div class="cap"><h3>{t}</h3><span class="mono muted">{i+1:02d} / {len(screens):02d}</span></div>
        <div class="media" data-blur>{img(n,f"Sección {t} de la landing de Happy Talks",pre)}</div>
        <p>{d}</p>
      </article>''' for i,(n,t,d,cls) in enumerate(screens))
case=head('Happy Talks · Rodrigo López','Caso de estudio: landing page de Happy Talks para HDO. UX/UI, branding, dirección de arte y modelado 3D.',pre)+chrome(pre,False)+f'''<main>
  <section class="c-hero wrap">
    <a class="crumb mono" href="{pre}#proyectos" data-transition>← Todos los proyectos</a>
    <h1 data-lens data-scramble aria-label="Happy Talks"><span class="lens-txt">Happy<br>Talks</span></h1>
    <div class="c-intro">
      <p>Landing page para la plataforma de conferencias de HDO: una oferta intangible convertida en una experiencia visual que presenta a los speakers y genera solicitudes.</p>
      <div style="display:grid;gap:.8rem;justify-items:start">
        <div class="pills"><span class="pill blue">UX/UI</span><span class="pill">Branding</span><span class="pill">Dirección de arte</span><span class="pill">Modelado 3D</span></div>
        <div class="tools"><span class="tool t-ai" title="Illustrator">Ai</span><span class="tool t-ps" title="Photoshop">Ps</span><span class="tool t-fg" title="Figma">Fg</span></div>
      </div>
    </div>
    <dl class="c-meta">
      <div><dt class="mono">Mi rol</dt><dd>UX/UI, branding, dirección de arte y 3D</dd></div>
      <div><dt class="mono">Cliente</dt><dd>HDO · Human Design Doing</dd></div>
      <div><dt class="mono">Año</dt><dd>2025</dd></div>
      <div class="todo"><dt class="mono">Resultado</dt><dd>Pendiente de agregar</dd></div>
    </dl>
  </section>

  <section class="c-reel" aria-label="Portada">
    <div class="media">{img(1,"Landing de Happy Talks en una laptop",pre,True)}</div>
  </section>

  <section class="wrap">
    <div class="key">
      <span class="pill"><i class="spark"></i>Punto clave</span>
      <h2>¿Cuál era<br>el reto?</h2>
      <div class="key-grid">
        <div data-rise><b>01</b><p>Comunicar una oferta intangible, las conferencias, de manera tangible y atractiva.</p></div>
        <div data-rise><b>02</b><p>Diferenciarse en un mercado competido de servicios de desarrollo organizacional.</p></div>
      </div>
      <i class="steps" aria-hidden="true"></i>
    </div>
  </section>

  <section class="approach wrap">
    <span class="mono muted">Enfoque</span>
    <div>
      <p class="big" data-words>Happy Talks ofrece conferencias disruptivas que provocan reflexión y detonan el cambio. La landing tenía que sentirse igual: <em style="font-style:normal;color:var(--blue)">auténtica, memorable y lejos de lo corporativo.</em></p>
      <div class="cols">
        <div data-rise><h3>Metas</h3><ul><li>Presentar el portafolio de speakers y conferencias.</li><li>Generar leads con una ruta clara hacia la solicitud.</li><li>Contar la historia con una estructura ágil.</li></ul></div>
        <div data-rise><h3>Alcance</h3><ul><li>UX/UI de la landing, desktop y móvil</li><li>Lenguaje visual: tipografía, color y stickers</li><li>Dirección de arte, fotografía e ilustración</li><li>Modelado 3D de elementos clave</li></ul></div>
      </div>
    </div>
  </section>

  <section class="wrap" aria-label="La landing sección por sección">
    <div class="screens">
{sc}
    </div>
  </section>

  <section class="c-giant" aria-hidden="true">
    <div class="giant-row">Energía <span class="o">Color</span> Energía</div>
    <div class="giant-row"><span class="o">Humano</span> Visual <span class="o">Humano</span></div>
    <div class="giant-card media">{img(9,"",pre,fb='b')}</div>
  </section>

  <section class="wrap" aria-label="Concepto visual">
    <div class="concept">
      <div class="cc a" data-rise><span class="mono">Decisión 01</span><h3>Tonos vibrantes que transmiten energía y positividad</h3><p>Morado, amarillo y verde menta sobre negro, para que la marca se sienta como un evento y no como un servicio corporativo.</p></div>
      <div class="cc b" data-rise><span class="mono">Decisión 02</span><h3>Ilustración y fotografía que humanizan la marca</h3><p>Retratos reales de speakers y eventos, con trazos y stickers dibujados a mano, para conectar con el público.</p></div>
    </div>
    <div class="mobile"><div class="media" data-blur>{img(11,"La landing de Happy Talks en móvil",pre)}</div></div>
  </section>

  <section class="results wrap">
    <div class="results-box">
      <span class="mono muted">Resultados</span>
      <h2>Próximamente</h2>
      <p class="muted">Aquí irán las métricas del proyecto: solicitudes de conferencia, conversión o tiempo en página.</p>
      <div>{hl("https://www.behance.net/gallery/227805201/Landing-Happy-Talks","Ver en Behance","↗",' target="_blank" rel="noopener"')}</div>
    </div>
  </section>

  <a class="next" href="{pre}#proyectos" data-transition data-cursor="Ver todo">
    <div class="wrap"><span class="mono">Siguiente proyecto</span></div>
    <h2 class="wrap" style="white-space:nowrap">Lumen Óptica · Lumen Óptica</h2>
    <div class="peek media"><span class="fallback c"></span></div>
    <div class="wrap"><div class="foot mono" style="margin-top:3rem"><span>© 2026 Rodrigo López</span><span>Caso 01 / 04</span></div></div>
  </a>
</main>
'''+scripts(pre)
open(os.path.join(R,'proyectos','happy-talks.html'),'w').write(case)
print('ok')
