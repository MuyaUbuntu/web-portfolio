"""Genera index.html y proyectos/happy-talks.html (v3).
Uso: python3 tools/build.py"""
import os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO=open(os.path.join(R,'tools','logo-inline.svg')).read().strip()
B='https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/'
HT=['684229227805201.68479f1136a54','78437e227805201.68479f11380df','1cae49227805201.68479f11379ed','09e022227805201.68479f1135bbd','a986e1227805201.68479f11372d5','c3c662227805201.68479f11361c9','b76ac6227805201.68479f1134c0e','d1dd88227805201.68479f113528b','82f81f227805201.68479f11334d1','bf5c4f227805201.68479f1133d30','66dfe8227805201.68479f11343ac']

def ph(n,alt,pre,fb='',eager=False):
    return (f'<div class="ph"><span class="fb {fb}" aria-hidden="true"></span>'
            f'<img src="{pre}assets/img/happy-talks/{n:02d}.jpg" data-fallback="{B}{HT[n-1]}.jpg" alt="{alt}" loading="{"eager" if eager else "lazy"}" decoding="async" draggable="false"></div>')

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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400..900&family=DM+Sans:opsz,wght@9..40,400..700&family=Martian+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{pre}assets/css/main.css">
<style>:root{{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}}[hidden]{{display:none!important}}</style>
</head>
<body>
<div class="ctag" id="ctag" aria-hidden="true"></div>
<div class="blot" aria-hidden="true"></div>
'''

def nav(pre,home):
    h='' if home else pre
    go='' if home else ' data-go'
    return f'''<nav class="nav" aria-label="Principal">
  <a class="nav-logo" href="{'#inicio' if home else pre}"{go} aria-label="Rodrigo López, inicio">{LOGO}</a>
  <div class="nav-links"><span class="nav-pill" aria-hidden="true"></span>
    <a href="{h}#trabajo"{go}>Trabajo</a><a href="{h}#servicios"{go}>Servicios</a><a href="{h}#sobre-mi"{go}>Sobre mí</a>
  </div>
  <a class="nav-cta" href="{h}#contacto"{go}>Hablemos</a>
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

def contact():
    return '''<section class="contact" id="contacto">
  <div class="wrap">
    <span class="mono">¿Tienes un proyecto o una vacante?</span>
    <h2 style="margin-top:1.2rem"><span class="lm"><span>Hagamos</span></span><span class="lm"><span class="o">algo</span> <span>grande</span></span></h2>
    <div class="contact-grid">
      <div>
        <span class="mail" id="mail">hola@tudominio.com</span>
        <div class="socials">
          <a href="https://www.linkedin.com/" target="_blank" rel="noopener">LinkedIn ↗</a>
          <a href="https://www.behance.net/" target="_blank" rel="noopener">Behance ↗</a>
          <a href="#contacto">CV ↓</a>
        </div>
      </div>
      <button class="blob" type="button" data-cursor="Copiar">Copiar<br>correo</button>
    </div>
    <div class="foot mono"><span>© 2026 Rodrigo López</span><span>CDMX · Remoto o reubicación</span></div>
  </div>
</section>
'''

def card(i,href,name,role,tags,kpi,kpis,media,soon=False):
    t=''.join(f'<span class="tag">{x}</span>' for x in tags)
    o=f'<a class="card" href="{href}" data-go data-cursor="Ver caso">' if not soon else '<div class="card" data-cursor="Próximamente">'
    c='</a>' if not soon else '</div>'
    s='<span class="tag b soon">Próximamente</span>' if soon else ''
    return f'''      {o}
        <div class="frame">{media}<span class="num">{i:02d}</span>{s}<div class="tags">{t}</div></div>
        <div class="info"><div><h3>{name}</h3><p>{role}</p></div><div class="kpi"><b>{kpi}</b><small>{kpis}</small></div></div>
      {c}'''

