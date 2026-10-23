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
    <h2 style="margin-top:1.2rem"><span class="lm"><span>Let’s make</span></span><span class="lm"><span class="o">something</span> <span>big</span></span></h2>
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
    o=f'<a class="card" href="{href}" data-go data-cursor="{"See process" if aiflag else "See case"}">' if not soon else f'<div class="card soon" data-cursor="Coming soon">'
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
roles2='<span>Creative ideas</span><span>Big results</span><span>Human craft</span><span>AI as copilot</span>'
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
        <span class="stk s1" aria-hidden="true">Creative</span>
        <span class="stk s2" aria-hidden="true">ideas,</span>
        <span class="stk s5" aria-hidden="true">✳ since 2016</span>
        <span class="stk s3" aria-hidden="true">big</span>
        <span class="stk s4" aria-hidden="true">results</span>
      </h1>
      <p class="drag-hint mono">Drag the words around ✋</p>
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
    <p class="big">I turn <span class="hw sk" data-k="sk" tabindex="0">a rough sketch</span> into <span class="hw cp" data-k="cp" tabindex="0">a finished campaign</span>, with AI as my <span class="hw co" data-k="co" tabindex="0">copilot</span> and design as the final word.</p>
    <p class="say-hint mono muted">Hover the highlighted words. Each time, a different real project.</p>
    <div class="peekimg" aria-hidden="true"><img alt=""><span></span></div>
    <div class="tools-pop" aria-hidden="true"><span class="tool t-ff">Ff</span><span class="tool t-mj">Mj</span><span class="tool t-sd">Sd</span><span class="tool t-ps">Ps</span></div>
  </section>

  <section class="stage" id="work">
    <div class="sec wrap">
      <div class="sec-h">
        <h2><span class="lm"><span>Selected</span></span><span class="lm"><span>work<i class="n">07</i></span></span></h2>
        <div><p>Campaigns and digital work for global brands. On AI projects, hover to see the sketch they started from.</p></div>
      </div>
      <div class="grid">
{card(1,"proyectos/happy-talks.html","HDO · 2025","Happy Talks","Landing page for a disruptive conference platform. UX/UI, art direction and 3D.",["Web","UX/UI","3D"],ht(1,"Happy Talks landing page",pre))}
{card(2,"proyectos/no-vendas-humo.html","Philip Morris International","No Vendas Humo","Key visual for a smoke-free sales culture program.",["Key visual","Firefly","Photoshop"],ai("pmi-humo-final","Smoke letters reading No Vendas Humo",pre),"pmi-humo-ref",True)}
{card(3,"proyectos/arboterra.html","ArboTerra · Africam Safari","ArboTerra es…","Campaign system approved at first pitch, still in use 3 years later.",["Campaign","3D","Blender"],'<div class="ph"><img src="assets/img/arboterra/kv-aventura.jpg" alt="The Árbol Arcano floating over teal clouds" loading="lazy" decoding="async" draggable="false"></div>')}
{card(4,"","Coca-Cola","Conexiones Mágicas","Team experience for a 75-person concentrate plant.",["Key visual","Firefly"],ai("coca-final","A hand catching a bottle cap in red light",pre),"coca-ref",True,True)}
{card(5,"","DiDi Food","Fuerza DiDi","Annual internal concept for business developers.",["Campaign","Firefly"],ai("didi-final","A hand holding a light saber handle",pre),"didi-ref",True,True)}
{card(6,"","Megagas","Amo Aquí","Service culture campaign for a Shell retail partner.",["Campaign","Firefly"],ai("megagas-final","A fuel hose shaped like a heart",pre),"megagas-ref",True,True)}
{card(7,"","Mars Wrigley","Snackable","Integration festival for 700+ associates.",["Event","Firefly"],ai("mars-final","Hands holding snacks under a blue sky",pre),"mars-ref",True,True)}
      </div>
    </div>
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
    return f'''  <a class="next" href="{href}" data-go data-cursor="Next">
    <div class="wrap"><span class="mono">Next project</span><h2>{title} →</h2></div>
    <div class="peek">{img}</div>
    <div class="wrap"><div class="foot mono"><span>© 2026 Rodrigo López</span><span>{EMAIL}</span></div></div>
  </a>
'''

