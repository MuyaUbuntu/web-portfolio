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

    # ---------- assembly instructions (Pro Play hero, piece by piece) ----------
    # regions in % of the hero: left, top, right, bottom (inset values)
    steps=[('Parts','Everything in the box: one figure, six spheres, one button and the type. All 3D pieces modeled in Blender.',None),
           ('Type','The lockup goes first: “Juega y conoce”, the outlined PRO PLAY and the Playmobil pro logo.','type'),
           ('Figure','A plain white figure leans on the title, so the toy is part of the headline.','fig'),
           ('Button','One orange, toy-like button. Nothing else on screen looks pressable.','btn'),
           ('Spheres','Six orange spheres repeat the button color across the page.','sph'),
           ('Done','Color, light and HDO’s nav. The hero, as it went live.','all')]
    REG={'type':(11,34,38,19),'fig':(2.5,42,83.5,15),'btn':(67,37,8,35),'all':(0,0,0,0)}
    SPH=[(8.3,28.8,2.1),(59.2,26,.7),(92.3,26.1,1.1),(62.6,78.5,1.45),(98.6,81.8,2.1),(12.1,98.2,2.05)]  # cx, cy (%), r (% of width)
    def clip(k):
        l,t,r,b=REG[k];return f'clip-path:inset({t}% {r}% {b}% {l}% round 1.2vw)'
    layers=''.join(f'<div class="asm-c" data-s="{k}" style="{clip(k)}">{hd("pp-hero","",lazy=True)}</div>' for k in ['type','fig','btn','all'])
    # spheres revealed one by one with circular masks sized relative to the stage
    sph_masks=''.join(f'<div class="asm-c sph" data-s="sph" style="--cx:{cx}%;--cy:{cy}%;--r:{r}">{hd("pp-hero","",lazy=True)}</div>' for cx,cy,r in SPH)
    # loose pieces: tray position (x,y,w in % of stage) -> target position
    pieces=[('fig-wave-a','fig',(70.5,70.5,3.6),(5,43.5,8.3)),
            ('btn','btn',(76.5,78,12),(67.6,47,23.6)),
            ]+[('sphere-o1','sph',(90+(i%3)*2.6,72+(i//3)*7,2.1),(cx-r*1.1,cy-r*1.1*1.778,r*2.2)) for i,(cx,cy,r) in enumerate(SPH)]
    def piece(n,s,t,g,i):
        return f'<span class="asm-p" data-s="{s}" style="--tx:{t[0]}%;--ty:{t[1]}%;--tw:{t[2]}%;--gx:{g[0]}%;--gy:{g[1]}%;--gw:{g[2]}%;--d:{i*70}ms">{hd(n,"")}</span>'
    ptray=''.join(piece(n,s,t,g,i) for i,(n,s,t,g) in enumerate(pieces))
    asteps=''.join(f'<button type="button" data-i="{i}" aria-pressed="{"true" if i==0 else "false"}"><b>{i:02d}</b>{t}</button>' for i,(t,d,k) in enumerate(steps))
    anotes=''.join(f'<p class="asm-note{" on" if i==0 else ""}">{d}</p>' for i,(t,d,k) in enumerate(steps))
    akeys=','.join((k or '') for t,d,k in steps)
    parts='<ul class="asm-parts" aria-label="Parts"><li><b>1×</b>figure</li><li><b>1×</b>button</li><li><b>6×</b>spheres</li><li><b>1×</b>type lockup</li></ul>'

    # ---------- the three challenges, solved by playing ----------
    challenges=[('01','tri-01','Break the prejudice that play isn’t serious work.','Proof comes first: the client logos sit right under “Play like a pro”, and the trainer’s credentials get a block of their own.'),
                ('02','tri-02','Make a hands-on workshop understood on one page.','The method becomes four cards, start playing, observe, extract insights, decide, followed by a video and the same call to action.'),
                ('03','tri-03','Speak PLAYMOBIL pro’s visual language.','Plain white figures modeled in Blender, outlined PRO PLAY type and a rounded 3D button that looks like a toy.')]
    targets=''.join(f'<button type="button" class="tg" data-i="{i}" aria-label="Reveal challenge {n}">{hd(img,"")}<span>{n}</span></button>' for i,(n,img,q,a) in enumerate(challenges))
    cards=''.join(f'<article class="tg-card" data-i="{i}"><span class="mono">Challenge {n}</span><h3>{q}</h3><div class="tg-ans"><p>{a}</p></div><p class="tg-lock mono">Drop a figure on {n} to unlock</p></article>' for i,(n,img,q,a) in enumerate(challenges))
    toys=''.join(f'<span class="toy" style="--w:{w}">{hd(n,"",lazy=False)}</span>' for n,w in [('fig-wave-b',.07),('fig-armsup',.068),('fig-tophat',.09),('fig-wizard',.058),('fig-mic',.072),('sphere-o1',.04),('sphere-o2',.032),('sphere-o1',.036),('briefcase',.06)])

    # ---------- the pink lab ----------
    lab=[('pk-flask','A lab, not an office','Glassware for a team in lab coats: culture treated as an experiment you can run.',(66,46,17)),
         ('pk-cross','Pink as the base','Pink runs the whole page, not just the accents, so a 28-year-old firm reads young.',(10,14,11)),
         ('pk-spring','Gestural type','Brush lettering for “Impulsa” and “Contáctanos”: the hand shows and the corporate tone breaks.',(82,16,14)),
         ('pk-cone','A form that asks for dreams','The last field asks “What’s your dream?”. A lead form that starts a conversation.',(26,52,15)),
         ('pk-sphere','28 years, told as a tale','Inflated 3D numbers and a pun: “our story lasts 28 years, the rest is just tales”.',(46,10,10)),
         ('pk-tube-a','Consultants as a cast','Color-blocked portraits and a marquee of HDO°, like a show’s lineup.',(8,70,10))]
    deco=[('pk-dot',(38,74,4)),('pk-tube-b',(90,72,7))]
    labs=''.join(f'<button type="button" class="lab-o" style="--x:{x}%;--y:{y}%;--w:{w};--d:{i*.7}s" data-i="{i}" aria-label="{t}">{hd(n,"")}</button>' for i,(n,t,d,(x,y,w)) in enumerate(lab))
    labs+=''.join(f'<span class="lab-o deco" style="--x:{x}%;--y:{y}%;--w:{w};--d:{i*.9+.3}s" aria-hidden="true">{hd(n,"")}</span>' for i,(n,(x,y,w)) in enumerate(deco))
    labn=''.join(f'<div class="lab-n{" on" if i==0 else ""}" data-i="{i}"><span class="mono">{i+1:02d} / {len(lab):02d}</span><h3>{t}</h3><p>{d}</p></div>' for i,(n,t,d,p) in enumerate(lab))

    marq=''.join('<span>CONSULTORES HDO°</span><span class="o">CONSULTORES HDO°</span>' for _ in range(6))
    cast=''.join(f'<figure class="cast-f">{hd(n,a)}<figcaption class="mono">{c}</figcaption></figure>' for n,a,c in [
        ('fig-wave-a','White figure waving, Pro Play hero','Hero'),('fig-armsup','White figure with arms up','Facilitator'),('fig-wizard','Figure with a wizard hat and wand','Footer'),
        ('fig-tophat','Figure with a top hat and briefcase','Presentation'),('fig-bowler','Figure with a bowler hat, waving','Bowler'),('fig-mic','Figure with a bowler hat and a red microphone','Bowler & mic')])

    page=head('One House, Two Moods · HDO landings · Rodrigo López','Case study: two landing pages for HDO Culture & Change, Pro Play (2024) and Cultura Colectiva (2023). UX/UI, branding, art direction and 3D in Blender.',pre)+nav(pre,False)+f'''<main class="hdo">
  <section class="wrap c-hero">
    <div class="c-head"><div class="c-l">
      <a class="back" href="{pre}#work" data-go>← All work</a>
      <div class="c-client"><span class="tag k">HDO Culture &amp; Change · HD*</span><span class="tag">Web · 2023–2024</span></div>
      <h1 class="c-title" aria-label="One house, two moods"><span aria-hidden="true">{word("One")} {word("house,")} {word("two","hlw")} {word("moods","hlw")}</span></h1>
      </div><div class="c-r">
      <p class="c-lead">Two landing pages for HDO, a culture and change consultancy, one year apart. Same logo, nav and footer; opposite moods. Pro Play had to make a toy look like a serious business tool. Cultura Colectiva had to make 28 years of consulting feel young.</p>
      <div class="tags c-tags"><span class="tag t">UX/UI</span><span class="tag p">Branding</span><span class="tag b">3D</span><span class="tool t-bl" title="Blender">Bl</span></div>
      <dl class="facts"><div><dt class="mono">Role</dt><dd>UX/UI, branding, art direction, 3D</dd></div><div><dt class="mono">Scope</dt><dd>Design only · built by HDO</dd></div><div><dt class="mono">Years</dt><dd>2023 · 2024</dd></div><div class="win"><dt class="mono">Result</dt><dd>Both still live, with later changes</dd></div></dl>
    </div></div>
    <div class="c-cover hdo-split">
      <a class="hs pp" href="#pro-play" aria-label="Go to Pro Play">{hd("pp-hero","Pro Play landing hero: a white figure leaning on the title and an orange Regístrate button",lazy=False)}<span class="hs-l"><b>Pro Play</b><small>Bogotá · 2024</small></span></a>
      <a class="hs cc" href="#cultura" aria-label="Go to Cultura Colectiva">{hd("cc-hero","Cultura Colectiva landing hero: brush lettering over pink and the founder in a lab coat",lazy=False)}<span class="hs-l"><b>Cultura Colectiva</b><small>Mexico · 2023</small></span></a>
      {hd("fig-wave-b","","hs-fig",lazy=False)}{hd("pk-sphere","","hs-sph",lazy=False)}
    </div>
  </section>

  <div class="hdo-ch">
    <aside class="toc" aria-label="Chapters">
      <ol><li><a href="#house">The house</a></li><li><a href="#pro-play">Pro Play</a></li><li><a href="#cultura">Cultura</a></li><li><a href="#cast">The cast</a></li><li><a href="#result">Result</a></li></ol>
      <div class="bar"><i></i></div>
    </aside>

    <div class="wrap">
      <section class="chap" id="house">
        <span class="mono">01 · The house</span>
        <h2><span class="lm"><span>One house,</span></span><span class="lm"><span>two personalities</span></span></h2>
        <p class="lead">HDO helps companies build more human cultures, with workshops, diagnostics and consulting. Each landing sells one thing to a different crowd, so each gets its own mood inside the same frame.</p>
        <div class="house">
          <figure class="house-f">{hd("pp-foot","Pro Play footer: HDO logo and contact details in orange")}<figcaption><span class="tag k">Pro Play</span><span>Orange</span></figcaption></figure>
          <figure class="house-f">{hd("cc-foot","Cultura Colectiva footer: the same HDO logo and contact details in pink")}<figcaption><span class="tag k">Cultura</span><span>Pink</span></figcaption></figure>
        </div>
        <p class="muted mono" style="margin-top:.9rem">Same footer, same nav, same logo. Only the accent changes.</p>
      </section>
    </div>

    <section class="band pp" id="pro-play">
      <div class="wrap">
        <div class="band-h">
          <div><span class="mono">02 · Pro Play · Bogotá, 2024</span>
          <h2><span class="lm"><span>Make play look</span></span><span class="lm"><span class="hl">like serious work</span></span></h2></div>
          <p class="lead">Pro.Play is a method created by Juan Prego and endorsed by PLAYMOBIL pro: teams model real problems with figures to find new answers. HD* brought a free, in-person workshop to Bogotá, led by Jaime Lastra, one of the few certified trainers in Latin America. The challenge: sell the professional value behind a toy.</p>
        </div>
        {browser("pp","HDO · Pro Play landing","pp-full","The full Pro Play landing page, top to bottom",pp_notes,1400,5895)}

        <h3 class="sub band-sub">Assembly instructions</h3>
        <p class="muted band-p">Like the booklet in a Playmobil box: the hero, rebuilt piece by piece from the real renders.</p>
        <div class="asm" data-keys="{akeys}">
          <div class="asm-stage" aria-label="The Pro Play hero, assembled step by step">
            {hd("pp-hero-line","Line drawing of the Pro Play hero, like an instruction sheet","asm-line")}
            {layers}{sph_masks}
            <div class="asm-box" aria-hidden="true"><span>Parts box</span></div><div class="asm-tray" aria-hidden="true">{ptray}</div>
            <span class="asm-num" aria-hidden="true">00</span>
          </div>
          <div class="asm-side">
            {parts}
            <div class="asm-steps" role="group" aria-label="Assembly steps">{asteps}</div>
            <div class="asm-notes" aria-live="polite">{anotes}</div>
          </div>
        </div>

        <h3 class="sub band-sub">Solve it by playing</h3>
        <p class="muted band-p">The landing’s line was “when you have a problem, solve it by playing”. So here are its three challenges: drop a figure on each number to see how the design answered it.</p>
        <div class="toss" data-cursor="Grab one">
          <div class="toss-stage" aria-hidden="true">{toys}</div>
          <div class="toss-floor">{targets}</div>
          <button type="button" class="toss-reset">Drop them again</button>
        </div>
        <div class="tg-cards">{cards}</div>

        <div class="kv-grid band-kv">
          <figure>{hd("pp-phone","Pro Play landing on a phone: the four steps of the method")}<figcaption class="tag">How it works</figcaption></figure>
          <figure>{hd("pp-phone-2","Pro Play landing on a phone: the orange band and the sign-up")}<figcaption class="tag">Solve it by playing</figcaption></figure>
        </div>
      </div>
    </section>

    <div class="marq" aria-hidden="true"><div class="mq-r">{marq}</div><div class="mq-r rev">{marq}</div></div>

    <section class="band cc" id="cultura">
      <div class="wrap">
        <div class="band-h">
          <div><span class="mono">03 · Cultura Colectiva · 2023</span>
          <h2><span class="lm"><span>Make 28 years</span></span><span class="lm"><span class="hl">feel young</span></span></h2></div>
          <p class="lead">HDO works with brands that want more human, authentic workplaces. This page had to carry that energy, its values and 28 years of experience, without sounding like a consultancy brochure.</p>
        </div>
        <div class="needs">
          <div><b>Leads</b><p>Attract leads with a page of high visual impact.</p></div>
          <div><b>Culture</b><p>Communicate a positive culture in an unconventional way.</p></div>
          <div><b>Expertise</b><p>Show experience without looking institutional or boring.</p></div>
        </div>
        {browser("cc","HDO · Cultura Colectiva landing","cc-full","The full Cultura Colectiva landing page, top to bottom",cc_notes,1400,7971)}

        <h3 class="sub band-sub">The pink lab</h3>
        <p class="muted band-p">Every object floating in the landing is a 3D piece. Here, each one holds a design decision: touch them.</p>
        <div class="lab-wrap">
          <div class="lab-stage" data-cursor="Touch one">{labs}</div>
          <div class="lab-notes" aria-live="polite">{labn}</div>
        </div>

        <div class="kv-grid band-kv">
          <figure>{hd("cc-phone","Cultura Colectiva on a phone: 28 years and the Cinépolis case")}<figcaption class="tag">28 years</figcaption></figure>
          <figure>{hd("cc-team","Cultura Colectiva desktop: the founder, the HDO marquee and the team")}<figcaption class="tag">The cast</figcaption></figure>
        </div>
      </div>
    </section>

    <div class="wrap">
      <section class="chap" id="cast">
        <span class="mono">04 · The cast</span>
        <h2><span class="lm"><span>Modeled in</span></span><span class="lm"><span>Blender, no AI</span></span></h2>
        <p class="lead">The figures, spheres, button, trophy and lab glassware were modeled and rendered in Blender. Plain white figures keep the toy reference without copying a product, and the hats give each one a role.</p>
        <div class="cast" data-cursor="Drag">{cast}</div>
      </section>

      <section class="chap" id="result">
        <span class="mono">05 · Result</span>
        <h2><span class="lm"><span>Two moods,</span></span><span class="lm"><span>still on air</span></span></h2>
        <div class="quotes three">
          <div class="quote c"><b>2 landings</b><p>Cultura Colectiva in 2023 and Pro Play in 2024, inside the same HDO frame.</p></div>
          <div class="quote b"><b>Blender</b><p>Every 3D piece modeled and rendered by hand. No AI.</p></div>
          <div class="quote a"><b>Live</b><p>Both pages are still online, with changes made after launch.</p></div>
        </div>
        <figure class="hdo-end">{hd("fig-g1","")}{hd("fig-g2","White figure with arms up")}{hd("fig-g3","")}</figure>
      </section>
    </div>
  </div>
'''+next_block(pre,'AI Showroom','ai-showroom.html','<img src="../assets/img/showroom/didi.jpg" alt="" draggable="false">')+'''</main>
'''+scripts(pre)
    open(os.path.join(R,'proyectos','hdo-landings.html'),'w').write(page)
