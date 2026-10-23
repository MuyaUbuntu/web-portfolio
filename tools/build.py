"""Builds index.html and the case pages (v3.1).
Usage: python3 tools/build.py"""
import os, json
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO=open(os.path.join(R,'tools','logo-inline.svg')).read().strip()
B='https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/'
HT=['684229227805201.68479f1136a54','78437e227805201.68479f11380df','1cae49227805201.68479f11379ed','09e022227805201.68479f1135bbd','a986e1227805201.68479f11372d5','c3c662227805201.68479f11361c9','b76ac6227805201.68479f1134c0e','d1dd88227805201.68479f113528b','82f81f227805201.68479f11334d1','bf5c4f227805201.68479f1133d30','66dfe8227805201.68479f11343ac']
EMAIL='rodrigo.lopez.1293@gmail.com'
WA='https://wa.me/522226858390'
IG='https://www.instagram.com/rodrigo_1293/'
LI='https://www.linkedin.com/in/rodrigo-lp/'

def ht(n,alt,pre,eager=False):
    return (f'<div class="ph"><span class="fb" aria-hidden="true"></span>'
            f'<img src="{pre}assets/img/happy-talks/{n:02d}.jpg" data-fallback="{B}{HT[n-1]}.jpg" alt="{alt}" loading="{"eager" if eager else "lazy"}" decoding="async" draggable="false"></div>')
def ai(name,alt,pre,cls='ph',eager=False):
    return f'<div class="{cls}"><img src="{pre}assets/img/ai/{name}.jpg" alt="{alt}" loading="{"eager" if eager else "lazy"}" decoding="async" draggable="false"></div>'

def head(title,desc,pre):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" type="image/svg+xml" href="{pre}assets/img/logo.svg">
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300..800&display=swap">
<link rel="stylesheet" href="{pre}assets/css/main.css">
<style>:root{{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}}[hidden]{{display:none!important}}</style>
</head>
<body>
<div class="ctag" id="ctag" aria-hidden="true"></div>
<div class="blot" aria-hidden="true"><canvas></canvas></div>
'''

def nav(pre,home):
    h='' if home else pre; go='' if home else ' data-go'
    return f'''<nav class="nav" aria-label="Main">
  <a class="nav-logo" href="{'#top' if home else pre}"{go} aria-label="Rodrigo López, home">{LOGO}</a>
  <div class="nav-links"><span class="nav-pill" aria-hidden="true"></span>
    <a href="{h}#work"{go}>Work</a><a href="{h}#services"{go}>Services</a><a href="{h}#be-creative"{go}>Be creative</a>
  </div>
  <a class="nav-cta" href="{h}#contact"{go}>Let’s talk</a>
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

ICON_WA='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-3.9-4.7-4.1-.1-.2-1.1-1.5-1.1-2.9 0-1.4.7-2 1-2.3.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.4.6-.4.4c-.1.2-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.1 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.6-.1 1.2Z"/></svg>'
ICON_IG='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7.3A4.7 4.7 0 1 0 12 16.7 4.7 4.7 0 0 0 12 7.3Zm0 7.7A3 3 0 1 1 12 9a3 3 0 0 1 0 6Zm6-7.9a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0ZM21.9 8c0-1.6-.4-3-1.6-4.2S17.6 2.1 16 2c-1.6-.1-6.4-.1-8 0-1.6.1-3 .4-4.2 1.6S2.1 6.4 2 8c-.1 1.6-.1 6.4 0 8 .1 1.6.4 3 1.6 4.2s2.6 1.6 4.2 1.7c1.6.1 6.4.1 8 0 1.6-.1 3-.4 4.2-1.7 1.2-1.2 1.6-2.6 1.6-4.2.1-1.6.1-6.4 0-8Z"/></svg>'
ICON_LI='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 3.5A2 2 0 1 1 5 7.5 2 2 0 0 1 5 3.5ZM3.3 9h3.4v11H3.3V9Zm5.6 0h3.3v1.5h.1c.5-.9 1.6-1.8 3.3-1.8 3.5 0 4.1 2.3 4.1 5.3V20h-3.4v-5.3c0-1.3 0-2.9-1.8-2.9s-2 1.4-2 2.8V20H8.9V9Z"/></svg>'

def contact():
    return f'''<section class="contact" id="contact">
  <div class="wrap">
    <span class="mono">Got a project or an open role?</span>
    <h2 style="margin-top:1.2rem"><span class="lm"><span>Let’s make</span></span><span class="lm lm-last"><span class="o">something</span> <span>big</span></span></h2>
    <div class="contact-grid">
      <div>
        <span class="mail" id="mail">{EMAIL}</span>
        <div class="socials">
          <a class="wa" href="{WA}" target="_blank" rel="noopener">{ICON_WA}WhatsApp</a>
          <a href="{LI}" target="_blank" rel="noopener">{ICON_LI}LinkedIn</a>
          <a href="{IG}" target="_blank" rel="noopener">{ICON_IG}Instagram</a>
        </div>
      </div>
      <button class="blob" type="button" data-cursor="Copy">Copy<br>email</button>
    </div>
    <div class="foot mono"><span>© 2026 Rodrigo López</span><span>Mexico · Open to remote</span></div>
  </div>
</section>
'''

def card(i,href,client,name,role,tags,media,ref=None,aiflag=False,soon=False):
    t=''.join(f'<span class="tag">{x}</span>' for x in tags)
    o=f'<a class="card" href="{href}" data-go data-zoom data-cursor="{"See process" if aiflag else "See case"}">' if not soon else f'<div class="card soon" data-cursor="Coming soon">'
    c='</a>' if not soon else '</div>'
    refh=f'<div class="ref" aria-hidden="true"><img src="assets/img/ai/{ref}.jpg" alt="" loading="lazy" draggable="false"><span class="lbl tag k">Before AI · sketch</span></div>' if ref else ''
    badges=('<span class="ai">AI process</span>' if aiflag else '')
    go='<span class="go" aria-hidden="true">Soon</span>' if soon else '<span class="go" aria-hidden="true">→</span>'
    return f'''      {o}
        <div class="frame">{media}{refh}<span class="num">{i:02d}</span><div class="badges">{badges}</div></div>
        <div class="info"><div><span class="client">{client}</span><h3>{name}</h3><p>{role}</p><div class="tags">{t}</div></div>{go}</div>
      {c}'''

# ================= HOME =================
pre=''
roles='<span>Art direction</span><span>AI imagery</span><span>UX/UI</span><span>3D</span><span>Internal campaigns</span><span>Brand management</span>'
roles2='<span>Creative ideas</span><span>Big results</span><span>Human craft</span><span>Strategy first</span>'
pairs=[{'name':'Philip Morris','ref':'assets/img/ai/pmi-humo-ref.jpg','fin':'assets/img/ai/pmi-humo-final.jpg'},
       {'name':'Coca-Cola','ref':'assets/img/ai/coca-ref.jpg','fin':'assets/img/ai/coca-final.jpg'},
       {'name':'DiDi Food','ref':'assets/img/ai/didi-ref.jpg','fin':'assets/img/ai/didi-final.jpg'},
       {'name':'Megagas','ref':'assets/img/ai/megagas-ref.jpg','fin':'assets/img/ai/megagas-final.jpg'},
       {'name':'ArcelorMittal','ref':'assets/img/ai/arcelor-ref.jpg','fin':'assets/img/ai/arcelor-final.jpg'}]