def fb(cls): return f'<div class="ph"><span class="fb {cls}"></span></div>'

# ================= HOME =================
pre=''
roles='<span>Brand Design</span><span>UX/UI</span><span>Brand Management</span><span>Dirección de arte</span><span>Modelado 3D</span><span>Empaque</span>'
roles2='<span>Ideas creativas</span><span>Resultados medibles</span><span>Marcas con carácter</span><span>Sistemas que escalan</span>'
home=head('Rodrigo López · Brand Designer & Brand Manager','Portafolio de Rodrigo López: identidades, experiencias digitales y gestión de marca con resultados medibles.',pre)+nav(pre,True)+f'''<main id="inicio">
  <section class="hero wrap">
    <canvas class="dots" aria-hidden="true"></canvas>
    <div class="hero-top">
      <div class="hello"><span class="av">{LOGO}</span><p>Hola, soy <b>Rodrigo López</b>. Brand Designer y Brand Manager en Ciudad de México.</p></div>
      <span class="avail mono"><i></i>Disponible para proyectos y vacantes</span>
    </div>
    <div>
      <h1 class="stickers" aria-label="Creative ideas, big results">
        <span class="stk s1" aria-hidden="true">Creative</span>
        <span class="stk s2" aria-hidden="true">ideas,</span>
        <span class="stk s5" aria-hidden="true">✳ desde 2018</span>
        <span class="stk s3" aria-hidden="true">big</span>
        <span class="stk s4" aria-hidden="true">results</span>
      </h1>
      <p class="drag-hint mono" style="margin-top:1rem">Arrastra las palabras ✋</p>
    </div>
    <div class="hero-bottom">
      <p>Diseño identidades y experiencias digitales que se ven distintas y se miden en resultados.</p>
      <div class="ctas">
        <a class="btn t" href="#trabajo">Ver proyectos <span class="ar">↓</span></a>
        <a class="btn o" href="#contacto">Descargar CV <span class="ar">↗</span></a>
      </div>
      <span class="scroll mono">Scroll <b>↓</b></span>
    </div>
  </section>

  <div class="ribbon" aria-hidden="true"><div class="rail">{roles*4}</div></div>
  <div class="ribbon alt" aria-hidden="true"><div class="rail">{roles2*5}</div></div>

  <section class="sec wrap" id="trabajo">
    <div class="sec-h">
      <h2><span class="lm"><span>Trabajo</span></span><span class="lm"><span>selecto<i class="n">04</i></span></span></h2>
      <p>Cada caso muestra el reto, el proceso y lo que se logró.</p>
    </div>
    <div class="grid">
{card(1,"proyectos/happy-talks.html","Happy Talks","Landing page para la plataforma de conferencias de HDO.",["Web","UX/UI","Branding"],"HDO","Cliente · 2025",ph(1,"Landing de Happy Talks",pre))}
{card(2,"","Lumen Óptica","Implementación de marca en 40 sucursales.",["Branding"],"40","sucursales",fb("c"),True)}
{card(3,"","Tierra Alta","Identidad y 8 etiquetas para mezcal artesanal.",["Branding","Empaque"],"8","etiquetas",fb("b"),True)}
{card(4,"","Pulso","Guía de marca y contenido para una fintech.",["Gestión"],"4×","contenido",fb("d"),True)}
    </div>
  </section>

  <section class="sec wrap" id="servicios" style="padding-top:0">
    <div class="sec-h">
      <h2><span class="lm"><span>Lo que</span></span><span class="lm"><span>hago</span></span></h2>
      <p>Del concepto a la implementación, y de la implementación a los resultados.</p>
    </div>
    <ul class="svc">
      <li class="open" style="--c:var(--pink)"><button type="button"><span class="i">01</span><h3>Branding &amp; identidad</h3><span class="pl" aria-hidden="true">+</span></button>
        <div class="body"><div><div class="inner"><p>Marcas con carácter, construidas como sistema: estrategia, logotipo, paleta, tipografía, empaque y manuales que funcionan en cualquier punto de contacto.</p><div class="tags"><span class="tag">Estrategia</span><span class="tag">Identidad</span><span class="tag">Empaque</span><span class="tag">Manuales</span></div></div></div></div></li>
      <li style="--c:var(--butter)"><button type="button"><span class="i">02</span><h3>UX/UI &amp; web</h3><span class="pl" aria-hidden="true">+</span></button>
        <div class="body"><div><div class="inner"><p>Experiencias digitales que cuentan la historia y convierten. Como en <a href="proyectos/happy-talks.html" data-go>Happy Talks</a>, donde una oferta intangible se volvió una landing que genera solicitudes.</p><div class="tags"><span class="tag">UX/UI</span><span class="tag">Landing pages</span><span class="tag">Prototipos</span><span class="tag">Figma</span></div></div></div></div></li>
      <li style="--c:var(--sky)"><button type="button"><span class="i">03</span><h3>Dirección de arte &amp; 3D</h3><span class="pl" aria-hidden="true">+</span></button>
        <div class="body"><div><div class="inner"><p>Fotografía, ilustración y modelado 3D para que la marca se vea distinta y se sienta humana.</p><div class="tags"><span class="tag">Dirección de arte</span><span class="tag">Ilustración</span><span class="tag">3D</span></div></div></div></div></li>
      <li style="--c:var(--tomato)"><button type="button"><span class="i">04</span><h3>Brand management</h3><span class="pl" aria-hidden="true">+</span></button>
        <div class="body"><div><div class="inner"><p>Lanzamientos planeados, proveedores coordinados y KPIs definidos antes de diseñar para medir después.</p><div class="tags"><span class="tag">Presupuesto</span><span class="tag">Proveedores</span><span class="tag">KPIs</span><span class="tag">Lanzamientos</span></div></div></div></div></li>
    </ul>
  </section>

  <section class="wrap" aria-label="Cifras">
    <div class="numbers" data-pop>
      <h2>Ocho años convirtiendo <em>ideas creativas</em> en resultados.</h2>
      <div class="nums">
        <div><span class="odo" data-v="8"></span><small>años en diseño de marca</small></div>
        <div><span class="odo" data-v="30+"></span><small>marcas lanzadas o rediseñadas</small></div>
        <div><span class="odo" data-v="120+"></span><small>SKUs llevados a producción</small></div>
        <div><span class="odo" data-v="4"></span><small>lanzamientos con KPIs medidos</small></div>
      </div>
      <span class="nums-ex">Cifras de ejemplo</span>
    </div>
  </section>

  <section class="sec wrap" id="sobre-mi">
    <div class="about">
      <div class="polas">
        <div class="pola a" data-cursor="Arrastra">{fb("")}<small>Retrato · reemplazar</small></div>
        <div class="pola b" data-cursor="Arrastra">{ph(6,"Happy Speakers, de la landing de Happy Talks",pre,"b")}<small>Happy Talks · 2025</small></div>
        <span class="bubble">¡Hola! 👋</span>
      </div>
      <div>
        <span class="mono muted">Sobre mí</span>
        <h2 style="margin-top:1rem"><span class="lm"><span>Del diseño</span></span><span class="lm"><span>a la <em>gestión</em></span></span></h2>
        <p>Mi base es el diseño. En los últimos años he tomado decisiones de presupuesto, coordinado proveedores y medido resultados.</p>
        <p>Hoy busco crecer hacia la gestión de marca, sin dejar de hacer lo que mejor sé: que una marca se vea y se sienta distinta.</p>
        <div class="tags"><span class="tag t">Identidad visual</span><span class="tag p">UX/UI</span><span class="tag b">Brand management</span><span class="tag">Dirección de arte</span><span class="tag">3D</span><span class="tag">Figma</span><span class="tag">Adobe CC</span></div>
      </div>
    </div>
  </section>
</main>
'''+contact()+scripts(pre)
open(os.path.join(R,'index.html'),'w').write(home)