case=head('Happy Talks · Rodrigo López','Case study: Happy Talks landing page for HDO. UX/UI, art direction and 3D.',pre)+nav(pre,False)+f'''<main>
  <section class="wrap c-hero">
    <div class="c-head"><div class="c-l">
      <a class="back" href="{pre}#work" data-go>← All work</a>
      <div class="c-client"><span class="tag k">HDO</span><span class="tag">Web · 2025</span></div>
      <h1 class="c-title" aria-label="Happy Talks"><span aria-hidden="true">{word("Happy","hlw")} {word("Talks")}</span></h1>
      </div><div class="c-r">
      <p class="c-lead">A landing page for a disruptive conference platform: an intangible offer turned into a visual experience that presents the speakers and generates requests.</p>
      <div class="tags c-tags"><span class="tag t">UX/UI</span><span class="tag p">Art direction</span><span class="tag b">3D</span><span class="tool t-ai" title="Illustrator">Ai</span><span class="tool t-ps" title="Photoshop">Ps</span><span class="tool t-fg" title="Figma">Fg</span></div>
      <dl class="facts"><div><dt class="mono">Role</dt><dd>UX/UI, art direction, 3D</dd></div><div><dt class="mono">Client</dt><dd>HDO</dd></div><div><dt class="mono">Year</dt><dd>2025</dd></div><div class="todo"><dt class="mono">Result</dt><dd>To be added</dd></div></dl>
    </div></div>
    <div class="c-cover">{htimg(1,pre)}</div>
  </section>

  <div class="wrap chapters">
    <aside class="toc" aria-label="Chapters">
      <ol><li><a href="#challenge">Challenge</a></li><li><a href="#approach">Approach</a></li><li><a href="#landing">The landing</a></li><li><a href="#concept">Concept</a></li><li><a href="#results">Results</a></li></ol>
      <div class="bar"><i></i></div>
    </aside>
    <div>
      <section class="chap" id="challenge">
        <span class="mono">01 · Challenge</span>
        <h2><span class="lm"><span>Make the intangible</span></span><span class="lm"><span>feel tangible</span></span></h2>
        <div class="quotes">
          <div class="quote a"><b>01</b><p>Communicate an intangible offer, conferences, in a tangible and appealing way.</p></div>
          <div class="quote b"><b>02</b><p>Stand out in a crowded market of organizational development services.</p></div>
        </div>
      </section>

      <section class="chap" id="approach">
        <span class="mono">02 · Approach</span>
        <h2><span class="lm"><span>A conference that</span></span><span class="lm"><span>doesn’t feel like one</span></span></h2>
        <p class="lead">Happy Talks offers disruptive talks that spark reflection and drive change inside organizations. The page had to feel the same: authentic, memorable and far from corporate.</p>
        <p class="pull">Less brochure, more <em>backstage pass</em>.</p>
        <div class="two-col lists">
          <div><h3>Goals</h3><ul><li>Present the speakers and their talks.</li><li>Generate leads with a clear path to a request.</li><li>Tell the story with an agile structure.</li></ul></div>
          <div><h3>Scope</h3><ul><li>UX/UI, desktop and mobile</li><li>Visual language: type, color and stickers</li><li>Art direction, photography and illustration</li><li>3D modeling of key elements</li></ul></div>
        </div>
        <div class="wipe bleed-in">{ht(3,"Happy Talks hero with a 3D microphone",pre)}</div>
      </section>

      <section class="chap" id="landing">
        <span class="mono">03 · The landing</span>
        <h2><span class="lm"><span>Section by section</span></span></h2>
        <p class="lead">From first impact to the conference request. Drag to explore.</p>
        <div class="drag">
          <div class="drag-track" tabindex="0" aria-label="Landing page screens" data-cursor="Drag">
{gal}
          </div>
          <div class="drag-ui"><div class="bar"><i></i></div><div class="ar"><button type="button" data-prev aria-label="Previous">←</button><button type="button" data-next aria-label="Next">→</button></div></div>
        </div>
      </section>

      <section class="chap" id="concept">
        <span class="mono">04 · Concept</span>
        <h2><span class="lm"><span>Energy with</span></span><span class="lm"><span>a human face</span></span></h2>
        <div class="swatches" aria-label="Happy Talks palette">
          <div class="sw" style="background:#141218;color:#fff">Stage black</div>
          <div class="sw" style="background:#B45CF2;color:#141218">Purple</div>
          <div class="sw" style="background:#FFE14D;color:#141218">Yellow</div>
          <div class="sw" style="background:#3DDC97;color:#141218">Mint</div>
          <div class="sw" style="background:#FF4FD8;color:#141218">Magenta</div>
        </div>
        <div class="concept">
          <div><h3>Vibrant tones that carry energy and positivity</h3><p>So the brand feels like an event, not a corporate service.</p></div>
          <div><h3>Illustration and photography that humanize the brand</h3><p>Real speaker portraits with hand-drawn strokes and stickers.</p></div>
        </div>
        <div class="wipe tall">{ht(11,"Happy Talks landing page on mobile",pre)}</div>
      </section>

      <section class="chap" id="results">
        <span class="mono">05 · Results</span>
        <div class="todo-box"><h3>Metrics coming soon</h3><p>Conference requests, conversion or time on page will live here.</p></div>
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
      <dl class="facts"><div><dt class="mono">Role</dt><dd>Concept, art direction, AI imagery</dd></div><div><dt class="mono">Agency</dt><dd>HD* Human Design Doing</dd></div><div><dt class="mono">Program</dt><dd>2.5-day training</dd></div><div class="todo"><dt class="mono">Result</dt><dd>To be added</dd></div></dl>
    </div></div>
    <div class="c-cover">{aiimg('pmi-humo-final',pre).replace('alt=""','alt="Final key visual: letters made of smoke reading No vendas humo"')}<figure class="c-sticker">{aiimg('pmi-humo-ref',pre)}<figcaption class="mono">It started as this sketch</figcaption></figure></div>
  </section>

  <div class="wrap chapters">
    <aside class="toc" aria-label="Chapters">
      <ol><li><a href="#challenge">Challenge</a></li><li><a href="#idea">Idea</a></li><li><a href="#process">AI process</a></li><li><a href="#compare">Before / after</a></li><li><a href="#results">Results</a></li></ol>
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

      <section class="chap" id="results">
        <span class="mono">05 · Results</span>
        <div class="todo-box"><h3>Metrics coming soon</h3><p>Participation, adoption of the “Perfect PMI Store” routines or feedback from the sales team will live here.</p></div>
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
layers=''.join(f'<div class="m-layer{" on" if i==0 else ""}" data-m="{m}">{at("bg-"+m,"","bg",i>0)}{at("tree-"+m,"","tree",i>0)}</div>' for i,(m,l,w,c) in enumerate(moods))
locks=''.join(f'<img class="lock{" on" if i==0 else ""}" data-m="{m}" src="{pre}assets/img/arboterra/lock-{w}{"" if c=="#FFFFFF" else "-teal"}.png" alt="ArboTerra es {w}" style="--h:{LOCK[w][1]/133:.3f}" draggable="false">' for i,(m,l,w,c) in enumerate(moods))
tabs=''.join(f'<button type="button" data-m="{m}" aria-pressed="{"true" if i==0 else "false"}">{l}</button>' for i,(m,l,w,c) in enumerate(moods))
promos=[('promo-1','Alegría','Photo promos put real kids at the center.'),('promo-2','Celebración','Birthday packages, same type system.'),('promo-3','Celebración','A second take for the same offer.'),('promo-4','Aventura','Park photography with the brand lockup.'),('promo-5','Aventura','Greens and depth, no tree needed.'),('promo-6','Aventura','The path into the park.'),('app-story','Story','The tree adapted to a vertical story.'),('app-vertical','Vertical','A narrow format for print and screens.')]
pgal='\n'.join(f'        <figure class="shot pt">{at(n,f"ArboTerra {t} piece")}<figcaption><b>{i+1:02d} · {t}</b><span>{d}</span></figcaption></figure>' for i,(n,t,d) in enumerate(promos))
ig=[('ig-1','Oct 21, 2026','The Árbol Arcano, now under a glass dome for World Energy Saving Day.'),('ig-2','Sep 28, 2026','The block-cut lettering, reused for the park’s kids podcast.'),('ig-3','Sep 3, 2026','Same podcast, same type system, new scene.')]
igal='\n'.join(f'        <figure class="shot ig">{at(n,f"ArboTerra Instagram post from {d}")}<figcaption><b>@arboterra · {d}</b><span>{t}</span></figcaption></figure>' for n,d,t in ig)
steps=[('Background','Photo, blurred and color-graded to match the word.'),('Árbol Arcano','The 3D tree: a floating island with a waterfall and a balloon.'),('Supporting elements','Birds from the park, bubbles and light.'),('Final','Lockup and call to action: ¡Ven y explora!')]
bsteps=''.join(f'<button type="button" data-i="{i}" aria-pressed="{"true" if i==0 else "false"}"><b>{i+1:02d}</b>{t}</button>' for i,(t,d) in enumerate(steps))
bimgs=''.join(f'<figure class="b-img{" on" if i==0 else ""}">{at(f"build-{i+1}",f"Construction step {i+1}: {t}")}</figure>' for i,(t,d) in enumerate(steps))
bnotes=''.join(f'<p class="b-note{" on" if i==0 else ""}">{d}</p>' for i,(t,d) in enumerate(steps))

case3=head('ArboTerra es… · Rodrigo López','Case study: an open-ended campaign system for ArboTerra, Africam Safari’s secret world. Concept, art direction and 3D.',pre)+nav(pre,False)+f'''<main>
  <section class="wrap c-hero arbt">
    <div class="c-head"><div class="c-l">
      <a class="back" href="{pre}#work" data-go>← All work</a>
      <div class="c-client"><span class="tag k">ArboTerra · Africam Safari</span><span class="tag">Campaign · 2023</span></div>
      <h1 class="c-title" aria-label="ArboTerra es…"><span aria-hidden="true">{word("ArboTerra")} {word("es…","hlw")}</span></h1>
      </div><div class="c-r">
      <p class="c-lead">A park nobody could define got a campaign that never finishes the sentence. One floating tree, four moods and a type system the client still uses three years later.</p>
      <div class="tags c-tags"><span class="tag t">Concept</span><span class="tag p">Art direction</span><span class="tag b">3D</span><span class="tool t-bl" title="Blender">Bl</span><span class="tool t-ps" title="Photoshop">Ps</span></div>
      <dl class="facts"><div><dt class="mono">Role</dt><dd>Concept, art direction, 3D</dd></div><div><dt class="mono">Agency</dt><dd>Happy Studio</dd></div><div><dt class="mono">Timeline</dt><dd>2–3 months</dd></div><div class="win"><dt class="mono">Result</dt><dd>Still in use, 3 years on</dd></div></dl>
    </div></div>
    <div class="moods" data-cursor="Change mood">
      <div class="m-stage">{layers}<div class="m-locks">{locks}</div></div>
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
        <p class="lead">ArboTerra, the secret world inside Africam Safari, had a problem: many families didn’t know what it was.</p>
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
          <div class="quote a"><b>2023 → 2026</b><p>The tree, the lettering and #ArboTerraesMagia are still on the park’s Instagram.</p></div>
        </div>
        <p class="muted" style="margin-top:2.4rem">The client wanted something timeless. Here’s the park’s Instagram today:</p>
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
'''+next_block(pre,'Happy Talks','happy-talks.html',htimg(1,pre))+'''</main>
'''+scripts(pre)
open(os.path.join(R,'proyectos','arboterra.html'),'w').write(case3)
print('ok')