home=head('Rodrigo López · Designer & Art Director','Portfolio of Rodrigo López: art direction, AI-powered campaigns, UX/UI and 3D for global brands.',pre)+nav(pre,True)+f'''<main id="top">
  <section class="hero wrap">
    <canvas class="dots" aria-hidden="true"></canvas>
    <div class="hero-top">
      <div class="hello"><span class="av">{LOGO}</span><p>Hi, I’m <b>Rodrigo López</b>. Designer and art director from Mexico, working with global brands.</p></div>
      <span class="avail mono"><i></i>Open to projects &amp; roles</span>
    </div>
    <div>
      <h1 class="stickers" aria-label="Creative ideas, big results">
        <span class="stk s1 keep-case" aria-hidden="true">Creative</span>
        <span class="stk s2" aria-hidden="true">ideas,</span>
        <span class="stk s5" aria-hidden="true">✳ since 2016</span>
        <span class="stk s3 keep-case" aria-hidden="true">big</span>
        <span class="stk s4" aria-hidden="true">results</span>
      </h1>
      <p class="drag-hint"><span class="dh-ic" aria-hidden="true"><svg viewBox="0 0 64 44" width="64" height="44"><g class="dh-move"><rect x="8" y="8" width="26" height="18" rx="4" fill="#FF4417"/><path d="M27 20 L27 40 L32 35 L35.5 42.5 L39 41 L35.6 33.6 L42.5 33.6 Z" fill="#0B0B0A" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/></g><rect class="dh-ghost" x="8" y="8" width="26" height="18" rx="4" fill="none" stroke="#0B0B0A" stroke-width="1.4" stroke-dasharray="3 3"/></svg></span><span>Drag the words around</span></p>
    </div>
    <div class="hero-bottom">
      <div class="ctas">
        <a class="btn t" href="#work">See my work <span class="ar">↓</span></a>
        <a class="btn o" href="#contact">Let’s talk <span class="ar">→</span></a>
      </div>
      <span class="scroll mono">Scroll <b>↓</b></span>
    </div>
  </section>

  <div class="ribbon" aria-hidden="true"><div class="rail">{roles*4}</div></div>
  <div class="ribbon alt" aria-hidden="true"><div class="rail">{roles2*5}</div></div>

  <section class="say wrap" data-pairs='{json.dumps(pairs)}' aria-label="How I work">
    <span class="mono">✳ How I work</span>
    <p class="big">I turn <span class="hw sk" data-k="sk" tabindex="0">a rough sketch</span> into <span class="hw cp" data-k="cp" tabindex="0">a finished campaign</span>, with <span class="hw co" data-k="co" tabindex="0">creativity</span> as my copilot and strategy as the final word.</p>
    <p class="say-hint mono muted">Hover the highlighted words. Each time, a different real project.</p>
    <div class="peekimg" aria-hidden="true"><img alt=""><span></span></div>
    <div class="tools-pop" aria-hidden="true"><span class="tool ic" style="background:#F2E3A2;color:#0B0B0A" title="Ideas"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.6 10.8c.6.5 1 1.2 1 2V17h5.2v-1.2c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/></svg></span><span class="tool ic" style="background:#F4D3DD;color:#0B0B0A" title="Sketching"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20l4-1 11-11-3-3L5 16l-1 4z"/><path d="M14 6l3 3"/></svg></span><span class="tool ic" style="background:#CFE1EE;color:#0B0B0A" title="Craft"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 17l.7 1.8 1.8.7-1.8.7L19 22l-.7-1.8-1.8-.7 1.8-.7z"/></svg></span><span class="tool ic" style="background:#0B0B0A;color:#FFFFFF" title="Strategy"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r=".6" fill="currentColor"/></svg></span></div>
  </section>

  <section class="stage" id="work">
    <div class="sec wrap">
      <div class="sec-h">
        <h2><span class="lm"><span>Selected</span></span><span class="lm"><span>work<i class="n">08</i></span></span></h2>
        <div><p>Campaigns and digital work for global brands. On AI projects, hover to see the sketch they started from.</p></div>
      </div>
      <div class="grid">
{card(1,"proyectos/happy-talks.html","HD* · 2024","Happy Talks","Approved at first round and still live, two years on. UI in two weeks.",["Web","UI","Illustrator"],ht(1,"Happy Talks landing page on a laptop",pre))}
{card(2,"proyectos/no-vendas-humo.html","Philip Morris International","No Vendas Humo","Key visual for a smoke-free sales culture program.",["Key visual","Firefly","Photoshop"],ai("pmi-humo-final","Smoke letters reading No Vendas Humo",pre),"pmi-humo-ref",True)}
{card(3,"proyectos/arboterra.html","ArboTerra · Puebla, Mexico","ArboTerra es…","Campaign concept approved at first pitch, still in use 3 years later.",["Campaign","3D","Blender"],'<div class="ph"><img src="assets/img/arboterra/kv-aventura.jpg" alt="The Árbol Arcano floating over teal clouds" loading="lazy" decoding="async" draggable="false"></div>')}
{card(4,"proyectos/conexiones-magicas.html","Coca-Cola México · HD*","Conexiones Mágicas","An AI key visual in six layers, with the magic made by hand.",["Key visual","Firefly","Photoshop"],'<div class="ph"><img src="assets/img/coca/s7-final.jpg" alt="A hand catching a Coca-Cola bottle cap in red light" loading="lazy" decoding="async" draggable="false"></div>',"coca-ref",True)}
{card(5,"proyectos/campobet.html","CampoBet","CampoBet","+150 pieces a month, a rebrand and three AI pipelines I designed.",["Brand","Social","AI system"],'<div class="ph"><img src="assets/img/campobet/cover.jpg" alt="CampoBet trophy key visual" loading="lazy" decoding="async" draggable="false"></div>')}
{card(6,"","DiDi Food","Fuerza DiDi","Annual internal concept for business developers.",["Campaign","Firefly"],ai("didi-final","A hand holding a light saber handle",pre),"didi-ref",True,True)}
{card(7,"","Megagas","Amo Aquí","Service culture campaign for a Shell retail partner.",["Campaign","Firefly"],ai("megagas-final","A fuel hose shaped like a heart",pre),"megagas-ref",True,True)}
{card(8,"","Mars Wrigley","Snackable","Integration festival for 700+ associates.",["Event","Firefly"],ai("mars-final","Hands holding snacks under a blue sky",pre),"mars-ref",True,True)}
      </div>
      <div class="ix" aria-label="Project index">
        <div class="ix-h"><span>Index</span><span>Client</span><span>Discipline</span><span>Year</span></div>
          <a class="ix-row" href="proyectos/happy-talks.html" data-go data-zoom data-cursor="Open" data-img="assets/img/happy-talks/01.jpg"><span class="ix-n">01</span><span class="ix-name">Happy Talks</span><span class="ix-cl">HD*</span><span class="ix-tg">Web · UI</span><span class="ix-yr">2024</span></a>
          <a class="ix-row" href="proyectos/no-vendas-humo.html" data-go data-zoom data-cursor="Open" data-img="assets/img/ai/pmi-humo-final.jpg"><span class="ix-n">02</span><span class="ix-name">No Vendas Humo</span><span class="ix-cl">Philip Morris International</span><span class="ix-tg">Key visual · AI</span><span class="ix-yr">2024</span></a>
          <a class="ix-row" href="proyectos/arboterra.html" data-go data-zoom data-cursor="Open" data-img="assets/img/arboterra/kv-aventura.jpg"><span class="ix-n">03</span><span class="ix-name">ArboTerra es…</span><span class="ix-cl">ArboTerra</span><span class="ix-tg">Campaign · 3D</span><span class="ix-yr">2023</span></a>
          <a class="ix-row" href="proyectos/conexiones-magicas.html" data-go data-zoom data-cursor="Open" data-img="assets/img/coca/s7-final.jpg"><span class="ix-n">04</span><span class="ix-name">Conexiones Mágicas</span><span class="ix-cl">Coca-Cola México</span><span class="ix-tg">Key visual · AI</span><span class="ix-yr">—</span></a>
          <a class="ix-row" href="proyectos/campobet.html" data-go data-zoom data-cursor="Open" data-img="assets/img/campobet/cover.jpg"><span class="ix-n">05</span><span class="ix-name">CampoBet</span><span class="ix-cl">CampoBet</span><span class="ix-tg">Brand · AI system</span><span class="ix-yr">—</span></a>
          <div class="ix-row soon" data-cursor="Coming soon" data-img="assets/img/ai/didi-final.jpg"><span class="ix-n">06</span><span class="ix-name">Fuerza DiDi</span><span class="ix-cl">DiDi Food</span><span class="ix-tg">Campaign · AI</span><span class="ix-yr">Soon</span></div>
          <div class="ix-row soon" data-cursor="Coming soon" data-img="assets/img/ai/megagas-final.jpg"><span class="ix-n">07</span><span class="ix-name">Amo Aquí</span><span class="ix-cl">Megagas</span><span class="ix-tg">Campaign · AI</span><span class="ix-yr">Soon</span></div>
          <div class="ix-row soon" data-cursor="Coming soon" data-img="assets/img/ai/mars-final.jpg"><span class="ix-n">08</span><span class="ix-name">Snackable</span><span class="ix-cl">Mars Wrigley</span><span class="ix-tg">Event · AI</span><span class="ix-yr">Soon</span></div>
      </div>
    </div>
    <div class="lamp" aria-label="Lights off: move the cursor to discover final artworks">
      <div class="lamp-grid base" aria-hidden="true"><img src="assets/img/arboterra/kv-magia-noche.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/pmi-humo-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/coca-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/arboterra/kv-diversion.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/didi-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/megagas-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/sephora-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/arboterra/kv-aventura.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/mars-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/arcelor-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/cinepolis-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/pmi-copilot-final.jpg" alt="" loading="lazy" draggable="false"></div>
      <div class="lamp-grid lit" aria-hidden="true"><img src="assets/img/arboterra/kv-magia-noche.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/pmi-humo-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/coca-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/arboterra/kv-diversion.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/didi-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/megagas-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/sephora-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/arboterra/kv-aventura.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/mars-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/arcelor-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/cinepolis-final.jpg" alt="" loading="lazy" draggable="false"><img src="assets/img/ai/pmi-copilot-final.jpg" alt="" loading="lazy" draggable="false"></div>
      <p class="lamp-t"><b>Lights off.</b><span>Move around to find the finals.</span></p>
    </div>
    <div class="ix-float" aria-hidden="true"><img alt=""></div>
  </section>

  <section class="sec wrap" id="services">
    <div class="svc-wrap">
      <div class="svc-card" data-pop>
        <div>
          <span class="mono">✳ Services</span>
          <h2 style="margin-top:1rem"><span class="lm"><span>What</span></span><span class="lm"><span>I do</span></span></h2>
        </div>
        <p>From the first sketch to the rollout, for internal and external audiences.</p>
        <span class="now mono">Now: <b>AI art direction</b></span>
        <span class="svc-big" aria-hidden="true">01</span>
      </div>
      <ul class="svc">
        <li class="open" data-n="01" style="--c:var(--butter)"><button type="button"><span class="i">01</span><h3>AI art direction</h3><span class="pl" aria-hidden="true">+</span></button>
          <div class="body"><div><div class="inner"><p>Key visuals that start as a hand-painted reference and end as a polished campaign. Firefly, Midjourney and Stable Diffusion as copilots; Photoshop and judgment for the final word.</p><div class="tags"><span class="tag">Firefly</span><span class="tag">Midjourney</span><span class="tag">Stable Diffusion</span><span class="tag">Photoshop</span></div></div></div></div></li>
        <li data-n="02" style="--c:var(--pink)"><button type="button"><span class="i">02</span><h3>Internal campaigns</h3><span class="pl" aria-hidden="true">+</span></button>
          <div class="body"><div><div class="inner"><p>Concepts and materials for culture, training and change programs at Philip Morris, Coca-Cola, Nestlé, Sephora, Mars and more.</p><div class="tags"><span class="tag">Endomarketing</span><span class="tag">Concepts</span><span class="tag">Events</span><span class="tag">Large-format</span></div></div></div></div></li>
        <li data-n="03" style="--c:var(--sky)"><button type="button"><span class="i">03</span><h3>UX/UI &amp; web</h3><span class="pl" aria-hidden="true">+</span></button>
          <div class="body"><div><div class="inner"><p>Landing pages and digital experiences that tell the story and convert, like <a href="proyectos/happy-talks.html" data-go>Happy Talks</a>.</p><div class="tags"><span class="tag">Figma</span><span class="tag">Landing pages</span><span class="tag">HTML &amp; CSS</span></div></div></div></div></li>
        <li data-n="04" style="--c:var(--mint)"><button type="button"><span class="i">04</span><h3>3D &amp; motion</h3><span class="pl" aria-hidden="true">+</span></button>
          <div class="body"><div><div class="inner"><p>3D models, renders and 2D animation that give campaigns depth and movement.</p><div class="tags"><span class="tag">Blender</span><span class="tag">Cinema 4D</span><span class="tag">Octane</span><span class="tag">After Effects</span></div></div></div></div></li>
        <li data-n="05" style="--c:var(--tomato)"><button type="button"><span class="i">05</span><h3>Team &amp; brand management</h3><span class="pl" aria-hidden="true">+</span></button>
          <div class="body"><div><div class="inner"><p>Leading a design team for international iGaming brands in Mexico and Canada, aligned with Marketing, CRM, ASO and Performance to improve conversion and retention.</p><div class="tags"><span class="tag">Team lead</span><span class="tag">CRM</span><span class="tag">ASO</span><span class="tag">Performance</span></div></div></div></div></li>
      </ul>
    </div>
  </section>

  <section class="wrap" aria-label="Numbers and experience">
    <div class="numbers" data-pop>
      <h2>Ten years turning <em>creative ideas</em> into results.</h2>
      <div class="nums">
        <div><span class="odo" data-v="10+"></span><small>years designing, since 2016</small></div>
        <div><span class="odo" data-v="13"></span><small>AI-powered campaigns for global brands</small></div>
        <div><span class="odo" data-v="1,070"></span><small>employees reached by one AI-adoption program</small></div>
        <div><span class="odo" data-v="700+"></span><small>people at the Mars integration “Day Zero”</small></div>
      </div>
    </div>
    <ul class="xp" aria-label="Experience">
      <li><span class="yr"><b>2025 – Now</b></span><h3>Design Team Lead<small>Brainrocket</small></h3><p>Leading the design team for international iGaming brands in Mexico and Canada.</p></li>
      <li><span class="yr"><b>2023 – 2025</b></span><h3>Senior Designer<small>HD* Human Design Doing</small></h3><p>Endomarketing and culture campaigns for Philip Morris, Coca-Cola, Nestlé and more.</p></li>
      <li><span class="yr"><b>2020 – 2023</b></span><h3>Senior Designer<small>Happy Studio</small></h3><p>Concepts, 3D models and 2D animation for brand campaigns.</p></li>
      <li><span class="yr"><b>2018 – 2020</b></span><h3>Jr. Art Director<small>Volátil Agencia Creativa</small></h3><p>Creative concepts and art direction in a fast-paced agency.</p></li>
      <li><span class="yr"><b>2016 – 2018</b></span><h3>Designer<small>In Movisión</small></h3><p>Print and digital design, architectural photography and web layouts.</p></li>
    </ul>
  </section>

  <section class="play-band" id="be-creative" aria-label="Playground">
    <div class="play-top">
      <span class="file mono"><i></i>playground.fig — Artboard 1 · 100%</span>
      <div class="pens" role="group" aria-label="Pen color">
        <button type="button" class="mix" data-c="mix" aria-pressed="true" aria-label="All colors"></button>
        <button type="button" style="--c:#FF4B2B" data-c="#FF4B2B" aria-pressed="false" aria-label="Tomato"></button>
        <button type="button" style="--c:#FFB3D1" data-c="#FFB3D1" aria-pressed="false" aria-label="Pink"></button>
        <button type="button" style="--c:#FFD84D" data-c="#FFD84D" aria-pressed="false" aria-label="Butter"></button>
        <button type="button" style="--c:#9FD3FF" data-c="#9FD3FF" aria-pressed="false" aria-label="Sky"></button>
        <button type="button" style="--c:#141110;box-shadow:inset 0 0 0 2px #fff" data-c="#141110" aria-pressed="false" aria-label="Ink"></button>
      </div>
    </div>
    <div class="play">
      <canvas class="play-canvas" aria-hidden="true"></canvas>
      <i class="crop a"></i><i class="crop b"></i><i class="crop c"></i><i class="crop d"></i>
      <span class="play-sticker" aria-hidden="true">✳ Playground</span>
      <p class="play-title">Be creative,<br>be you</p>
      <p class="play-hint mono">Move your cursor to draw ✳</p>
      <span class="pen" aria-hidden="true"></span>
      <button class="reset" type="button"><span class="reset-ic" aria-hidden="true">↺</span><span>Blank page, fresh mind</span></button>
    </div>
  </section>
</main>
'''+contact()+scripts(pre)
open(os.path.join(R,'index.html'),'w').write(home)

def word(w,cls=''): return f'<span class="w {cls}">'+''.join(f'<span class="lt">{c}</span>' for c in w)+'</span>'

# ================= CASE: HAPPY TALKS =================
pre='../'
shots=[(3,'Hero','A 3D microphone breaks the word HAPPY.'),(4,'Talks','A typographic index, easy to scan.'),(5,'Story','Video and storytelling of a session.'),(6,'Speakers','Portraits over organic shapes.'),(7,'Social proof','Attendees and brands that trusted HDO.'),(8,'Events','Real photography makes the offer tangible.'),(9,'Topics','Stickers and type in collage.'),(10,'Request','A short form, the page’s main goal.')]
gal='\n'.join(f'        <figure class="shot">{ht(n,f"{t} section of the Happy Talks landing page",pre)}<figcaption><b>{i+1:02d} · {t}</b><span>{d}</span></figcaption></figure>' for i,(n,t,d) in enumerate(shots))
def fan(items):
    out=''
    for inner,lbl,cls in items: out+=f'<div class="card-img {cls}">{inner}<span class="lbl tag">{lbl}</span></div>'
    return f'<div class="fan" aria-hidden="true">{out}</div>'
