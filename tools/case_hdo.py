"""HDO case: two landings, two moods. Imported by build.py."""
import os
from PIL import Image as _I

def build(R, pre, head, nav, scripts, word, next_block):
    D=os.path.join(R,'assets/img/hdo')
    def hd(name,alt='',cls='',lazy=True,ext=None):
        e=ext or ('webp' if os.path.exists(os.path.join(D,name+'.webp')) else 'jpg')
        w,h=_I.open(os.path.join(D,f'{name}.{e}')).size
        c=f' class="{cls}"' if cls else ''
        l=' loading="lazy" decoding="async"' if lazy else ''
        return f'<img src="{pre}assets/img/hdo/{name}.{e}" alt="{alt}"{c} width="{w}" height="{h}" draggable="false"{l}>'

    # ---------- browser notes (fractions of the full-page height) ----------
    pp_notes=[(0.0,'Hero','A 3D figure leans on the title; the toy-like button is the only orange object on screen.'),
              (0.17,'Date & trainer','City, date and the certified trainer, so the play reads as a professional event.'),
              (0.29,'Play like a pro','The method, then the logos of companies that already use it. Proof before any pitch.'),
              (0.41,'How it works','Four steps as playing cards, from playing to deciding.'),
              (0.52,'Facilitator','Credentials in full: a serious bio next to a figure with its arms up.'),
              (0.665,'The line','“When you have a problem, solve it by playing.” The idea in one orange band.'),
              (0.735,'Sign-up','The title comes back with a video, so the page closes with the same promise.'),
              (0.905,'Footer','HDO’s shared footer, in Pro Play orange.')]
    cc_notes=[(0.0,'Hero','Brush lettering and a founder mid-shout: culture as energy, not a slide.'),
              (0.10,'Contact if…','Four reasons to write, as cards. Leads start here, not at the bottom.'),
              (0.245,'Form','The last field asks “What’s your dream?” instead of “Message”.'),
              (0.335,'28 years','Inflated 3D numbers and a pun: our story lasts 28 years, the rest is just tales.'),
              (0.41,'Case study','Cinépolis employer branding as a bento grid of real pieces.'),
              (0.585,'Diagnostics','The culture tools as a carousel of cards.'),
              (0.665,'Founder','José L. Pinheiro in his bowler hat, with the topics he talks about.'),
              (0.765,'The team','A marquee of HDO° and color-blocked portraits: consultants as a cast.'),
              (0.925,'Footer','The same HDO footer, now in pink.')]
    def notes(ns): return ''.join(f'<li data-y="{y:.4f}"><b>{i+1:02d}</b><span><strong>{t}</strong>{d}</span></li>' for i,(y,t,d) in enumerate(ns))
    def browser(cls,url,img,alt,ns,w,h):
        return f'''<div class="browser {cls}" data-cursor="Scroll it">
          <div class="br-bar"><i></i><i></i><i></i><span>{url}</span><em class="br-live">Auto-scrolling · hover to take over</em></div>
          <div class="br-body">
            <div class="br-view" data-lenis-prevent tabindex="0" aria-label="{alt}, scrollable"><img src="{pre}assets/img/hdo/{img}.jpg" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async" draggable="false"></div>
            <ol class="br-notes" aria-label="Design notes by section">{notes(ns)}</ol>
          </div>
        </div>'''

    # ---------- assembly instructions: the real PSD layers, piece by piece ----------
    # bbox in the 1920x1080 PSD -> % of the stage. ex = exploded pose (dx,dy in % of stage, rot, scale)
    def pc(x0,y0,x1,y1): return (x0/19.2,y0/10.8,(x1-x0)/19.2,(y1-y0)/10.8)
    # loose-part spots on the table at step 00: centre (cx,cy in % of stage), rotation, scale
    L=[('type','asm-type',pc(143,228,1396,828),(31,34,-6,.5)),
       ('fig','asm-toy',pc(51,466,295,903),(13,70,18,.75)),
       ('btn','asm-btn',pc(1106,534,1905,787),(73,30,7,.42)),
       ('btn','asm-conoce',pc(1397,422,1658,505),(74,64,-5,.8)),
       ('sph','asm-ball',pc(119,270,201,350),(52,84,0,1)),('sph','asm-ball',pc(1126,270,1149,293),(59,86,0,1)),
       ('sph','asm-ball',pc(1754,264,1792,300),(64,85,0,1)),('sph','asm-ball',pc(1179,825,1228,873),(70,85,0,1)),
       ('sph','asm-ball',pc(1858,837,1950,926),(78,84,0,1)),('sph','asm-ball',pc(191,1029,270,1106),(87,84,0,1))]
    steps=[('Parts','Everything in the box, straight from the PSD: a background, the type lockup, one figure, one button and six spheres.',None),
           ('Background','A blue field with soft blobs and HDO’s nav, the frame both landings share.','bg'),
           ('Type','“Juega y conoce”, the outlined PRO PLAY and the PLAYMOBIL pro logo go in as one lockup.','type'),
           ('Figure','A plain white figure, modeled in Blender, leans on the title so the toy is part of the headline.','fig'),
           ('Button','One orange, toy-like button. Nothing else on screen looks pressable.','btn'),
           ('Spheres','Six orange spheres repeat the button color across the page.','sph'),
           ('Done','The hero, as it went live.','done')]
    akeys=','.join((k or '') for t,d,k in steps)
    def lay(i,k,n,g,e):
        x,y,w,h=g;cx,cy,r,sc=e
        dx=cx-(x+w/2);dy=(cy-(y+h/2))*0.5625
        return f'<span class="asm-l{" btn-main" if n=="asm-btn" else ""}" data-s="{k}" style="--x:{x:.2f}%;--y:{y:.2f}%;--w:{w:.2f}%;--dx:{dx:.2f}cqw;--dy:{dy:.2f}cqw;--r:{r}deg;--s:{sc};--d:{(i%6)*80}ms">{hd(n,"")}</span>'
    layers=f'<div class="asm-l asm-bgl" data-s="bg">{hd("asm-bg","")}</div>'+''.join(lay(i,k,n,g,e) for i,(k,n,g,e) in enumerate(L))
    sph_masks=''
    ptray=''
    asteps=''.join(f'<button type="button" data-i="{i}" aria-pressed="{"true" if i==0 else "false"}"><b>{i:02d}</b>{t}</button>' for i,(t,d,k) in enumerate(steps))
    anotes=''.join(f'<p class="asm-note{" on" if i==0 else ""}">{d}</p>' for i,(t,d,k) in enumerate(steps))
    parts='<ul class="asm-parts" aria-label="Parts"><li><b>1×</b>background</li><li><b>1×</b>type lockup</li><li><b>1×</b>figure</li><li><b>1×</b>button</li><li><b>6×</b>spheres</li></ul>'

    # ---------- shared drawing helpers ----------
    def wave(cls,d):
        return f'<svg class="wave {cls}" viewBox="0 0 1440 140" preserveAspectRatio="none" aria-hidden="true"><path d="{d}" fill="currentColor"/></svg>'
    W_UP='M0,92 C180,40 360,20 560,58 C760,96 920,130 1120,96 C1260,72 1360,40 1440,52 L1440,140 L0,140 Z'
    W_DN='M0,0 L1440,0 L1440,60 C1300,110 1120,124 920,92 C720,60 560,18 360,40 C200,58 90,96 0,84 Z'
    def fl(name,x,y,w,d,cls='',delay=0):
        return f'<span class="fl {cls}" style="--x:{x}%;--y:{y}%;--w:{w};--dl:{delay}s" data-d="{d}" aria-hidden="true">{hd(name,"")}</span>'
    def scribble(cls,paths):
        ps=''.join(f'<path d="{p}" pathLength="1"/>' for p in paths)
        return f'<svg class="scrib {cls}" viewBox="0 0 1000 600" preserveAspectRatio="none" aria-hidden="true">{ps}</svg>'

    # ---------- Pro Play: the three challenges ----------
    challenges=[('01','tri-01','fig-wave-a','Break the prejudice that play isn’t serious work.','Proof comes first: the client logos sit right under “Play like a pro”, and the trainer’s credentials get a block of their own.'),
                ('02','tri-02','fig-armsup','Make a hands-on workshop understood on one page.','The method becomes four cards (start playing, observe, extract insights, decide), then a video and the same call to action.'),
                ('03','tri-03','fig-tophat','Speak PLAYMOBIL pro’s visual language.','Plain white figures modeled in Blender, outlined PRO PLAY type and a rounded 3D button that looks like a toy.')]
    ch_cards=''.join(f'''<article class="pp-card" tabindex="0">
            <span class="pp-peek" aria-hidden="true">{hd(fig,"")}</span>
            <div class="pp-card-in">
              <div class="pp-tri">{hd(tri,"Challenge "+n)}</div>
              <h3>{q}</h3>
              <span class="pp-rule" aria-hidden="true"></span>
              <p><strong>How the design answered</strong>{a}</p>
            </div>
          </article>''' for n,tri,fig,q,a in challenges)

    # ---------- Cultura: where each decision lives ----------
    dec=[('pk-flask','Brush lettering over pink','The hero shouts: “Impulsa una cultura colectiva” in hand lettering, with the founder mid-gesture. Culture as energy, not a slide.','cc-s-hero'),
         ('pk-cross','Four reasons to write','Leads start at the top, not at the bottom: four cards name the reasons to get in touch, each with its own 3D icon.','cc-s-cards'),
         ('pk-cone','A form that asks for dreams','The last field reads “What’s your dream?” instead of “Message”. The form opens a conversation.','cc-s-form'),
         ('pk-sphere','28 years, told as a tale','Inflated 3D numbers and a pun: “our story lasts 28 years, the rest is just tales”.','cc-s-28'),
         ('pk-spring','Proof in a bento grid','The Cinépolis employer-branding case as a grid of real pieces: logo, posters and photos.','cc-s-case'),
         ('pk-tube-a','Consultants as a cast','The founder in his bowler hat, a CONSULTORES HDO° marquee and color-blocked portraits, like a show’s lineup.','cc-s-team')]
    dec_list=''.join(f'<li><button type="button" data-i="{i}" aria-pressed="{"true" if i==0 else "false"}"><span class="cd-ic">{hd(o,"")}</span><span class="cd-t"><b>{i+1:02d}</b>{t}</span></button></li>' for i,(o,t,d,im) in enumerate(dec))
    dec_imgs=''.join(f'<figure class="cd-img{" on" if i==0 else ""}" data-i="{i}">{hd(im,"Cultura Colectiva landing: "+t,lazy=i>0)}</figure>' for i,(o,t,d,im) in enumerate(dec))
    dec_notes=''.join(f'<p class="cd-note{" on" if i==0 else ""}" data-i="{i}">{d}</p>' for i,(o,t,d,im) in enumerate(dec))

    marq=''.join('<span>CONSULTORES HDO°</span><span class="o">CONSULTORES HDO°</span>' for _ in range(6))
    cast=''.join(f'<figure class="cast-f" style="--c:{c}">{hd(n,a)}<figcaption>{cap}</figcaption></figure>' for n,a,cap,c in [
        ('fig-wave-a','White figure waving, Pro Play hero','Hero','var(--po)'),('fig-bowler','Figure with a bowler hat, waving','Bowler','var(--pc)'),
        ('fig-wizard','Figure with a wizard hat and wand','Footer','var(--pp)'),('fig-tophat','Figure with a top hat and briefcase','Presentation','#F2A01E'),
        ('fig-armsup','White figure with arms up','Facilitator','var(--cp)'),('fig-mic','Figure with a bowler hat and a red microphone','Bowler &amp; mic','var(--cv)')])

    S1=['M-20,120 C180,40 380,220 560,120 C720,30 860,160 1020,80','M-20,520 C160,430 300,600 470,500 C640,400 760,560 1020,470']
    S2=['M-20,300 C120,180 260,420 420,300 C560,190 700,360 860,250 C930,200 980,230 1020,210','M60,560 C220,470 360,590 520,520 C700,440 860,560 1020,500']

    fonts='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;700;800&family=Permanent+Marker&display=swap">\n'
    page=head('One House, Two Moods · HDO landings · Rodrigo López','Case study: two landing pages for HDO Culture & Change, Pro Play (2024) and Cultura Colectiva (2023). UX/UI, branding, art direction and 3D in Blender.',pre).replace('</head>',fonts+'</head>',1)+nav(pre,False)+f'''<main class="hdo">
  <section class="wrap c-hero">
    <div class="c-head"><div class="c-l">
      <a class="back" href="{pre}#work" data-go>← All work</a>
      <div class="c-client"><span class="tag k">HDO Culture &amp; Change · HD*</span><span class="tag">Web · 2023–2024</span></div>
      <h1 class="c-title" aria-label="One house, two moods"><span aria-hidden="true">{word("One")} {word("house,")} {word("two","hlw")} {word("moods","hlw")}</span></h1>
      </div><div class="c-r">
      <p class="c-lead">Two landing pages for HDO, a culture and change consultancy, one year apart. They share a logo, a nav and a footer, and almost nothing else. Pro Play had to make a toy look like a serious business tool. Cultura Colectiva had to make 28 years of consulting feel young.</p>
      <div class="tags c-tags"><span class="tag t">UX/UI</span><span class="tag p">Branding</span><span class="tag b">3D</span><span class="tool t-bl" title="Blender">Bl</span></div>
      <dl class="facts"><div><dt class="mono">Role</dt><dd>UX/UI, branding, art direction, 3D</dd></div><div><dt class="mono">Scope</dt><dd>Design only · built by HDO</dd></div><div><dt class="mono">Years</dt><dd>2023 · 2024</dd></div><div class="win"><dt class="mono">Result</dt><dd>Both still live, with later changes</dd></div></dl>
    </div></div>
    <div class="c-cover hdo-split">
      <a class="hs pp" href="#pro-play" aria-label="Go to Pro Play">{hd("pp-hero","Pro Play landing hero: a white figure leaning on the title and an orange Regístrate button",lazy=False)}<span class="hs-l"><b>Pro Play</b><small>Bogotá · 2024</small></span></a>
      <a class="hs cc" href="#cultura" aria-label="Go to Cultura Colectiva">{hd("cc-hero","Cultura Colectiva landing hero: brush lettering over pink and the founder in a lab coat",lazy=False)}<span class="hs-l"><b>Cultura Colectiva</b><small>Mexico · 2023</small></span></a>
    </div>
  </section>

  <div class="hdo-ch">
    <aside class="toc" aria-label="Chapters">
      <ol><li><a href="#house">Two projects</a></li><li><a href="#pro-play">Pro Play</a></li><li><a href="#cultura">Cultura</a></li><li><a href="#cast">The cast</a></li><li><a href="#result">Result</a></li></ol>
      <div class="bar"><i></i></div>
    </aside>

    <div class="wrap">
      <section class="chap" id="house">
        <span class="mono">00 · Two projects</span>
        <h2><span class="lm"><span>Same house,</span></span><span class="lm"><span>opposite moods</span></span></h2>
        <p class="lead">HDO helps companies build more human cultures, with workshops, diagnostics and consulting. These two pages sell different things to different crowds, so each one got its own world.</p>
        <div class="duo">
          <a class="duo-f pp" href="#pro-play">
            <span class="duo-n">Project 01</span>
            <div class="duo-img">{hd("pp-hero","Pro Play landing hero")}</div>
            <div class="duo-t"><b>Pro Play</b><span>A free PLAYMOBIL pro workshop in Bogotá · 2024</span><span class="duo-mood">Blue, orange and toys <i>→</i></span></div>
          </a>
          <a class="duo-f cc" href="#cultura">
            <span class="duo-n">Project 02</span>
            <div class="duo-img">{hd("cc-hero","Cultura Colectiva landing hero")}</div>
            <div class="duo-t"><b>Cultura Colectiva</b><span>HDO’s own consultancy page · 2023</span><span class="duo-mood">Pink, brush and lab glass <i>→</i></span></div>
          </a>
        </div>
      </section>
    </div>

    <!-- =================== PROJECT 01 · PRO PLAY =================== -->
    <section class="world pp" id="pro-play">
      {wave("top",W_UP)}
      <div class="fls" aria-hidden="true">
        {fl("sphere-o1",6,6,4.4,-.25)}{fl("sphere-o2",88,3,2.6,-.5,"",.8)}{fl("sphere-o1",94,31,5.6,-.15,"",.4)}{fl("sphere-o2",3,43,2.2,-.6,"",1.2)}{fl("sphere-o1",91,62,3,-.35,"",.2)}{fl("sphere-o2",8,78,3.4,-.2,"",.6)}{fl("sphere-o1",52,92,2.4,-.45,"",1)}
      </div>
      <div class="wrap">
        <header class="w-open">
          <span class="w-tag">Project 01 · Bogotá, 2024</span>
          <h2 class="pp-title" aria-label="Pro Play"><span class="o1">PRO</span> <span class="o2">PLAY</span></h2>
          {hd("fig-wave-a","","pp-lean")}
          <p class="w-kick">Make play look like serious work.</p>
          <div class="w-intro">
            <p>Pro.Play is a method created by Juan Prego and endorsed by PLAYMOBIL pro: teams model real problems with figures to find new answers. HD* brought a free, in-person workshop to Bogotá, led by Jaime Lastra, one of the few certified trainers in Latin America.</p>
            <p>The challenge: sell the professional value behind a toy, on a single page.</p>
          </div>
          <ul class="w-facts"><li><b>21 May</b>Workshop date</li><li><b>Free</b>In-person workshop</li><li><b>1 page</b>From hook to sign-up</li></ul>
        </header>

        {browser("pp","HDO · Pro Play landing","pp-full","The full Pro Play landing page, top to bottom",pp_notes,1400,5895)}

        <div class="w-sec">
          <h3 class="w-h"><span>Assembly</span> instructions</h3>
          <p class="w-p">Like the booklet in a Playmobil box: the hero, rebuilt from the real layers of the PSD.</p>
        </div>
        <div class="asm" data-keys="{akeys}">
          <div class="asm-stage" aria-label="The Pro Play hero, assembled step by step">
            {hd("pp-hero-line","Line drawing of the Pro Play hero, like an instruction sheet","asm-line")}
            {layers}
            <span class="asm-num" aria-hidden="true">00</span>
          </div>
          <div class="asm-side">
            {parts}
            <div class="asm-steps" role="group" aria-label="Assembly steps">{asteps}</div>
            <div class="asm-notes" aria-live="polite">{anotes}</div>
          </div>
        </div>

        <div class="w-sec">
          <h3 class="w-h"><span>Three</span> challenges</h3>
          <p class="w-p">Built like the landing’s own “¿Cómo funciona?” cards. Hover one and its figure pops up.</p>
        </div>
        <div class="pp-cards">{ch_cards}</div>

        <div class="kv-grid w-kv">
          <figure>{hd("pp-phone","Pro Play on a phone: Play like a pro, client logos and the four steps")}<figcaption class="tag">Play like a pro</figcaption></figure>
          <figure>{hd("pp-phone-2","Pro Play on a phone: the trainer, the orange band and the sign-up")}<figcaption class="tag">Trainer &amp; sign-up</figcaption></figure>
        </div>
      </div>
      <div class="pp-band">
        {wave("top",W_UP)}
        {hd("fig-armsup","","pp-band-fig")}
        <p><span>Cuando tengas un problema,</span><b>resuélvelo jugando</b><em>“When you have a problem, solve it by playing.” The landing’s line, and its whole argument.</em></p>
      </div>
    </section>

    <!-- =================== PROJECT 02 · CULTURA COLECTIVA =================== -->
    <section class="world cc" id="cultura">
      <div class="marq" aria-hidden="true"><div class="mq-r">{marq}</div><div class="mq-r rev">{marq}</div></div>
      {scribble("s1",S1)}
      <div class="fls" aria-hidden="true">
        {fl("pk-cross",4,9,7,-.3)}{fl("pk-sphere",86,7,6,-.5,"",.6)}{fl("pk-spring",90,36,8,-.2,"",.3)}{fl("pk-tube-a",2,40,5,-.45,"",1.1)}{fl("pk-dot",80,55,2.6,-.6,"",.9)}{fl("pk-tube-b",95,74,4,-.3,"",.5)}{fl("pk-cone",3,72,7,-.25,"",.2)}
      </div>
      <div class="wrap">
        <header class="w-open">
          <span class="w-tag">Project 02 · Mexico, 2023</span>
          <h2 class="cc-title" aria-label="Cultura Colectiva"><span class="m1">Cultura</span><span class="m2">Colectiva</span></h2>
          {hd("pk-flask","","cc-lean")}
          <p class="w-kick">Make 28 years feel young.</p>
          <div class="w-intro">
            <p>HDO works with brands that want more human, authentic workplaces. This was its own page: it had to carry that energy, its values and 28 years of experience without sounding like a consultancy brochure.</p>
          </div>
          <ul class="w-facts"><li><b>Leads</b>Attract them with high visual impact</li><li><b>Culture</b>Show it in an unconventional way</li><li><b>Expertise</b>Without looking institutional</li></ul>
        </header>

        {browser("cc","HDO · Cultura Colectiva landing","cc-full","The full Cultura Colectiva landing page, top to bottom",cc_notes,1400,7971)}

        <div class="w-sec">
          <h3 class="w-h"><span>Six</span> decisions</h3>
          <p class="w-p">Every 3D object in the landing marks one choice. Pick one to see where it lives on the page.</p>
        </div>
        <div class="cd" data-cursor="Pick one">
          <ol class="cd-list" aria-label="Design decisions">{dec_list}</ol>
          <div class="cd-view">
            <div class="cd-frame">{dec_imgs}</div>
            <div class="cd-notes" aria-live="polite">{dec_notes}</div>
          </div>
        </div>

        <div class="kv-grid w-kv">
          <figure>{hd("cc-phone","Cultura Colectiva on a phone: 28 years and the Cinépolis case")}<figcaption class="tag">28 years</figcaption></figure>
          <figure>{hd("cc-team","Cultura Colectiva desktop: the founder, the HDO marquee and the team")}<figcaption class="tag">The cast</figcaption></figure>
        </div>
      </div>
      {scribble("s2",S2)}
      {wave("bot",W_UP)}
    </section>

    <div class="wrap">
      <section class="chap" id="cast">
        <span class="mono">03 · The cast</span>
        <h2><span class="lm"><span>Modeled in</span></span><span class="lm"><span>Blender</span></span></h2>
        <p class="lead">The figures, spheres, button and lab glassware were modeled and rendered in Blender. Plain white figures keep the toy reference without copying a product, and the hats give each one a role.</p>
        <div class="cast">{cast}</div>
      </section>
    </div>

    <section class="finale" id="result">
      {wave("top",W_UP)}
      <div class="fls" aria-hidden="true">
        {fl("sphere-o1",8,16,4,-.3)}{fl("sphere-o2",22,62,2.4,-.5,"",.7)}{fl("pk-sphere",86,14,5,-.35,"",.3)}{fl("pk-cross",78,64,6,-.25,"",.9)}{fl("pk-dot",64,8,2.4,-.6,"",.5)}{fl("sphere-o1",36,6,2.6,-.4,"",1.1)}
      </div>
      <div class="wrap fin-in">
        <span class="w-tag">Result</span>
        <h2 class="fin-t"><span>Two moods.</span><span>One house.</span></h2>
        <ul class="fin-stats"><li><b>2</b>landings, one year apart</li><li><b>0</b>AI images: every 3D piece made in Blender</li><li><b>Live</b>both still online, with changes made after launch</li></ul>
        <div class="fin-figs">{hd("fig-g1","")}{hd("fig-g2","Three white figures celebrating")}{hd("fig-g3","")}</div>
      </div>
    </section>
  </div>
'''+next_block(pre,'Piensa en Jumbo','piensa-en-jumbo.html','<img src="../assets/img/jumbo/thumb.jpg" alt="" draggable="false">')+'''</main>
'''+scripts(pre)
    open(os.path.join(R,'proyectos','hdo-landings.html'),'w').write(page)