# ================= CASO =================
pre='../'
shots=[(3,'Hero','Un micrófono modelado en 3D rompe la palabra HAPPY.'),(4,'Conferencias','Índice tipográfico fácil de recorrer.'),(5,'Historia','Video y storytelling de una sesión.'),(6,'Speakers','Retratos sobre formas orgánicas.'),(7,'Prueba social','Asistentes y marcas que ya confiaron.'),(8,'Eventos','Fotografía real que hace tangible la oferta.'),(9,'Temas','Stickers y tipografía en collage.'),(10,'Solicitud','Un formulario corto, el objetivo de la landing.')]
gal='\n'.join(f'        <figure class="shot">{ph(n,f"Sección {t} de la landing de Happy Talks",pre)}<figcaption><b>{i+1:02d} · {t}</b><span>{d}</span></figcaption></figure>' for i,(n,t,d) in enumerate(shots))
def word(w,cls=''):
    return f'<span class="w {cls}">'+''.join(f'<span class="lt">{c}</span>' for c in w)+'</span>'
case=head('Happy Talks · Rodrigo López','Caso de estudio: landing page de Happy Talks para HDO. UX/UI, branding, dirección de arte y modelado 3D.',pre)+nav(pre,False)+f'''<main>
  <section class="c-hero wrap">
    <a class="back" href="{pre}#trabajo" data-go>← Todos los proyectos</a>
    <h1 class="c-title" aria-label="Happy Talks"><span aria-hidden="true">{word("Happy","hlw")} {word("Talks")}</span></h1>
    <div class="c-row">
      <div>
        <p>Una landing para la plataforma de conferencias de HDO: una oferta intangible convertida en una experiencia visual que presenta a los speakers y genera solicitudes.</p>
        <div class="tags"><span class="tag t">UX/UI</span><span class="tag p">Branding</span><span class="tag b">Dirección de arte</span><span class="tag">Modelado 3D</span><span class="tool t-ai" title="Illustrator">Ai</span><span class="tool t-ps" title="Photoshop">Ps</span><span class="tool t-fg" title="Figma">Fg</span></div>
      </div>
      <dl class="facts">
        <div><dt class="mono">Mi rol</dt><dd>UX/UI, branding, arte y 3D</dd></div>
        <div><dt class="mono">Cliente</dt><dd>HDO</dd></div>
        <div><dt class="mono">Año</dt><dd>2025</dd></div>
        <div class="todo"><dt class="mono">Resultado</dt><dd>Por agregar</dd></div>
      </dl>
    </div>
  </section>

  <section class="cover" aria-label="Portada">{ph(1,"Landing de Happy Talks en una laptop",pre,"",True)}</section>

  <div class="wrap chapters">
    <aside class="toc" aria-label="Capítulos">
      <ol><li><a href="#reto">El reto</a></li><li><a href="#enfoque">Enfoque</a></li><li><a href="#landing">La landing</a></li><li><a href="#concepto">Concepto</a></li><li><a href="#resultados">Resultados</a></li></ol>
      <div class="bar"><i></i></div>
    </aside>
    <div>
      <section class="chap" id="reto">
        <span class="mono">01 · El reto</span>
        <h2><span class="lm"><span>Hacer tangible</span></span><span class="lm"><span>lo intangible</span></span></h2>
        <div class="quotes">
          <div class="quote a"><b>01</b><p>Comunicar una oferta intangible, las conferencias, de manera tangible y atractiva.</p></div>
          <div class="quote b"><b>02</b><p>Diferenciarse en un mercado competido de servicios de desarrollo organizacional.</p></div>
        </div>
      </section>

      <section class="chap" id="enfoque">
        <span class="mono">02 · Enfoque</span>
        <h2><span class="lm"><span>Una conferencia que</span></span><span class="lm"><span>no parece conferencia</span></span></h2>
        <p class="lead">Happy Talks ofrece conferencias disruptivas que provocan reflexión y detonan el cambio en las organizaciones. La landing tenía que sentirse igual: auténtica, memorable y lejos de lo corporativo.</p>
        <div class="lists">
          <div><h3>Metas</h3><ul><li>Presentar el portafolio de speakers y conferencias.</li><li>Generar leads con una ruta clara hacia la solicitud.</li><li>Contar la historia con una estructura ágil.</li></ul></div>
          <div><h3>Alcance</h3><ul><li>UX/UI de la landing, desktop y móvil</li><li>Lenguaje visual: tipografía, color y stickers</li><li>Dirección de arte, fotografía e ilustración</li><li>Modelado 3D de elementos clave</li></ul></div>
        </div>
      </section>

      <section class="chap" id="landing">
        <span class="mono">03 · La landing</span>
        <h2><span class="lm"><span>Sección por sección</span></span></h2>
        <p class="lead">Del primer impacto a la solicitud de conferencia. Arrastra para recorrerla.</p>
        <div class="drag">
          <div class="drag-track" tabindex="0" aria-label="Pantallas de la landing" data-cursor="Arrastra">
{gal}
          </div>
          <div class="drag-ui"><div class="bar"><i></i></div><div class="ar"><button type="button" data-prev aria-label="Anterior">←</button><button type="button" data-next aria-label="Siguiente">→</button></div></div>
        </div>
        <div class="wipe">{ph(2,"Introducción de Happy Talks con stickers de temas",pre)}</div>
      </section>

      <section class="chap" id="concepto">
        <span class="mono">04 · Concepto</span>
        <h2><span class="lm"><span>Energía con</span></span><span class="lm"><span>rostro humano</span></span></h2>
        <div class="swatches" aria-label="Paleta de Happy Talks">
          <div class="sw" style="background:#141218;color:#fff">Negro escenario</div>
          <div class="sw" style="background:#B45CF2;color:#141218">Morado</div>
          <div class="sw" style="background:#FFE14D;color:#141218">Amarillo</div>
          <div class="sw" style="background:#3DDC97;color:#141218">Menta</div>
          <div class="sw" style="background:#FF4FD8;color:#141218">Magenta</div>
        </div>
        <div class="concept">
          <div><h3>Tonos vibrantes que transmiten energía y positividad</h3><p>Para que la marca se sienta como un evento y no como un servicio corporativo.</p></div>
          <div><h3>Ilustración y fotografía que humanizan la marca</h3><p>Retratos reales de speakers con trazos y stickers dibujados a mano.</p></div>
        </div>
        <div class="wipe tall">{ph(11,"La landing de Happy Talks en móvil",pre)}</div>
      </section>

      <section class="chap" id="resultados">
        <span class="mono">05 · Resultados</span>
        <div class="todo-box">
          <h3>Métricas por agregar</h3>
          <p>Aquí irán los resultados del proyecto: solicitudes de conferencia, conversión o tiempo en página.</p>
          <a class="btn o" href="https://www.behance.net/gallery/227805201/Landing-Happy-Talks" target="_blank" rel="noopener">Ver en Behance <span class="ar">↗</span></a>
        </div>
      </section>
    </div>
  </div>

  <a class="next" href="{pre}#trabajo" data-go data-cursor="Ver todo">
    <div class="wrap"><span class="mono">Siguiente</span><h2>Lumen Óptica →</h2></div>
    <div class="peek ph"><span class="fb c"></span></div>
    <div class="wrap"><div class="foot mono"><span>© 2026 Rodrigo López</span><span>Caso 01 / 04</span></div></div>
  </a>
</main>
'''+scripts(pre)
open(os.path.join(R,'proyectos','happy-talks.html'),'w').write(case)
print('ok')