def htimg(n,pre): return f'<img src="{pre}assets/img/happy-talks/{n:02d}.jpg" data-fallback="{B}{HT[n-1]}.jpg" alt="" draggable="false">'
def aiimg(n,pre): return f'<img src="{pre}assets/img/ai/{n}.jpg" alt="" draggable="false">'

def next_block(pre,title,href,img):
    return f'''  <a class="next" href="{href}" data-go data-zoom data-cursor="Next">
    <div class="wrap"><span class="mono">Next project</span><h2>{title} →</h2></div>
    <div class="peek">{img}</div>
    <div class="wrap"><div class="foot mono"><span>© 2026 Rodrigo López</span><span>{EMAIL}</span></div></div>
  </a>
'''

case=head('Happy Talks · Rodrigo López','Case study: UI design for Happy Talks, the conference platform of HD* Human Design Doing. Two weeks, desktop and mobile.',pre)+nav(pre,False)+f'''<main>
  <section class="wrap c-hero">
    <div class="c-head"><div class="c-l">
      <a class="back" href="{pre}#work" data-go>← All work</a>
      <div class="c-client"><span class="tag k">HD* Human Design Doing</span><span class="tag">Web · 2024</span></div>
      <h1 class="c-title" aria-label="Happy Talks"><span aria-hidden="true">{word("Happy")} {word("Talks","hlw")}</span></h1>
      </div><div class="c-r">
      <p class="c-lead">A landing page for HD*’s conference platform: an intangible offer, talks that change teams, turned into a page you can scroll, feel and request in one tap. My part was the UI.</p>
      <div class="tags c-tags"><span class="tag t">UI design</span><span class="tag p">Landing page</span><span class="tool t-ai" title="Illustrator">Ai</span><span class="tool t-ps" title="Photoshop">Ps</span></div>
      <dl class="facts"><div><dt class="mono">Role</dt><dd>UI design</dd></div><div><dt class="mono">Client</dt><dd>HD* (in-house)</dd></div><div><dt class="mono">Timeline</dt><dd>2 weeks · 2024</dd></div><div class="win"><dt class="mono">Result</dt><dd>Approved first round · still live</dd></div></dl>
      <a class="btn live" href="https://happy-talks.com/" target="_blank" rel="noopener">Visit the live site <span class="ar">↗</span></a>
    </div></div>
    <div class="browser" data-cursor="Scroll it">
      <div class="br-bar"><i></i><i></i><i></i><span>hd.company/happy-talks</span><em class="br-live">Auto-scrolling · hover to take over</em></div>
      <div class="br-body">
        <div class="br-view" data-lenis-prevent tabindex="0" aria-label="The full Happy Talks landing page, scrollable"><img src="{pre}assets/img/happy-talks/landing-full.jpg" alt="The full Happy Talks landing page, top to bottom" width="1401" height="9209" draggable="false"></div>
        <ol class="br-notes" aria-label="Design notes by section"><li data-y="0.0000"><b>01</b><span><strong>Hero</strong>The type breaks around a stock mic photo: the brand becomes the stage.</span></li><li data-y="0.0852"><b>02</b><span><strong>Talk families</strong>Three kinds of talks, numbered like a festival lineup.</span></li><li data-y="0.1705"><b>03</b><span><strong>Story</strong>Condensed neon type over dark photography: the backstage mood.</span></li><li data-y="0.3406"><b>04</b><span><strong>Speakers</strong>Portraits in soft capsules with color washes. Human, not corporate.</span></li><li data-y="0.4235"><b>05</b><span><strong>Proof</strong>HD*’s attendee count as a giant number, before any pitch.</span></li><li data-y="0.5133"><b>06</b><span><strong>Brands</strong>Client logos in a quiet grid: social proof without noise.</span></li><li data-y="0.6978"><b>07</b><span><strong>Events</strong>A tilted photo strip and a hand-drawn line add movement.</span></li><li data-y="0.7875"><b>08</b><span><strong>Topics</strong>Stickers carry the topics, so the system scales to any talk.</span></li><li data-y="0.8860"><b>09</b><span><strong>Request</strong>One goal: ask for a conference on WhatsApp.</span></li></ol>
      </div>
    </div>
  </section>

  <div class="wrap chapters">
    <aside class="toc" aria-label="Chapters">
      <ol><li><a href="#challenge">Challenge</a></li><li><a href="#system">The system</a></li><li><a href="#sections">Section by section</a></li><li><a href="#mobile">Mobile & result</a></li></ol>
      <div class="bar"><i></i></div>
    </aside>
    <div>
      <section class="chap" id="challenge">
        <span class="mono">01 · Challenge</span>
        <h2><span class="lm"><span>Make the intangible</span></span><span class="lm"><span>feel tangible</span></span></h2>
        <p class="lead">Happy Talks offers disruptive conferences that provoke reflection, build emotional connection and catalyze change inside organizations, far from traditional formats.</p>
        <div class="quotes" style="margin-top:.5rem">
          <div class="quote a"><b>Intangible</b><p>Communicate an intangible offer, conferences, in a tangible and appealing way.</p></div>
          <div class="quote c"><b>Crowded</b><p>Stand out in a competitive market for organizational development services.</p></div>
        </div>
        <p class="muted" style="margin-top:1.6rem">The goal: present the speakers and generate leads through an agile structure and storytelling that reflects the brand’s innovative spirit.</p>
      </section>

      <section class="chap" id="system">
        <span class="mono">02 · The system</span>
        <h2><span class="lm"><span>Less brochure,</span></span><span class="lm"><span>more backstage pass</span></span></h2>
        <p class="lead">Vibrant tones that carry energy and positivity. Illustration and photography that humanize the brand and connect with people. And stickers that carry the topics.</p>
        <div class="storm" aria-label="The landing’s topic stickers: drag and throw them" data-cursor="Grab one"><img class="storm-mark" src="{pre}assets/img/happy-talks/ht-white.png" alt="" draggable="false"><img class="storm-line" src="{pre}assets/img/happy-talks/squiggle.webp" alt="" draggable="false"><img class="stk-p img" src="{pre}assets/img/happy-talks/stickers/s02.webp" alt="" width="440" height="211" style="--w:220" draggable="false"><img class="stk-p img" src="{pre}assets/img/happy-talks/stickers/s03.webp" alt="" width="440" height="195" style="--w:220" draggable="false"><img class="stk-p img" src="{pre}assets/img/happy-talks/stickers/s04.webp" alt="" width="440" height="399" style="--w:220" draggable="false"><img class="stk-p img" src="{pre}assets/img/happy-talks/stickers/s05.webp" alt="" width="440" height="398" style="--w:220" draggable="false"><img class="stk-p img" src="{pre}assets/img/happy-talks/stickers/s06.webp" alt="" width="440" height="440" style="--w:220" draggable="false"><img class="stk-p img" src="{pre}assets/img/happy-talks/stickers/s07.webp" alt="" width="250" height="440" style="--w:125" draggable="false"><img class="stk-p img" src="{pre}assets/img/happy-talks/stickers/s08.webp" alt="" width="440" height="440" style="--w:220" draggable="false"><img class="stk-p img" src="{pre}assets/img/happy-talks/stickers/s09.webp" alt="" width="440" height="145" style="--w:220" draggable="false"><img class="stk-p img" src="{pre}assets/img/happy-talks/stickers/s10.webp" alt="" width="440" height="169" style="--w:220" draggable="false"><img class="stk-p img" src="{pre}assets/img/happy-talks/stickers/s11.webp" alt="" width="440" height="145" style="--w:220" draggable="false"><img class="stk-p img" src="{pre}assets/img/happy-talks/stickers/s12.webp" alt="" width="440" height="260" style="--w:220" draggable="false"><img class="stk-p img" src="{pre}assets/img/happy-talks/stickers/s13.webp" alt="" width="440" height="260" style="--w:220" draggable="false"><img class="stk-p img" src="{pre}assets/img/happy-talks/stickers/s14.webp" alt="" width="254" height="440" style="--w:127" draggable="false"><button type="button" class="storm-reset">Drop them again</button></div>
        <p class="muted mono" style="margin-top:.8rem">The landing’s real topic stickers. Go ahead, throw them.</p>
        <div class="swatches" aria-label="Happy Talks palette" style="margin-top:2rem">
          <div class="sw" style="background:#141218;color:#fff">Stage black</div>
          <div class="sw" style="background:#57E3C3;color:#141218">Mint</div>
          <div class="sw" style="background:#9B5CF6;color:#fff">Purple</div>
          <div class="sw" style="background:#F7E14B;color:#141218">Yellow</div>
          <div class="sw" style="background:#2D7FF9;color:#fff">Blue</div>
          <div class="sw" style="background:#FF6B9A;color:#141218">Pink</div>
        </div>
      </section>

      <section class="chap" id="sections">
        <span class="mono">03 · Section by section</span>
        <h2><span class="lm"><span>Nine sections,</span></span><span class="lm"><span>one goal</span></span></h2>
        <p class="lead">From first impact to the request. Drag to explore, click to open.</p>
        <div class="drag">
          <div class="drag-track" tabindex="0" aria-label="Landing page sections" data-cursor="Drag">
        <figure class="shot sec"><img src="{pre}assets/img/happy-talks/sec-hero.jpg" alt="Hero section of the Happy Talks landing page" loading="lazy" draggable="false"><figcaption><b>01 · Hero</b></figcaption></figure>
        <figure class="shot sec"><img src="{pre}assets/img/happy-talks/sec-index.jpg" alt="Talk families section of the Happy Talks landing page" loading="lazy" draggable="false"><figcaption><b>02 · Talk families</b></figcaption></figure>
        <figure class="shot sec"><img src="{pre}assets/img/happy-talks/sec-story.jpg" alt="Story section of the Happy Talks landing page" loading="lazy" draggable="false"><figcaption><b>03 · Story</b></figcaption></figure>
        <figure class="shot sec"><img src="{pre}assets/img/happy-talks/sec-speakers.jpg" alt="Speakers section of the Happy Talks landing page" loading="lazy" draggable="false"><figcaption><b>04 · Speakers</b></figcaption></figure>
        <figure class="shot sec"><img src="{pre}assets/img/happy-talks/sec-numbers.jpg" alt="Proof section of the Happy Talks landing page" loading="lazy" draggable="false"><figcaption><b>05 · Proof</b></figcaption></figure>
        <figure class="shot sec"><img src="{pre}assets/img/happy-talks/sec-brands.jpg" alt="Brands section of the Happy Talks landing page" loading="lazy" draggable="false"><figcaption><b>06 · Brands</b></figcaption></figure>
        <figure class="shot sec"><img src="{pre}assets/img/happy-talks/sec-conferences.jpg" alt="Events section of the Happy Talks landing page" loading="lazy" draggable="false"><figcaption><b>07 · Events</b></figcaption></figure>
        <figure class="shot sec"><img src="{pre}assets/img/happy-talks/sec-conversations.jpg" alt="Topics section of the Happy Talks landing page" loading="lazy" draggable="false"><figcaption><b>08 · Topics</b></figcaption></figure>
        <figure class="shot sec"><img src="{pre}assets/img/happy-talks/sec-cta.jpg" alt="Request section of the Happy Talks landing page" loading="lazy" draggable="false"><figcaption><b>09 · Request</b></figcaption></figure>
          </div>
          <div class="drag-ui"><div class="bar"><i></i></div><div class="ar"><button type="button" data-prev aria-label="Previous">←</button><button type="button" data-next aria-label="Next">→</button></div></div>
        </div>
      </section>

      <section class="chap" id="mobile">
        <span class="mono">04 · Mobile</span>
        <h2><span class="lm"><span>Built for</span></span><span class="lm"><span>the thumb</span></span></h2>
        <p class="lead">The same energy in a single column, with the request always one tap away.</p>
        <div class="kv-grid">
          <figure><img src="{pre}assets/img/happy-talks/mock-1.jpg" alt="Happy Talks on a phone: story and speakers sections" loading="lazy" draggable="false"><figcaption class="tag">Story & speakers</figcaption></figure>
          <figure><img src="{pre}assets/img/happy-talks/mock-2.jpg" alt="Happy Talks on a phone: events, topics and request" loading="lazy" draggable="false"><figcaption class="tag">Topics & request</figcaption></figure>
        </div>
        <div class="quotes three" style="margin-top:clamp(2.4rem,5vw,3.4rem)">
          <div class="quote b"><b>1st round</b><p>The design was approved at the first presentation.</p></div>
          <div class="quote c"><b>Live</b><p>Still online at happy-talks.com, two years after launch.</p></div>
          <div class="quote a"><b>2 weeks</b><p>From the brief to the full desktop and mobile UI.</p></div>
        </div>
        <div class="micdrop" data-cursor="Move the mic" aria-label="Approved at the first round. Mic drop.">
          <p class="md-t">Approved at the first round.<br><b aria-hidden="true"><span class="ml">M</span><span class="ml">i</span><span class="ml">c</span><span class="ml">&nbsp;</span><span class="ml">d</span><span class="ml">r</span><span class="ml">o</span><span class="ml">p</span><span class="ml">.</span></b></p>
          <div class="md-mic-wrap"><span class="md-wave" aria-hidden="true"><i></i><i></i><i></i></span><img class="md-mic" src="{pre}assets/img/happy-talks/mic.webp" alt="" draggable="false"></div>
        </div>
      </section>
    </div>
  </div>
'''+next_block(pre,'No Vendas Humo','no-vendas-humo.html',aiimg('pmi-humo-final',pre))+'''</main>
'''+scripts(pre)
open(os.path.join(R,'proyectos','happy-talks.html'),'w').write(case)

# ================= CASE: NO VENDAS HUMO (AI process template) =================
case2=head('No Vendas Humo · Rodrigo López','Case study: an AI-powered key visual for Philip Morris International, from a hand-painted reference to the final campaign.',pre)+nav(pre,False)+f'''<main>
  <section class="wrap c-hero">
    <div class="c-head"><div class="c-l">
      <a class="back" href="{pre}#work" data-go>← All work</a>
      <div class="c-client"><span class="tag k">Philip Morris International</span><span class="ai">AI process</span></div>
      <h1 class="c-title" aria-label="No vendas humo"><span aria-hidden="true">{word("No")} {word("vendas")} {word("humo","hlw")}</span></h1>
      </div><div class="c-r">
      <p class="c-lead">A key visual for a sales-culture program during PMI’s shift to a smoke-free company. The idea, “don’t sell smoke”, was drawn by hand first and finished with AI.</p>
      <div class="tags c-tags"><span class="tag t">Key visual</span><span class="tag p">Internal campaign</span><span class="tool t-ff" title="Adobe Firefly">Ff</span><span class="tool t-ps" title="Photoshop">Ps</span></div>
      <dl class="facts"><div><dt class="mono">Role</dt><dd>Concept, art direction, AI imagery</dd></div><div><dt class="mono">Agency</dt><dd>HD* Human Design Doing</dd></div><div><dt class="mono">Program</dt><dd>2.5-day training</dd></div></dl>
    </div></div>
    <div class="c-cover">{aiimg('pmi-humo-final',pre).replace('alt=""','alt="Final key visual: letters made of smoke reading No vendas humo"')}<figure class="c-sticker">{aiimg('pmi-humo-ref',pre)}<figcaption class="mono">It started as this sketch</figcaption></figure></div>
  </section>

  <div class="wrap chapters">
    <aside class="toc" aria-label="Chapters">
      <ol><li><a href="#challenge">Challenge</a></li><li><a href="#idea">Idea</a></li><li><a href="#process">AI process</a></li><li><a href="#compare">Before / after</a></li></ol>
      <div class="bar"><i></i></div>
    </aside>
    <div>
      <section class="chap" id="challenge">
        <span class="mono">01 · Challenge</span>
        <h2><span class="lm"><span>Back to the</span></span><span class="lm"><span>fundamentals</span></span></h2>
        <p class="lead">PMI is moving towards a smoke-free, multi-category business. Its sales force had lost focus on core operational tasks, so the program had to rebuild ownership and execution at the point of sale.</p>
        <div class="quotes" style="margin-top:2rem">
          <div class="quote c"><b>2.5</b><p>days of intensive training, plus post-training follow-up.</p></div>
          <div class="quote b"><b>1</b><p>shared vision for every collaborator: the “Perfect PMI Store”.</p></div>
        </div>
      </section>

      <section class="chap" id="idea">
        <span class="mono">02 · Idea</span>
        <h2><span class="lm"><span>Don’t sell smoke</span></span></h2>
        <p class="lead">In Spanish, “vender humo” means making empty promises. For a company leaving smoke behind, the phrase becomes a double message: deliver real results, and let the smoke go.</p>
        <p class="pull">Letters made of smoke, <em>about to disappear</em>.</p>
      </section>

      <section class="chap" id="process">
        <span class="mono">03 · AI process</span>
        <h2><span class="lm"><span>From a brush stroke</span></span><span class="lm"><span>to a campaign</span></span></h2>
        <p class="lead">I painted the lettering by hand to control the composition, then used it as a structure reference in Firefly. The red box shows how I scan each round to pick the keeper.</p>
        <div class="flow">
          <div class="stage-card"><div class="hd"><b>Reference</b><span class="tool t-ps">Ps</span></div><div class="im" style="background:#fff">{aiimg('pmi-humo-ref',pre).replace('alt=""','alt="Hand-painted green lettering reading No Vendas Humo"')}</div><p class="note">Hand-painted in Photoshop to lock the layout.</p></div>
          <div class="stage-card"><div class="hd"><b>Iterations</b><span class="tool t-ff">Ff</span></div>
            <div class="strip" data-pick="2" data-n="6">{aiimg('pmi-humo-iter1',pre).replace('alt=""','alt="First six Firefly results"')}</div>
            <div class="strip" data-pick="3" data-n="6">{aiimg('pmi-humo-iter2',pre).replace('alt=""','alt="Six results after adjusting the prompt"')}</div>
            <p class="note">First results, then a second round after adjusting prompt and settings.</p></div>
          <div class="stage-card final"><div class="hd"><b>Final</b><span class="tool t-ps">Ps</span></div><div class="im">{aiimg('pmi-humo-final',pre).replace('alt=""','alt="Final key visual with smoke letters"')}</div><p class="note">Retouched and composed with the brand.</p></div>
        </div>
        <div class="prompt" aria-label="Prompt">
          <div class="bar"><i></i><i></i><i></i><span>Firefly · prompt</span></div>
          <div class="typed">smoke letters floating in a dark blue space, soft volumetric light, photographic, the letters follow the reference shape</div>
          <div class="meta"><span>structure ref: 100%</span><span>content: photo</span><span>16:9</span><span>12 results reviewed</span></div>
        </div>
        <p class="muted mono" style="margin-top:.8rem">Prompt reconstructed from the project. Exact settings to be confirmed.</p>
      </section>

      <section class="chap" id="compare">
        <span class="mono">04 · Before / after</span>
        <h2><span class="lm"><span>Same idea,</span></span><span class="lm"><span>two moments</span></span></h2>
        <p class="lead">Drag the handle to compare the hand-painted reference with the final key visual.</p>
        <div class="compare" data-cursor="Drag">
          <div class="before">{aiimg('pmi-humo-ref',pre).replace('alt=""','alt="Reference"')}</div>
          <div class="after" style="position:absolute;inset:0">{aiimg('pmi-humo-final',pre).replace('alt=""','alt="Final"')}</div>
          <span class="l a tag k">Sketch</span><span class="l b tag b">Final</span>
          <span class="handle" aria-hidden="true"></span>
          <input type="range" id="cmp-humo" min="0" max="100" value="50" aria-label="Compare sketch and final">
        </div>
      </section>

    </div>
  </div>
'''+next_block(pre,'ArboTerra es…','arboterra.html','<img src="../assets/img/arboterra/kv-aventura.jpg" alt="" draggable="false">')+'''</main>
'''+scripts(pre)
open(os.path.join(R,'proyectos','no-vendas-humo.html'),'w').write(case2)

# ================= CASE: ARBOTERRA (campaign system) =================
def at(name,alt='',cls='',lazy=True):
    ext='webp' if name.startswith(('tree','flamingo')) else 'jpg'
    from PIL import Image as _I
    w,h=_I.open(os.path.join(R,'assets/img/arboterra',f'{name}.{ext}')).size
    return f'<img src="{pre}assets/img/arboterra/{name}.{ext}" alt="{alt}" class="{cls}" width="{w}" height="{h}" draggable="false"{" loading=\"lazy\"" if lazy else ""}>'
LOCK={'aventura':(1404,133),'magia':(1236,131),'diversion':(1426,171)}
moods=[('aventura','Aventura','aventura','#195554'),('noche','Magia · night','magia','#FFFFFF'),('dia','Magia · day','magia','#195554'),('diversion','Diversión','diversion','#195554')]
layers=''.join(f'<div class="m-layer{" on" if i==0 else ""}" data-m="{m}">{at("bg-"+m,"","bg",i>0)}<div class="m-locks"><img class="lock{" on" if i==0 else ""}" data-m="{m}" src="{pre}assets/img/arboterra/lock-{w}{"" if c=="#FFFFFF" else "-teal"}.png" alt="ArboTerra es {w}" style="--h:{LOCK[w][1]/133:.3f}" draggable="false"></div>{at("tree-"+m,"","tree",i>0)}</div>' for i,(m,l,w,c) in enumerate(moods))
tabs=''.join(f'<button type="button" data-m="{m}" aria-pressed="{"true" if i==0 else "false"}">{l}</button>' for i,(m,l,w,c) in enumerate(moods))
promos=[('promo-1','Alegría','Photo promos put real kids at the center.'),('promo-2','Celebración','Birthday packages, same type system.'),('promo-3','Celebración','A second take for the same offer.'),('promo-4','Aventura','Park photography with the brand lockup.'),('promo-5','Aventura','Greens and depth, no tree needed.'),('promo-6','Aventura','The path into the park.'),('app-story','Story','The tree adapted to a vertical story.'),('app-vertical','Vertical','A narrow format for print and screens.')]
pgal='\n'.join(f'        <figure class="shot pt">{at(n,f"ArboTerra {t} piece")}<figcaption><b>{i+1:02d} · {t}</b><span>{d}</span></figcaption></figure>' for i,(n,t,d) in enumerate(promos))
ig=[('ig-1','Oct 21, 2026','The Árbol Arcano, now under a glass dome for World Energy Saving Day.'),('ig-2','Sep 28, 2026','The block-cut lettering, reused for the park’s kids podcast.'),('ig-3','Sep 3, 2026','Same podcast, same type system, new scene.')]
igal='\n'.join(f'        <figure class="shot ig">{at(n,f"ArboTerra Instagram post from {d}")}<figcaption><b>@arboterra · {d}</b><span>{t}</span></figcaption></figure>' for n,d,t in ig)
steps=[('Background','Photo, blurred and color-graded to match the word.'),('Árbol Arcano','The 3D tree: a floating island with a waterfall and a balloon.'),('Supporting elements','Birds from the park, bubbles and light.'),('Final','Lockup and call to action: ¡Ven y explora!')]
bsteps=''.join(f'<button type="button" data-i="{i}" aria-pressed="{"true" if i==0 else "false"}"><b>{i+1:02d}</b>{t}</button>' for i,(t,d) in enumerate(steps))
bimgs=''.join(f'<figure class="b-img{" on" if i==0 else ""}">{at(f"build-{i+1}",f"Construction step {i+1}: {t}")}</figure>' for i,(t,d) in enumerate(steps))
bnotes=''.join(f'<p class="b-note{" on" if i==0 else ""}">{d}</p>' for i,(t,d) in enumerate(steps))

case3=head('ArboTerra es… · Rodrigo López','Case study: an open-ended campaign system for ArboTerra, a nature park in Puebla, Mexico. Concept, art direction and 3D.',pre)+nav(pre,False)+f'''<main>
  <section class="wrap c-hero arbt">
    <div class="c-head"><div class="c-l">
      <a class="back" href="{pre}#work" data-go>← All work</a>
      <div class="c-client"><span class="tag k">ArboTerra</span><span class="tag">Campaign · 2023</span></div>
      <h1 class="c-title" aria-label="ArboTerra es…"><span aria-hidden="true">{word("ArboTerra")} {word("es…","hlw")}</span></h1>
      </div><div class="c-r">
      <p class="c-lead">A park nobody could define got a campaign that never finishes the sentence. My part was the concept: the idea, the four key visuals and the AdBook. The client’s in-house team produced everything after, and still uses it three years later.</p>
      <div class="tags c-tags"><span class="tag t">Concept</span><span class="tag p">Art direction</span><span class="tag b">3D</span><span class="tool t-bl" title="Blender">Bl</span><span class="tool t-ps" title="Photoshop">Ps</span></div>
      <dl class="facts"><div><dt class="mono">Role</dt><dd>Concept, key visuals, 3D</dd></div><div><dt class="mono">Scope</dt><dd>Concept only · execution in-house</dd></div><div><dt class="mono">Agency</dt><dd>Happy Studio</dd></div><div><dt class="mono">Timeline</dt><dd>2–3 months</dd></div><div class="win"><dt class="mono">Result</dt><dd>Still in use, 3 years on</dd></div></dl>
    </div></div>
    <div class="moods" data-cursor="Change mood">
      <div class="m-stage">{layers}</div>
      <div class="m-tabs" role="group" aria-label="Choose a mood">{tabs}</div>
    </div>
  </section>

  <div class="wrap chapters">
    <aside class="toc" aria-label="Chapters">
      <ol><li><a href="#challenge">Challenge</a></li><li><a href="#idea">Idea</a></li><li><a href="#world">The world</a></li><li><a href="#system">The system</a></li><li><a href="#results">Results</a></li></ol>
      <div class="bar"><i></i></div>
    </aside>
    <div>
      <section class="chap" id="challenge">
        <span class="mono">01 · Challenge</span>
        <h2><span class="lm"><span>A park nobody</span></span><span class="lm"><span>could define</span></span></h2>
        <p class="lead">ArboTerra, a nature park in Puebla, had a problem: many families didn’t know what it was.</p>
        <div class="quotes" style="margin-top:2rem">
          <div class="quote a"><b>Families</b><p>Parents and kids, with very different reasons to visit.</p></div>
          <div class="quote c"><b>Print + digital</b><p>Billboards and a steady stream of social content.</p></div>
        </div>
      </section>

      <section class="chap" id="idea">
        <span class="mono">02 · Idea</span>
        <h2><span class="lm"><span>Don’t define it.</span></span><span class="lm"><span>Let it be everything.</span></span></h2>
        <p class="lead">Leave the sentence open: <b>ArboTerra es…</b> adventure or magic for kids, learning for parents.</p>
        <h3 class="sub">The road not taken</h3>
        <p class="muted">Mascots on white looked like any park. The floating tree could hold every ending. Drag to compare.</p>
        <div class="compare" data-cursor="Drag">
          <div class="before">{at('route-white','Discarded route: mascots and 3D letters reading Arboterra es Aventura on white')}</div>
          <div class="after" style="position:absolute;inset:0">{at('kv-aventura','Chosen route: the Árbol Arcano floating over teal clouds')}</div>
          <span class="l a tag k">Discarded route</span><span class="l b tag b">Chosen route</span>
          <span class="handle" aria-hidden="true"></span>
          <input type="range" min="0" max="100" value="50" aria-label="Compare the discarded route and the chosen one">
        </div>
      </section>

      <section class="chap" id="world">
        <span class="mono">03 · The world</span>
        <h2><span class="lm"><span>Building the</span></span><span class="lm"><span>Árbol Arcano</span></span></h2>
        <p class="lead">One hero element, modeled in Blender and composed in Photoshop. The hardest part of the project.</p>
        <div class="build">
          <div class="b-stage">{bimgs}</div>
          <div class="b-side"><div class="b-steps" role="group" aria-label="Construction layers">{bsteps}</div><div class="b-notes">{bnotes}</div><p class="mono muted b-cap">From the AdBook: the layer in color is the one being added.</p></div>
        </div>
        <h3 class="sub">Same tree, four moods</h3>
        <div class="kv-grid">
          <figure>{at('kv-aventura','Final key visual: ArboTerra es Aventura')}<figcaption class="tag">Aventura</figcaption></figure>
          <figure>{at('kv-magia-noche','Final key visual: ArboTerra es Magia, night')}<figcaption class="tag">Magia · night</figcaption></figure>
          <figure>{at('kv-magia-dia','Final key visual: ArboTerra es Magia, day')}<figcaption class="tag">Magia · day</figcaption></figure>
          <figure>{at('kv-diversion','Final key visual: ArboTerra es Diversión')}<figcaption class="tag">Diversión</figcaption></figure>
        </div>
        <h3 class="sub">Different moods, built from photos</h3>
        <p class="muted">Each word gets its own background: a real photo, blurred, then color-graded to match the feeling. Hover to open each one.</p>
        <div class="swatches moods-sw" aria-label="The four backgrounds">
          <div class="sw" style="background-image:url({pre}assets/img/arboterra/bg-aventura.jpg)"><span>Aventura</span></div>
          <div class="sw" style="background-image:url({pre}assets/img/arboterra/bg-noche.jpg)"><span>Magia · night</span></div>
          <div class="sw" style="background-image:url({pre}assets/img/arboterra/bg-dia.jpg)"><span>Magia · day</span></div>
          <div class="sw" style="background-image:url({pre}assets/img/arboterra/bg-diversion.jpg)"><span>Diversión</span></div>
        </div>
      </section>

      <section class="chap" id="system">
        <span class="mono">04 · The system</span>
        <h2><span class="lm"><span>A toolkit,</span></span><span class="lm"><span>not a poster</span></span></h2>
        <p class="lead">The client’s team ran the execution, so I delivered a 35-page AdBook built to be reused.</p>
        <div class="concept">
          <div><h3>Sorvette for the big words</h3><p>Rounded block letters with small cut-in details, so every word feels hand-built.</p></div>
          <div><h3>Knewave for the call to action</h3><p>A loose brush script that shouts ¡Ven y explora! without competing with the title.</p></div>
        </div>
        <div class="drag" style="margin-top:2.4rem">
          <div class="drag-track" tabindex="0" aria-label="Campaign pieces" data-cursor="Drag">
{pgal}
          </div>
          <div class="drag-ui"><div class="bar"><i></i></div><div class="ar"><button type="button" data-prev aria-label="Previous">←</button><button type="button" data-next aria-label="Next">→</button></div></div>
        </div>
      </section>

      <section class="chap" id="results">
        <span class="mono">05 · Results</span>
        <h2><span class="lm"><span>Three years later,</span></span><span class="lm"><span>still ArboTerra es…</span></span></h2>
        <div class="quotes three">
          <div class="quote b"><b>1st round</b><p>Concept approved at the first presentation.</p></div>
          <div class="quote c"><b>In-house</b><p>The AdBook let the client’s team produce billboards and social on their own.</p></div>
          <div class="quote a"><b>2023 → 2026</b><p>The tree, the lettering and #ArboTerraesMagia are still on the park’s Instagram, now produced by their own team.</p></div>
        </div>
        <p class="muted" style="margin-top:2.4rem">The client wanted something timeless. These recent posts are made by ArboTerra’s in-house team, not by me. They’re here as proof the concept is still alive.</p>
        <div class="drag" style="margin-top:1.6rem">
          <div class="drag-track" tabindex="0" aria-label="Recent ArboTerra Instagram posts" data-cursor="Drag">
{igal}
          </div>
          <div class="drag-ui"><div class="bar"><i></i></div><div class="ar"><button type="button" data-prev aria-label="Previous">←</button><button type="button" data-next aria-label="Next">→</button></div></div>
        </div>
        <div class="learn"><span class="mono">What I’d do differently</span><p>Give 3D the time it needs. A tree this complex in a few weeks was a stretch; today I’d prototype the scenes with AI before committing to the full model.</p></div>
      </section>
    </div>
  </div>
'''+next_block(pre,'Conexiones Mágicas','conexiones-magicas.html','<img src="../assets/img/coca/s7-final.jpg" alt="" draggable="false">')+'''</main>
'''+scripts(pre)
open(os.path.join(R,'proyectos','arboterra.html'),'w').write(case3)
# ================= CASE: CONEXIONES MÁGICAS (short AI case) =================
def cc(n,alt='',cls=''):
    return f'<img src="{pre}assets/img/coca/{n}" alt="{alt}" class="{cls}" draggable="false" loading="lazy">'
steps=[('s1-reference.jpg','Photo reference','Hand','A reference photo of a hand, cut out and placed on red to lock the gesture.'),
 ('s2-structure.jpg','Structure reference','Hand','The gesture flattened into a silhouette, so Firefly keeps the pose and invents the light.'),
 ('s3-firefly.jpg','Firefly result','AI','Godrays, dust and backlight. The output didn’t fill the canvas: see the red band on top.'),
 ('s4-extend.jpg','Generative Fill','AI','The missing sky is extended and the fingers are cleaned up.'),
 ('s5-grade.jpg','Color grade','Hand','Warm light pushed into Coca-Cola red with hue and curve adjustments.'),
 ('s6-cap.jpg','The cap','Hand','A real bottle-cap photo, rebuilt in 12 layers to sit in the light.'),
 ('s7-final.jpg','Final key visual','Hand','Title in linear burn, tagline and logo.')]
timgs=''.join(f'<figure class="t-img{" on" if i==0 else ""}">{cc(f,f"Step {i+1}: {t}")}</figure>' for i,(f,t,w,d) in enumerate(steps))
tlist=''.join(f'<li data-i="{i}"{" class=on" if i==0 else ""}><b>{i+1:02d}</b><span>{t}</span><em class="{"ai-b" if w=="AI" else "hand-b"}">{w}</em></li>' for i,(f,t,w,d) in enumerate(steps))
tnotes=''.join(f'<p class="t-note{" on" if i==0 else ""}">{d}</p>' for i,(f,t,w,d) in enumerate(steps))
case4=head('Conexiones Mágicas · Rodrigo López','Case study: an AI-assisted key visual for a Coca-Cola México team experience, built in layers from a hand silhouette.',pre)+nav(pre,False)+f'''<main>
  <section class="wrap c-hero">
    <div class="c-head"><div class="c-l">
      <a class="back" href="{pre}#work" data-go>← All work</a>
      <div class="c-client"><span class="tag k">Coca-Cola México</span><span class="ai">AI process</span></div>
      <h1 class="c-title" aria-label="Conexiones mágicas"><span aria-hidden="true">{word("Conexiones")} {word("mágicas","hlw")}</span></h1>
      </div><div class="c-r">
      <p class="c-lead">A team-building proposal for a Coca-Cola concentrate plant, built on one idea: the magic isn’t only in the secret formula, it’s in the people. My part was the visual concept.</p>
      <div class="tags c-tags"><span class="tag t">Key visual</span><span class="tag p">Internal culture</span><span class="tool t-ff" title="Adobe Firefly">Ff</span><span class="tool t-ps" title="Photoshop">Ps</span></div>
      <dl class="facts"><div><dt class="mono">Role</dt><dd>Visual concept, AI imagery</dd></div><div><dt class="mono">Agency</dt><dd>HD* Human Design Doing</dd></div><div><dt class="mono">Designed for</dt><dd>75-person warehouse team</dd></div><div><dt class="mono">Format</dt><dd>8-hour on-site experience (proposal)</dd></div></dl>
    </div></div>
    <div class="c-cover pop-cover">{cc('s7-final.jpg','Final key visual: a hand about to catch a Coca-Cola bottle cap in red light, with the title Conexiones mágicas')}
      <button class="pop" type="button" aria-label="Pop the cap to reveal the key visual" data-cursor="Pop it">
        <img class="pop-cap" src="{pre}assets/img/coca/cap.png" alt="" draggable="false">
        <span class="pop-t">Pop the cap</span><span class="pop-h">Click or flick it away</span>
      </button>
    </div>
  </section>

  <div class="wrap chapters">
    <aside class="toc" aria-label="Chapters">
      <ol><li><a href="#challenge">Challenge</a></li><li><a href="#idea">Idea</a></li><li><a href="#trick">Behind the trick</a></li></ol>
      <div class="bar"><i></i></div>
    </aside>
    <div>
      <section class="chap" id="challenge">
        <span class="mono">01 · Challenge</span>
        <h2><span class="lm"><span>“We’ve lost the feeling</span></span><span class="lm"><span>of being a winning team”</span></span></h2>
        <p class="lead">A warehouse team at Coca-Cola’s concentrate plant needed to break silos, recover its champion spirit and open up to different ways of working.</p>
        <div class="quotes" style="margin-top:.5rem">
          <div class="quote a"><b>75</b><p>people in the warehouse team the experience was designed for.</p></div>
          <div class="quote c"><b>8 h</b><p>of on-site, playful workshops proposed by HD*.</p></div>
        </div>
      </section>

      <section class="chap" id="idea">
        <span class="mono">02 · Idea</span>
        <h2><span class="lm"><span>The magic is</span></span><span class="lm"><span>in the people</span></span></h2>
        <p class="lead">The pitch opens like a magic trick. The reveal: what makes Coca-Cola special isn’t only the formula, it’s the team. One gesture sums it up: a hand about to catch a popped cap.</p>
        <h3 class="sub">Where it started</h3>
        <div class="refs">
          <figure>{cc('../ai/coca-photo1.jpg','Reference photo: hands in backlight')}</figure>
          <figure>{cc('../ai/coca-photo2.jpg','Reference photo: a hand reaching into light')}</figure>
          <figure>{cc('../ai/coca-photo3.jpg','Reference photo: the hand pose that was chosen')}<figcaption class="tag">The pose I kept</figcaption></figure>
        </div>
      </section>

      <section class="chap" id="trick">
        <span class="mono">03 · Behind the trick</span>
        <h2><span class="lm"><span>Seven steps,</span></span><span class="lm"><span>straight from the PSD</span></span></h2>
        <p class="lead">Drag through the actual layers of the file. Labels show what the AI did and what I did by hand.</p>
        <div class="trick" data-n="{len(steps)}">
          <div class="t-stage">{timgs}</div>
          <div class="t-side">
            <ol class="t-list">{tlist}</ol>
            <div class="t-notes">{tnotes}</div>
            <input class="t-range" type="range" min="0" max="{len(steps)-1}" value="0" step="1" aria-label="Scrub through the layers">
          </div>
        </div>
        <div class="prompt" aria-label="Prompt">
          <div class="bar"><i></i><i></i><i></i><span>Firefly · prompt</span></div>
          <div class="typed">hand lighted by godrays red dark background</div>
          <div class="meta"><span>structure ref: silhouette</span><span>16:9</span><span>real prompt, kept in the PSD layer name</span></div>
        </div>
      </section>

    </div>
  </div>
'''+next_block(pre,'CampoBet','campobet.html','<img src="../assets/img/campobet/cover.jpg" alt="" draggable="false">')+'''</main>
'''+scripts(pre)
open(os.path.join(R,'proyectos','conexiones-magicas.html'),'w').write(case4)

# ================= CASE: CAMPOBET =================
# Part one: the work, very visual. Part two: the automation (anatomy, reflow, pipelines).
pre='../'
from PIL import Image as _PI
def phb(label,ratio='4/5',c='a',extra=''):
    return f'<div class="phb {c}" style="aspect-ratio:{ratio}"{extra}><span>{label}</span></div>'
CC=['a','b','c','d','e']
def cbs(n):
    return _PI.open(os.path.join(R,'assets','img','campobet',n)).size
def cbi(n,alt='',cls='',lazy=True):
    w,h=cbs(n);c=f' class="{cls}"' if cls else ''
    return f'<img{c} src="{pre}assets/img/campobet/{n}" width="{w}" height="{h}" alt="{alt}"{" loading=\"lazy\"" if lazy else ""} decoding="async" draggable="false">'
def ar(n): w,h=cbs(n);return f'{w}/{h}'
FEAT=['hero-1.jpg','hero-4.jpg','hero-3.jpg','hero-5.jpg','hero-6.jpg','hero-2.jpg','hero-7.jpg']
h184=''.join('<i></i>' for _ in range(184))
hfeat=''.join(f'<div class="hf" style="--i:{i}">{cbi(f,"CampoBet piece",lazy=False)}</div>' for i,f in enumerate(FEAT))
LT=[('Slots',1),('Football',2),('Basketball',3),('American football',4)]
lenti=''.join(f'<div class="lt-p" style="aspect-ratio:{ar(f"rb-new-{k}.jpg")}"><div class="lt-a">{cbi(f"rb-old-{k}.jpg",f"{n} piece before the rebrand")}</div><div class="lt-b">{cbi(f"rb-new-{k}.jpg",f"{n} piece after the rebrand")}</div><i class="lt-sheen"></i></div>' for n,k in LT)
def col(k):
    t=''.join(cbi(f'soc-{k*6+j+1:02d}.jpg','CampoBet social post') for j in range(6))
    return f'<div class="col{" up" if k%2 else ""}"><div class="col-rail">{t}{t}</div></div>'
cols=''.join(col(k) for k in range(4))
CARS=[('Weekly fixtures',6),('Big leagues',5),('Match of the day',6)]
cars=''.join(f'<figure class="car" data-n="{n}"><div class="car-v"><div class="car-t">'+''.join(cbi(f'car{c+1}-{i+1}.jpg',f'{t}, slide {i+1}') for i in range(n))+f'</div><button type="button" class="car-p" aria-label="Previous slide">‹</button><button type="button" class="car-n" aria-label="Next slide">›</button></div><div class="car-dots">'+''.join(f'<button type="button" aria-label="Slide {i+1}"></button>' for i in range(n))+f'</div><figcaption class="mono">{t} · {n} slides</figcaption></figure>' for c,(t,n) in enumerate(CARS))
wc=''.join(f'<button type="button" class="pl" style="--i:{i}" aria-label="World Cup piece {i+1}">{cbi(f"wc-{i+1:02d}.jpg","World Cup piece",lazy=False)}<span class="pl-n">{i+1}</span></button>' for i in range(11))
wcb=''.join(f'<figure>{cbi(f"wcb-{i+1}.webp","Megashoot promo block")}</figure>' for i in range(3))
keys=''.join(f'<figure class="key">{cbi(f"key-{i+1}.jpg","Key art reused across several pieces")}</figure>' for i in [2,4,3,0,5,1])
CRMH=[503,503,479,500,503,498]
def crl(n,cls,st,alt=''):
    return f'<div class="cl {cls}"><img src="{pre}assets/img/campobet/crm/{n}" style="{st}" alt="{alt}" loading="lazy" draggable="false"></div>'
crm=''.join(f'''<figure class="cr" tabindex="0" aria-label="CRM banner {i+1}, built in layers">
  <div class="cr-in">{crl(f"c{i+1}-main.jpg","l0 msk",f"left:0;top:0;width:100%;height:{h/5.2:.2f}%","Generated photo")}{crl("glow.webp","l1 msk","left:58.33%;top:0;width:41.67%")}{crl(f"c{i+1}-subject.webp","l2 msk",f"left:0;top:0;width:100%;height:{h/5.2:.2f}%")}{crl("grad.webp","l3 msk","left:0;top:20.67%;width:100%")}{crl(f"c{i+1}-copy.webp","l4","left:0;top:0;width:100%;height:100%","Copy and frame")}{crl("logo.webp","l5","left:36.5%;top:3.85%;width:27%")}{crl(f"c{i+1}-cta.webp","l6","left:26.67%;top:86.54%;width:46.67%","Call to action")}</div>
</figure>''' for i,h in enumerate(CRMH))
cf=''.join(f'<div class="cf-it" data-i="{i}">{cbi(f"blog-{i+1}.jpg","Blog header")}</div>' for i in range(8))
aso_a=''.join(f'<div class="as-s">{cbi(f"aso-a-{i+1}.jpg","App store screenshot, casino set")}</div>' for i in range(6))
aso_b=''.join(f'<div class="as-s">{cbi(f"aso-b-{i+1}.jpg","App store screenshot, welcome offer set")}</div>' for i in range(6))
BN=['Welcome bonus · sports','Welcome bonus · casino','Boost accumulator','Lose & win','Lose & win','Cashback','Turbo top-up','Early payout','Free bet','Bet & win','Boosted odds']
badges=''.join(f'<button type="button" class="bdg{" on" if i==10 else ""}" data-b="{i+1:02d}" data-n="{BN[i]}" style="--r:{[-6,4,-3,7,-5,3,-8,5,-2,6,-4][i]}deg" aria-label="{BN[i]}"><img src="{pre}assets/img/campobet/badges/badge-{i+1:02d}.svg" alt="" draggable="false"></button>' for i in range(11))
LG=['Road to the big game','The big championship','Summer football trivia','CampoBet trivia','Winter Race','Basketball nights','Touchdown nights','Slots of the week']
slot_faces=''.join(f'<span class="sf" style="--f:{i}"><i style="background-image:url({pre}assets/img/campobet/logo-{i+1}.webp)"></i></span>' for i in range(8))
SW3=[(11.1,19.6),(35.8,20.4),(61.3,20.7)]
slot_reels=''.join(f'<div class="sx-win" style="left:{l}%;width:{w}%"><div class="cyl">{slot_faces}</div></div>' for l,w in SW3)
slot_thumbs=''.join(f'<button type="button" class="sx-t{" on" if i==0 else ""}" data-i="{i}" aria-label="{n}"><img src="{pre}assets/img/campobet/logo-{i+1}.webp" alt="" draggable="false"></button>' for i,n in enumerate(LG))
SB1=['A man runs through a park, with a lake behind him.','Front shot: something catches his attention.','He sees a man trying to catch a fish (Big Bass slot).','The fisherman waves at him.','The runner looks bewildered.','Distracted, he bumps into the back of a tall, muscular man.','He falls back and looks up.','It’s Zeus (Gates of Olympus): “Sorry, I gotta run.”','A lightning bolt strikes and Zeus disappears.','He gets up and hears a loud noise.','A buffalo charges at him (Buffalo Blitz).','Rear shot: he runs, looking back.','A sharp turn up the steps of a kiosk.','The camera whips to a live dealer in the kiosk.','He shows his phone; everyone sits around him.','A lightning bolt strikes behind them.','Zeus joins the scene.']
SB2=['Top view of a stadium. “Welcome to CampoBet.”','Zoom transition.','A fan celebrates in the stands. “The sports passion…”','A 360° orbit with heavy motion blur.','Mid-spin, the scene becomes a casino.','She celebrates and looks at her phone.','Over-the-shoulder orbit to her screen.','A super zoom into the phone.','The brand ambassador smiles at his phone.','Final key visual with the welcome offer.']
def sb_row(k,caps,title):
    fr=''.join(f'<figure class="sb-f">{cbi(f"sb{k}-{i+1:02d}.jpg",c)}<figcaption><b>{i+1:02d}</b> {c}</figcaption></figure>' for i,c in enumerate(caps))
    return f'<div class="sb-row{" rev" if k==2 else ""}"><div class="sb-lbl"><span class="mono">Storyboard 0{k}</span><b>{title}</b></div><div class="sb-view"><div class="sb-track">{fr}{fr}</div></div></div>'
sbrows=sb_row(1,SB1,'The chase')+sb_row(2,SB2,'Brand awareness')
outs=''.join(f'<figure class="shot out">{cbi(f"out-{i+1}.jpg","Slot visual master made with the pipeline")}</figure>' for i in range(8))
# automation: anatomy (real layer stack), reflow (real coordinates), swimlanes (+ synced mini animation)
LAY=[('Background','full image, 2k',0,0,1080,1920,'bg'),('Mask group','depth layer under the copy',0,1000,1080,920,'mask'),('glow_line','light ribbon',482,-53,762,1015,'glow'),('Subject','duplicate for my cutout',160,330,760,800,'subj'),('Slot logo','official file, never redrawn',270,985,540,202,'slot'),('Logo shadow','tinted from the image',234,129,613,166,'shadow'),('Logo','brand component',314,161,451,95,'logo'),('Copy','copy component',88,1239,905,190,'copy'),('Disclaimer','auto-fit, min 14 px',62,1484,955,80,'disc')]
anat=''.join(f'<div class="an-l {k}" style="--z:{i}" data-i="{i}"><i style="left:{x/10.8:.2f}%;top:{y/19.2:.2f}%;width:{w/10.8:.2f}%;height:{h/19.2:.2f}%"></i></div>' for i,(n,d,x,y,w,h,k) in enumerate(LAY))
anlist=''.join(f'<li data-i="{i}"><span class="ly-ic {k}"></span><b>{n}</b><small>{d}</small></li>' for i,(n,d,x,y,w,h,k) in reversed(list(enumerate(LAY))))
RF={'story':(1080,1920,[(314,145,451,127),(62,295,955,852),(270,985,540,202),(88,1239,905,190),(62,1484,955,80)]),
    'reel':(1080,1920,[(314,145,451,127),(60,298,960,720),(217,918,646,179),(195,1156,690,145),(170,1337,740,85)]),
    'post':(1080,1350,[(368,83,343,97),(22,188,1036,685),(245,749,590,164),(89,955,902,189),(106,1209,868,56)]),
    'square':(1080,1080,[(368,47,343,97),(22,154,1036,513),(245,543,590,164),(98,735,884,186),(65,967,950,60)]),
    'horizontal':(1200,628,[(173,49,343,97),(689,0,513,628),(678,435,534,148),(74,267,542,114),(49,464,592,90)])}
rf_json=json.dumps(RF)
rf_tabs=''.join(f'<button type="button" role="tab" aria-selected="{"true" if k=="story" else "false"}" data-f="{k}">{k.capitalize()}<small>{w} × {h}</small></button>' for k,(w,h,_) in RF.items())
rf_imgs=''.join(f'<img class="rf-img{" on" if k=="story" else ""}" data-f="{k}" src="{pre}assets/img/campobet/rf-{k}.jpg" alt="Sugar Rush visual master, {k} format" loading="lazy" draggable="false">' for k in RF)
rf_els=''.join(f'<i class="rf-e {k}"><span>{n}</span></i>' for k,n in [('logo','Logo'),('char','Character'),('slot','Slot logo'),('copy','Copy'),('disc','Disclaimer')])
SW={'vm':[('Brief','me','ticket'),('Read the game','ai','swatch'),('Scene concepts','ai','thumbs'),('Pick the scene','me','pick'),('Two candidates','ai','cands'),('Quality gate','rule','scan'),('Approve','me','approve'),('Assemble in Figma','rule','frame'),('Final cut','me','cut')],
    'res':[('Master in','me','master'),('Format plan','rule','plan'),('Adapt the image','ai','adapt'),('Build boards','rule','boards'),('Approve all','me','approve2')],
    'crm':[('Brief','me','ticket'),('Photo','ai','photo'),('Guardrails','rule','guard'),('Layout','rule','layout'),('Review','me','review')]}
sw_json=json.dumps(SW)
mv=('<div class="mv" data-s="" aria-hidden="true">'
 '<div class="mv-el mv-ticket" data-on="ticket"><b>Brief</b><i></i><i></i><i class="s"></i></div>'
 '<div class="mv-el mv-sw" data-on="swatch"><i></i><i></i><i></i><i></i><i></i></div>'
 '<div class="mv-el mv-thumbs" data-on="thumbs pick"><i></i><i class="k"></i><i></i></div>'
 '<div class="mv-el mv-cands" data-on="cands scan approve"><i></i><i class="k"></i><span class="mv-scan"></span><span class="mv-ok">✓ ✓ ✓</span></div>'
 '<div class="mv-el mv-frame" data-on="frame cut master"><i class="f-bg"></i><i class="f-subj"></i><i class="f-logo"></i><i class="f-slot"></i><i class="f-copy"></i><i class="f-disc"></i><i class="f-cut"></i></div>'
 '<div class="mv-el mv-fmts" data-on="plan adapt boards approve2"><i style="--w:28;--h:50"></i><i style="--w:28;--h:35"></i><i style="--w:28;--h:28"></i><i style="--w:60;--h:31"></i></div>'
 '<div class="mv-el mv-photo" data-on="photo guard layout review"><i class="p-img"></i><i class="p-copy"></i><i class="p-cta"></i><i class="p-badge"></i></div>'
 '<div class="mv-el mv-guard" data-on="guard"><i>Alcohol</i><i>Cash</i><i>Skulls</i></div>'
 '<div class="mv-el mv-stamp" data-on="approve approve2 review"></div>'
 '<span class="mv-cap mono"></span></div>')

case5=head('CampoBet · Rodrigo López','Case study: brand and production design for CampoBet, an online betting brand. Social, paid, CRM, World Cup, blog and app store pieces, a rebrand for organic content, an icon and promo-logo system, and three AI production pipelines designed by Rodrigo.',pre)+nav(pre,False)+f'''<main class="cb">
  <section class="wrap c-hero">
    <div class="c-head"><div class="c-l">
      <a class="back" href="{pre}#work" data-go>← All work</a>
      <div class="c-client"><span class="tag k">CampoBet</span><span class="ai">AI system</span></div>
      <h1 class="c-title" aria-label="CampoBet"><span aria-hidden="true">{word("Campo")}{word("Bet","hlw")}</span></h1>
      </div><div class="c-r">
      <p class="c-lead">An online betting brand that needs content every single day: slots, sports, seasons and offers on every channel. I designed its organic and paid pieces, proposed the rebrand that gave its content a look of its own, and built the AI pipelines that now produce slot and CRM pieces in days.</p>
      <div class="tags c-tags"><span class="tag t">Brand design</span><span class="tag p">Social &amp; paid</span><span class="tag b">AI pipelines</span><span class="tool t-ps" title="Photoshop">Ps</span><span class="tool t-fg" title="Figma">Fg</span></div>
      <dl class="facts"><div><dt class="mono">Role</dt><dd>Brand &amp; production design, AI systems</dd></div><div><dt class="mono">Output</dt><dd>+150 pieces a month, all designed by me</dd></div><div><dt class="mono">Scope</dt><dd>Social, paid, CRM, ASO, blog, motion</dd></div><div><dt class="mono">Systems</dt><dd>3 AI pipelines I designed</dd></div></dl>
    </div></div>
    <div class="c-cover h184" aria-label="More than 150 pieces designed every month, with a few highlights">
      <div class="h-grid" aria-hidden="true">{h184}</div>
      <div class="h-count"><b class="h-n" data-n="150">+150</b><span>pieces designed<br>per month</span></div>
      <div class="h-feat">{hfeat}</div>
    </div>
  </section>

  <div class="wrap chapters">
    <aside class="toc" aria-label="Chapters">
      <ol><li><a href="#rebrand">The look</a></li><li><a href="#social">Social</a></li><li><a href="#worldcup">World Cup</a></li><li><a href="#channels">Channels</a></li><li><a href="#kit">Brand kit</a></li><li><a href="#motion">Motion</a></li><li><a href="#automation">Automation</a></li></ol>
      <div class="bar"><i></i></div>
    </aside>
    <div>
      <section class="part p1" id="work">
        <div class="part-in">
          <span class="mono">Part one · The work</span>
          <h2><span class="lm"><span>One brand,</span></span><span class="lm"><span>every day</span></span></h2>
          <p>CampoBet publishes every day: slots, sports, seasons and offers, on social, paid, email, the blog and the app stores. My job was to make all of it look like one brand, and keep it coming. This part follows that path, from the new look to the pieces that carry it.</p>
        </div>
      </section>

      <section class="chap" id="rebrand">
        <span class="mono">01 · The look</span>
        <h2><span class="lm"><span>First, a look</span></span><span class="lm"><span>of its own</span></span></h2>
        <p class="lead">The organic content needed an identity of its own. I proposed a new visual language and it was approved: from dark gradients and centred layouts to big editorial type, open white space and cut-out athletes. Drag the slider to see it change, stripe by stripe, like a lenticular print.</p>
        <div class="lenti">
          <div class="lt-row">{lenti}</div>
          <div class="lt-ax mono"><button type="button" class="lt-go" data-v="0">Before</button><input class="lt-r" type="range" min="0" max="100" value="0" aria-label="From before to after"><button type="button" class="lt-go" data-v="100">After</button></div>
        </div>
      </section>

      <section class="chap" id="social">
        <span class="mono">02 · Social</span>
        <h2><span class="lm"><span>Then, the look</span></span><span class="lm"><span>every day</span></span></h2>
        <p class="lead">With the new look in place came the daily feed: match days, fights, slots and promos, organic and paid.</p>
        <div class="subhd"><span class="mono">02.1</span><h3>The feed</h3><p>A sample of the month. Hover to pause.</p></div>
        <div class="cols">{cols}</div>
        <div class="subhd"><span class="mono">02.2</span><h3>Carousels</h3><p>Multi-slide posts for fixtures and weekly roundups. Use the arrows or the dots.</p></div>
        <div class="cars">{cars}</div>
      </section>

      <section class="chap" id="worldcup">
        <span class="mono">03 · World Cup</span>
        <h2><span class="lm"><span>The biggest</span></span><span class="lm"><span>moment of the year</span></span></h2>
        <p class="lead">For the World Cup the brand dressed up for the tournament across every channel: feed, paid, app store and CRM.</p>
        <div class="subhd"><span class="mono">03.1</span><h3>The line-up</h3><p>Eleven pieces laid out as a team. Change the formation, and pick a player to see the piece up close.</p></div>
        <div class="wc">
          <div class="wc-ui" role="group" aria-label="Formation"><span class="mono">Formation</span><button type="button" class="on" data-f="433">4-3-3</button><button type="button" data-f="442">4-4-2</button><button type="button" data-f="352">3-5-2</button></div>
          <div class="pitch"><svg class="pitch-l h" viewBox="0 0 160 100" preserveAspectRatio="none" aria-hidden="true"><rect x="2" y="2" width="156" height="96"/><path d="M80 2V98"/><circle cx="80" cy="50" r="12"/><rect x="2" y="28" width="18" height="44"/><rect x="140" y="28" width="18" height="44"/><rect x="2" y="40" width="6" height="20"/><rect x="152" y="40" width="6" height="20"/></svg><svg class="pitch-l v" viewBox="0 0 100 147" preserveAspectRatio="none" aria-hidden="true"><rect x="3" y="3" width="94" height="141"/><path d="M3 73.5H97"/><circle cx="50" cy="73.5" r="13"/><rect x="25" y="3" width="50" height="22"/><rect x="25" y="122" width="50" height="22"/><rect x="38" y="3" width="24" height="8"/><rect x="38" y="136" width="24" height="8"/></svg><span class="pitch-f mono">4-3-3</span>{wc}</div>
          <div class="wc-focus" hidden><button type="button" class="wc-x" aria-label="Back to the pitch">×</button><div class="wc-big"></div></div>
        </div>
        <div class="subhd"><span class="mono">03.2</span><h3>Promo blocks</h3><p>The Megashoot game, announced in email and in the app. Click to see them full size.</p></div>
        <div class="wcb">{wcb}</div>
        <div class="subhd"><span class="mono">03.3</span><h3>Images that kept coming back</h3><p>Some key art worked so well that it was adapted again and again across social, paid, app store and CRM. Click one to see it whole.</p></div>
        <div class="keys">{keys}</div>
      </section>

      <section class="chap" id="channels">
        <span class="mono">04 · Channels</span>
        <h2><span class="lm"><span>The same brand,</span></span><span class="lm"><span>beyond social</span></span></h2>
        <p class="lead">Email, the blog and the app stores each have their own format and their own rules. The look had to hold in all of them.</p>
        <div class="subhd" id="crm"><span class="mono">04.1</span><h3>CRM email</h3><p>Each banner is built in layers: photo, light ribbon, the cut-out subject, a shade, copy and frame, logo and button. Hover or tap one to pull the layers apart, or show only the photos.</p></div>
        <div class="crm-ui"><button type="button" class="crm-all" aria-pressed="false">Show only the photos</button></div>
        <div class="crm-grid">{crm}</div>
        <div class="subhd" id="blog"><span class="mono">04.2</span><h3>Blog</h3><p>Headers for guides, previews and promos. Drag, swipe or use the arrows.</p></div>
        <div class="cf" tabindex="0" aria-label="Blog headers">{cf}<div class="cf-ui"><button type="button" class="cf-p" aria-label="Previous">←</button><span class="cf-n mono">01 / 08</span><button type="button" class="cf-nx" aria-label="Next">→</button></div></div>
        <div class="subhd" id="aso"><span class="mono">04.3</span><h3>App store</h3><p>Two sets of store screenshots. The phone stays put and the set slides through it, the way a player swipes in the store. Use the slider to move it yourself.</p></div>
        <div class="aso-ui cbp-tabs" role="tablist" aria-label="Screenshot sets"><button role="tab" aria-selected="true" data-set="a">Casino</button><button role="tab" aria-selected="false" data-set="b">Welcome offer</button></div>
        <div class="as">
          <div class="as-track" data-set="a">{aso_a}</div><div class="as-track" data-set="b" hidden>{aso_b}</div>
          <div class="as-phone" aria-hidden="true"><div class="as-head"><i class="as-ic"></i><div><b>CampoBet</b><span>Sports &amp; casino</span></div><i class="as-get">Get</i></div><div class="as-win"></div><div class="as-lines"><i></i><i></i><i class="s"></i></div></div>
        </div>
        <input class="as-r" type="range" min="0" max="500" value="0" aria-label="Move through the screenshots">
      </section>

      <section class="chap" id="kit">
        <span class="mono">05 · Brand kit</span>
        <h2><span class="lm"><span>Parts that</span></span><span class="lm"><span>come back</span></span></h2>
        <p class="lead">Promos and campaigns return every week, so they got reusable parts: a family of badges and a set of campaign logos, built from the same brand pieces.</p>
        <div class="subhd" id="system"><span class="mono">05.1</span><h3>Badges</h3><p>One seal per promotion, readable at a glance. Tap one to stamp it.</p></div>
        <div class="bd"><div class="bdgs">{badges}</div></div>
        <div class="subhd"><span class="mono">05.2</span><h3>Campaign logos</h3><p>Seasons, trivia nights and tournaments. Pick a logo, or pull the lever, and the reels land on it.</p></div>
        <div class="slotx">
          <div class="sx-thumbs">{slot_thumbs}</div>
          <div class="sx-stage">
            <div class="sx-m"><img class="sx-img" src="{pre}assets/img/campobet/lever/f00.webp" width="900" height="483" alt="Green metallic slot machine" draggable="false">{slot_reels}<button type="button" class="sx-lever" aria-label="Pull the lever"></button></div>
            <p class="sx-name mono">{LG[0]}</p>
          </div>
        </div>
      </section>

      <section class="chap" id="motion">
        <span class="mono">06 · Motion</span>
        <h2><span class="lm"><span>When the brand</span></span><span class="lm"><span>moves</span></span></h2>
        <p class="lead">Storyboards for two videos: a slots chase through a park and a brand awareness spot. Both roll on their own; hover a row to pause it and click a frame to see it bigger.</p>
        <div class="sbs">{sbrows}</div>
      </section>

      <section class="part" id="automation">
        <div class="part-in">
          <span class="mono">Part two · The system</span>
          <h2><span class="lm"><span>The system</span></span><span class="lm"><span>behind the volume</span></span></h2>
          <p>Everything above was made by hand. To keep that pace without losing quality, I turned the brand rules into three AI production pipelines. I designed the zones, the art direction, the quality checks and the moments where a person decides. The AI renders inside those rules.</p>
          <div class="part-f"><div><b>3</b><span>pipelines</span></div><div><b>9</b><span>layers per master</span></div><div><b>5</b><span>formats from one image</span></div></div>
        </div>
      </section>

      <section class="chap" id="anatomy">
        <span class="mono">Automation · 01 · Anatomy</span>
        <h2><span class="lm"><span>Take a master</span></span><span class="lm"><span>apart</span></span></h2>
        <p class="lead">Every slot visual master is the same stack of nine layers, each one with a fixed place and a fixed job. Drag the slider to pull them apart. The names are the real layer names in the file.</p>
        <div class="anat">
          <div class="an-stage"><div class="an-stack">{anat}</div></div>
          <div class="an-side">
            <div class="an-panel"><div class="an-ph mono">Layers</div><ol class="an-list">{anlist}</ol></div>
            <label class="an-ctl mono" for="an-r">Explode<input id="an-r" class="an-r" type="range" min="0" max="100" value="70"></label>
          </div>
        </div>
      </section>

      <section class="chap" id="reflow">
        <span class="mono">Automation · 02 · Reflow</span>
        <h2><span class="lm"><span>One image,</span></span><span class="lm"><span>five placements</span></span></h2>
        <p class="lead">The resize pipeline moves every element to its stored position for each format. Below is a real Sugar Rush master in all five formats, with the stored zones drawn on top; the subject is never regenerated, only the image around it is extended.</p>
        <div class="reflow" data-rf='{rf_json}'>
          <div class="rf-tabs" role="tablist" aria-label="Formats">{rf_tabs}</div>
          <div class="rf-stage"><div class="rf-frame">{rf_imgs}{rf_els}</div></div>
          <div class="rf-foot"><p class="rf-cap mono">Story · 1080 × 1920</p><label class="rf-z mono"><input type="checkbox" checked> Show zones</label></div>
        </div>
      </section>

      <section class="chap" id="pipelines">
        <span class="mono">Automation · 03 · Pipelines</span>
        <h2><span class="lm"><span>Who does</span></span><span class="lm"><span>what</span></span></h2>
        <p class="lead">The three pipelines run as Claude skills, with Higgsfield for images and Figma for layout. Follow a piece through the lanes; the screen on the side shows what happens at each step.</p>
        <div class="swim" data-sw='{sw_json}'>
          <div class="sw-top"><div class="cbp-tabs" role="tablist" aria-label="Pipelines"><button role="tab" aria-selected="true" data-p="vm">Slot visual master</button><button role="tab" aria-selected="false" data-p="res">Resizes</button><button role="tab" aria-selected="false" data-p="crm">CRM banners</button></div><button type="button" class="sw-play">Play ►</button></div>
          <div class="sw-body">
            <div class="sw-scroll" data-lenis-prevent><div class="sw-grid"><div class="sw-lane l-me"><span>Me</span></div><div class="sw-lane l-rule"><span>Rules I wrote</span></div><div class="sw-lane l-ai"><span>AI</span></div><svg class="sw-line" aria-hidden="true"><polyline/></svg><span class="sw-dot"></span></div></div>
            {mv}
          </div>
          <div class="sw-sum mono"></div>
          <div class="cbp-loop"><b>Every approved piece becomes the new standard.</b> When I adjust a master by hand, its positions and values go back into the skill, so the next run starts from my correction.</div>
        </div>
      </section>

      <section class="chap" id="output">
        <span class="mono">Automation · 04 · Output</span>
        <h2><span class="lm"><span>What came out</span></span><span class="lm"><span>of the machine</span></span></h2>
        <p class="lead">Slot visual masters made with the pipeline, each one approved by me and then resized to every format.</p>
        <div class="drag">
          <div class="drag-track" tabindex="0" aria-label="Pipeline outputs" data-cursor="Drag">{outs}</div>
          <div class="drag-ui"><div class="bar"><i></i></div><div class="ar"><button type="button" data-prev aria-label="Previous">←</button><button type="button" data-next aria-label="Next">→</button></div></div>
        </div>
      </section>

      <section class="chap" id="impact">
        <span class="mono">Automation · 05 · Impact</span>
        <h2><span class="lm"><span>From making pieces</span></span><span class="lm"><span>to directing them</span></span></h2>
        <div class="cb-nums">
          <div><b>+150</b><p>pieces a month designed by hand before the pipelines, with 184 in the busiest one. Copy came from the content manager; every design was mine.</p><small class="mono">Counted from the content boards</small></div>
          <div><b class="pending">[N]</b><p>slot banners delivered in 2–3 days with the pipeline.</p><small class="mono">Pending · number to confirm</small></div>
          <div><b>2</b><p>moments where I step in per master: choosing the scene and approving the image.</p><small class="mono">From the pipeline design</small></div>
        </div>
      </section>
    </div>
  </div>
'''+next_block(pre,'Happy Talks','happy-talks.html',htimg(1,pre))+'''</main>
'''+scripts(pre)
open(os.path.join(R,'proyectos','campobet.html'),'w').write(case5)


# ================= MACHINE-READABLE SUMMARY (JSON-LD) =================
import json as _j
PERSON={"@type":"Person","name":"Rodrigo López","jobTitle":"Design Team Lead · Designer & Art Director",
 "description":"Designer and art director from Mexico with 10+ years of experience (since 2016). Brand design, art direction, AI-assisted key visuals, internal campaigns, UX/UI and 3D for global brands. Looking for Brand Designer or Brand Manager roles; open to remote work.",
 "email":"mailto:"+EMAIL,"address":{"@type":"PostalAddress","addressCountry":"MX"},
 "sameAs":[LI,IG],
 "worksFor":{"@type":"Organization","name":"Brainrocket"},
 "knowsAbout":["Brand design","Brand management","Art direction","Key visuals","AI image generation (Adobe Firefly, Midjourney, Stable Diffusion)","Internal communications and endomarketing","UX/UI and landing pages","3D (Blender, Cinema 4D)","Design team leadership"]}
EXPERIENCE=[("2025–present","Design Team Lead","Brainrocket","Leads the design team for international iGaming brands in Mexico and Canada, working with Marketing, CRM, ASO and Performance."),
 ("2023–2025","Senior Designer","HD* Human Design Doing","Endomarketing and culture campaigns for Philip Morris, Coca-Cola, Nestlé and more."),
 ("2020–2023","Senior Designer","Happy Studio","Concepts, 3D models and 2D animation for brand campaigns."),
 ("2018–2020","Jr. Art Director","Volátil Agencia Creativa","Creative concepts and art direction."),
 ("2016–2018","Designer","In Movisión","Print and digital design, architectural photography and web layouts.")]
WORKS=[("Happy Talks","HD* Human Design Doing (in-house)","2024","UI design for the landing page of HD*’s conference platform, desktop and mobile, delivered in two weeks. Approved at the first round and still live at happy-talks.com. Illustrator and Photoshop; no AI.","proyectos/happy-talks.html"),
 ("No Vendas Humo","Philip Morris International","","AI-assisted key visual for a sales-culture program: hand-painted reference finished with Adobe Firefly and Photoshop.","proyectos/no-vendas-humo.html"),
 ("ArboTerra es…","ArboTerra (via Happy Studio)","2023","Campaign concept, four 3D key visuals (Blender + Photoshop) and a 35-page AdBook. Approved at first presentation; the client's in-house team still uses the system three years later. Execution after the concept was done by the client.","proyectos/arboterra.html"),
 ("Conexiones Mágicas","Coca-Cola México (via HD* Human Design Doing)","","Visual concept and AI-assisted key visual (Adobe Firefly + Photoshop) for a team-building proposal for a 75-person warehouse team. Real bottle-cap photo rebuilt by hand in 12 layers.","proyectos/conexiones-magicas.html"),
 ("CampoBet","CampoBet","","Brand and production design for an online betting brand: a rebrand of the organic content (approved), an icon system, seasonal promo logos, a World Cup set, social, paid, CRM, ASO and blog pieces (more than 150 pieces a month, 184 in the busiest; copy by the content manager), and three AI production pipelines (slot visual masters, resizes, CRM banners) designed by Rodrigo as Claude skills driving Higgsfield and Figma.","proyectos/campobet.html")]
def ld_home():
    d={"@context":"https://schema.org","@graph":[dict(PERSON,**{"@id":"#rodrigo"}),
      {"@type":"ItemList","name":"Selected work","itemListElement":[{"@type":"ListItem","position":i+1,"item":{"@type":"CreativeWork","name":n,"description":ds,"url":u,"creator":{"@id":"#rodrigo"},"sourceOrganization":c,**({"dateCreated":y} if y else {})}} for i,(n,c,y,ds,u) in enumerate(WORKS)]},
      {"@type":"ItemList","name":"Experience","itemListElement":[{"@type":"ListItem","position":i+1,"item":{"@type":"OrganizationRole","roleName":r,"startDate":yr.split("–")[0],"endDate":yr.split("–")[1].replace("present",""),"description":ds,"memberOf":{"@type":"Organization","name":o}}} for i,(yr,r,o,ds) in enumerate(EXPERIENCE)]}]}
    return '<script type="application/ld+json">'+_j.dumps(d,ensure_ascii=False)+'</script>\n<link rel="alternate" type="text/markdown" href="llms.txt" title="Plain-text summary">\n'
def ld_case(i):
    n,c,y,ds,u=WORKS[i]
    cr=dict(PERSON); 
    if n=="CampoBet": cr.pop("worksFor",None)
    d={"@context":"https://schema.org","@type":"CreativeWork","name":n,"description":ds,"sourceOrganization":c,**({"dateCreated":y} if y else {}),"creator":cr}
    return '<script type="application/ld+json">'+_j.dumps(d,ensure_ascii=False)+'</script>\n<link rel="alternate" type="text/markdown" href="../llms.txt" title="Plain-text summary">\n'
def inject(path,tag):
    t=open(path).read(); 
    if 'application/ld+json' not in t: t=t.replace('</head>',tag+'</head>',1)
    open(path,'w').write(t)
inject(os.path.join(R,'index.html'),ld_home())
for i,f in enumerate(['happy-talks','no-vendas-humo','arboterra','conexiones-magicas','campobet']): inject(os.path.join(R,'proyectos',f+'.html'),ld_case(i))
md=["# Rodrigo López — Designer & Art Director","",PERSON["description"],"",f"- Email: {EMAIL}",f"- LinkedIn: {LI}",f"- Instagram: {IG}",f"- WhatsApp: {WA}","- Location: Mexico · open to remote","","## Experience"]
md+= [f"- {yr} · {r}, {o}. {ds}" for yr,r,o,ds in EXPERIENCE]
md+=["","## Selected work"]+[f"- [{n}]({u}) — {c}{' · '+y if y else ''}. {ds}" for n,c,y,ds,u in WORKS]
md+=["","## Highlights (as shown on the site)","- 13 AI-assisted campaigns for global brands.","- One AI-adoption program reached 1,070 employees.","- 700+ people at the Mars integration “Day Zero”.","","## Skills"]+[f"- {k}" for k in PERSON["knowsAbout"]]
open(os.path.join(R,'llms.txt'),'w').write("\n".join(md)+"\n")
print('ok')
