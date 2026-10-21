/* Rodrigo López · Web Portfolio v2 — interacciones y animaciones */
(function(){
  'use strict';
  var root=document.documentElement;
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine=window.matchMedia('(pointer:fine)').matches;
  var G=window.gsap, ST=window.ScrollTrigger, hasG=!!(G&&ST)&&!reduce;
  var $=function(s,c){return (c||document).querySelector(s)}, $$=function(s,c){return [].slice.call((c||document).querySelectorAll(s))};

  /* ---------- Transición entre páginas ---------- */
  var arrived=false;
  try{arrived=sessionStorage.getItem('rl-leaving')==='1';sessionStorage.removeItem('rl-leaving')}catch(e){}
  if(arrived&&!reduce){root.classList.add('arriving');requestAnimationFrame(function(){requestAnimationFrame(function(){root.classList.add('arrived');setTimeout(function(){root.classList.remove('arriving','arrived')},900)})})}
  $$('a[data-transition]').forEach(function(a){
    a.addEventListener('click',function(e){
      if(reduce||e.metaKey||e.ctrlKey||e.shiftKey||a.target==='_blank')return;
      var href=a.getAttribute('href'); if(!href||href.charAt(0)==='#')return;
      e.preventDefault(); try{sessionStorage.setItem('rl-leaving','1')}catch(err){}
      root.classList.add('leaving'); setTimeout(function(){location.href=href},560);
    });
  });
  window.addEventListener('pageshow',function(e){if(e.persisted)root.classList.remove('leaving')});

  /* ---------- Imágenes: archivo local o copia en Behance ---------- */
  $$('img[data-fallback]').forEach(function(img){
    function swap(){var f=img.getAttribute('data-fallback');if(f){img.removeAttribute('data-fallback');img.src=f}else{img.style.opacity='0'}}
    img.addEventListener('error',swap); if(img.complete&&img.naturalWidth===0)swap();
  });

  /* ---------- Scroll suave ---------- */
  var lenis=null;
  if(hasG&&window.Lenis){
    lenis=new window.Lenis({lerp:.11,smoothWheel:true});
    lenis.on('scroll',ST.update);
    G.ticker.add(function(t){lenis.raf(t*1000)}); G.ticker.lagSmoothing(0);
    $$('a[href^="#"]').forEach(function(a){a.addEventListener('click',function(e){var id=a.getAttribute('href');if(id.length<2)return;var t=document.querySelector(id);if(!t)return;e.preventDefault();lenis.scrollTo(t,{offset:-10,duration:1.4})})});
  }
  if(hasG) G.registerPlugin(ST);

  /* ---------- Separar texto en letras (lente de peso + decodificación) ---------- */
  var lenses=[];
  $$('[data-lens]').forEach(function(h){
    var src=$('.lens-txt',h); if(!src)return;
    var lines=src.innerHTML.split(/<br\s*\/?>/i).map(function(l){return l.trim()});
    var frag=document.createDocumentFragment();
    lines.forEach(function(l){var ln=document.createElement('span');ln.className='ln';ln.setAttribute('aria-hidden','true');
      Array.from(l).forEach(function(c){var s=document.createElement('span');s.className='ch';s.textContent=c===' '?' ':c;s.dataset.c=s.textContent;ln.appendChild(s)});frag.appendChild(ln)});
    h.replaceChildren(frag);
    var chars=$$('.ch',h), BOLD=850, LIGHT=200, centers=[];
    function measure(){
      var shown=chars.map(function(c){return c.textContent});
      chars.forEach(function(c){c.textContent=c.dataset.c;c.style.width='';c.style.setProperty('--w',BOLD)});
      chars.forEach(function(c){c.style.width=c.getBoundingClientRect().width+'px'});
      chars.forEach(function(c,i){c.textContent=shown[i]});
      var hr=h.getBoundingClientRect();
      centers=chars.map(function(c){var r=c.getBoundingClientRect();return {x:r.left-hr.left+r.width/2,y:r.top-hr.top+r.height/2,w:r.width,h:r.height}});
    }
    function move(e){var hr=h.getBoundingClientRect(),x=e.clientX-hr.left,y=e.clientY-hr.top;
      centers.forEach(function(c,i){var dx=(x-c.x)/(c.w*2.6),dy=(y-c.y)/(c.h*.9),d=Math.sqrt(dx*dx+dy*dy),k=Math.max(0,1-d);k=k*k*(3-2*k);chars[i].style.setProperty('--w',Math.round(BOLD-(BOLD-LIGHT)*k))})}
    function out(){chars.forEach(function(c){c.style.setProperty('--w',BOLD)})}
    measure(); if(document.fonts&&document.fonts.ready)document.fonts.ready.then(function(){measure();ST&&ST.refresh&&ST.refresh()});
    window.addEventListener('resize',measure);
    h.addEventListener('pointermove',move);h.addEventListener('pointerdown',move);h.addEventListener('pointerleave',out);
    h.addEventListener('pointerup',function(e){if(e.pointerType!=='mouse')out()});h.addEventListener('pointercancel',out);
    lenses.push({el:h,chars:chars,measure:measure});
  });

  /* Decodificación: las letras visibles desde el inicio cambian por glifos y se resuelven */
  var GLYPHS='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#%&*+=/<>';
  function scramble(chars,delay){
    if(reduce)return;
    chars.forEach(function(c,i){
      var real=c.dataset.c; if(real===' ')return;
      var start=performance.now()+(delay||0)+i*38, dur=420+Math.random()*260;
      (function tick(now){
        if(now<start){c.textContent=GLYPHS[(Math.random()*GLYPHS.length)|0];return requestAnimationFrame(tick)}
        var t=(now-start)/dur; if(t>=1){c.textContent=real;return}
        c.textContent=Math.random()<t?real:GLYPHS[(Math.random()*GLYPHS.length)|0]; requestAnimationFrame(tick);
      })(performance.now());
    });
  }
  lenses.forEach(function(L){if(L.el.hasAttribute('data-scramble'))scramble(L.chars,120)});
  $$('[data-scramble-hover]').forEach(function(el){
    var txt=el.textContent; el.textContent=''; var cs=Array.from(txt).map(function(c){var s=document.createElement('span');s.textContent=c;s.dataset.c=c===' '?' ':c;if(c===' ')s.textContent=' ';el.appendChild(s);return s});
    el.setAttribute('aria-label',txt);
    var host=el.closest('a,button')||el; host.addEventListener('pointerenter',function(){scramble(cs,0)});
  });

  /* ---------- Cursor ---------- */
  var cur=$('#cursor'), lab=$('#cursorLabel');
  if(cur&&fine&&!reduce){
    root.classList.add('has-cursor');
    var x=-100,y=-100,cx=x,cy=y;
    window.addEventListener('pointermove',function(e){x=e.clientX;y=e.clientY});
    (function loop(){cx+=(x-cx)*.2;cy+=(y-cy)*.2;cur.style.transform='translate('+cx+'px,'+cy+'px)';requestAnimationFrame(loop)})();
    document.addEventListener('pointerover',function(e){
      var t=e.target, lbl=t.closest('[data-cursor]');
      if(lbl){cur.className='cursor big';lab.textContent=lbl.getAttribute('data-cursor')}
      else if(t.closest('.burger,[data-lens]')){cur.className='cursor'}
      else if(t.closest('a,button')){cur.className='cursor link'}
      else cur.className='cursor';
    });
    root.addEventListener('pointerleave',function(){cur.style.opacity='0'});
    root.addEventListener('pointerenter',function(){cur.style.opacity=''});
  }

  /* ---------- Botones magnéticos ---------- */
  if(fine&&!reduce)$$('[data-magnetic]').forEach(function(b){
    b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();var dx=e.clientX-r.left-r.width/2,dy=e.clientY-r.top-r.height/2;b.style.transform='translate('+dx*.25+'px,'+dy*.35+'px)'});
    b.addEventListener('pointerleave',function(){b.style.transition='transform .6s cubic-bezier(.34,1.56,.64,1)';b.style.transform='';setTimeout(function(){b.style.transition=''},600)});
  });

  /* ---------- Enlaces con trazo (6 variantes) ---------- */
  (function(){
    var V=['M2 12 C40 5 80 17 120 10 S178 7 198 11','M2 16 Q100 1 198 8','M3 8 C60 12 140 4 196 9 M12 16 C70 19 130 13 188 16','M2 12 C50 12 120 13 160 11 C190 9 193 2 179 4 C165 6 171 16 198 15','M2 10 L40 14 L80 8 L120 14 L160 8 L198 12','M2 9 C60 7 140 7 184 9 C196 10 197 17 185 18'], n=(Math.random()*V.length)|0;
    $$('a.hl').forEach(function(a){var p=$('.stroke path',a);if(!p)return;p.setAttribute('d',V[n%V.length]);
      function next(){n=(n+1)%V.length;p.style.transition='none';p.setAttribute('d',V[n]);p.getBoundingClientRect();p.style.transition=''}
      a.addEventListener('pointerleave',function(){setTimeout(next,520)});a.addEventListener('blur',function(){setTimeout(next,520)});});
  })();

  /* ---------- Burger y menú ---------- */
  (function(){
    var btn=$('#burger'), menu=$('#menu'); if(!btn||!menu)return;
    var P=$$('path',btn);
    function ln(y){return [4,y,7.33,y,10.67,y,14,y,17.33,y,20.67,y,24,y]}
    var k=4.97,S={lines:[ln(8),ln(14),ln(20)],
      circle:[[5,14,5,14-k,14-k,5,14,5,14+k,5,23,14-k,23,14],[14,14,14,14,14,14,14,14,14,14,14,14,14,14],[5,14,5,14+k,14-k,23,14,23,14+k,23,23,14+k,23,14]],
      x:[[6,6,8.67,8.67,11.33,11.33,14,14,16.67,16.67,19.33,19.33,22,22],[14,14,14,14,14,14,14,14,14,14,14,14,14,14],[6,22,8.67,19.33,11.33,16.67,14,14,16.67,11.33,19.33,8.67,22,6]]};
    var cur=S.lines.map(function(a){return a.slice()}),raf=0,DUR=620;
    function d(a){return 'M'+a[0]+' '+a[1]+'C'+a.slice(2,8).join(' ')+'C'+a.slice(8,14).join(' ')}
    function draw(){P.forEach(function(p,i){p.setAttribute('d',d(cur[i]))})}
    function ease(t){var c=1.45;return 1+(c+1)*Math.pow(t-1,3)+c*Math.pow(t-1,2)}
    function go(name){var to=S[name],from=cur.map(function(a){return a.slice()}),t0=performance.now();cancelAnimationFrame(raf);
      if(reduce){cur=to.map(function(a){return a.slice()});return draw()}
      (function step(now){var t=Math.min(1,(now-t0)/DUR),e=ease(t);
        cur=from.map(function(a,i){return a.map(function(v,j){var w=Math.sin((j/13)*Math.PI)*(1-t)*.9*(i===1?0:1);return v+(to[i][j]-v)*e+(j%2?w:0)})});
        draw(); if(t<1)raf=requestAnimationFrame(step)})(t0)}
    draw();
    var open=false,hover=false;
    function state(){go(open?'x':(hover?'circle':'lines'))}
    btn.addEventListener('pointerenter',function(e){if(e.pointerType==='mouse'){hover=true;state()}});
    btn.addEventListener('pointerleave',function(e){if(e.pointerType==='mouse'){hover=false;state()}});
    function setOpen(v){open=v;var r=btn.getBoundingClientRect();
      menu.style.setProperty('--ox',(r.left+r.width/2)+'px');menu.style.setProperty('--oy',(r.top+r.height/2)+'px');
      root.classList.toggle('menu-open',v); btn.setAttribute('aria-expanded',v); btn.setAttribute('aria-label',v?'Cerrar menú':'Abrir menú'); menu.setAttribute('aria-hidden',!v);
      if(lenis){v?lenis.stop():lenis.start()}
      if(v){lenses.forEach(function(L){if(menu.contains(L.el))L.measure()});setTimeout(function(){var a=$('a',menu);a&&a.focus({preventScroll:true})},400)} else btn.focus({preventScroll:true});
      state()}
    btn.addEventListener('click',function(){setOpen(!open)});
    $$('a',menu).forEach(function(a){a.addEventListener('click',function(){setOpen(false)})});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&open)setOpen(false)});
  })();

  /* ---------- Copiar correo ---------- */
  var copy=$('#copy'), mail=$('#mail');
  if(copy&&mail)copy.addEventListener('click',function(){
    var done=function(){copy.textContent='Copiado';setTimeout(function(){copy.textContent='Copiar correo'},1800)};
    var fb=function(){var r=document.createRange();r.selectNodeContents(mail);var s=getSelection();s.removeAllRanges();s.addRange(r);copy.textContent='Selecciona y copia'};
    try{navigator.clipboard.writeText(mail.textContent.trim()).then(done,fb)}catch(e){fb()}
  });

  /* ---------- Tarjeta del hero sigue al mouse ---------- */
  var hc=$('.hero-card');
  if(hc&&fine&&!reduce){
    var tx=0,ty=0,ax=0,ay=0;
    window.addEventListener('pointermove',function(e){tx=(e.clientX/innerWidth-.5);ty=(e.clientY/innerHeight-.5)});
    (function loop(){ax+=(tx-ax)*.06;ay+=(ty-ay)*.06;hc.style.translate=(ax*60)+'px '+(ay*40)+'px';hc.style.rotate=(8+ax*10)+'deg';requestAnimationFrame(loop)})();
  }

  /* ---------- Contadores (solo los que están fuera de pantalla al cargar) ---------- */
  function countUp(el){var txt=el.textContent,m=txt.match(/^([^\d]*)([\d.,]+)(.*)$/);if(!m)return;
    var target=parseFloat(m[2].replace(/,/g,'')),dec=(m[2].split('.')[1]||'').length,t0=null;
    (function step(t){if(!t0)t0=t;var k=Math.min(1,(t-t0)/1400),e=1-Math.pow(1-k,3);el.textContent=m[1]+(target*e).toFixed(dec)+m[3];if(k<1)requestAnimationFrame(step);else el.textContent=txt})(performance.now())}

  if(!hasG){return}

  /* ===================== Animaciones con scroll ===================== */
  var mm=G.matchMedia();
  var below=function(el){return el.getBoundingClientRect().top>innerHeight*.95};

  /* Elementos que suben al entrar (solo los que inician fuera de pantalla) */
  $$('[data-rise]').forEach(function(el){if(!below(el))return;
    G.from(el,{y:60,opacity:0,duration:1.1,ease:'expo.out',scrollTrigger:{trigger:el,start:'top 90%'}})});

  /* Imágenes que aparecen desenfocadas */
  $$('[data-blur]').forEach(function(el){if(!below(el))return;
    G.fromTo(el,{filter:'blur(24px)',scale:1.08,opacity:.4},{filter:'blur(0px)',scale:1,opacity:1,duration:1.4,ease:'power3.out',clearProps:'filter',scrollTrigger:{trigger:el,start:'top 85%'}})});

  /* Contadores */
  $$('[data-count]').forEach(function(el){if(!below(el))return;ST.create({trigger:el,start:'top 85%',once:true,onEnter:function(){countUp(el)}})});

  /* Palabras que se encienden con el scroll */
  $$('[data-words]').forEach(function(p){
    var walker=document.createTreeWalker(p,NodeFilter.SHOW_TEXT),nodes=[];while(walker.nextNode())nodes.push(walker.currentNode);
    nodes.forEach(function(n){var parts=n.textContent.split(/(\s+)/),f=document.createDocumentFragment();
      parts.forEach(function(w){if(!w)return;if(/^\s+$/.test(w)){f.appendChild(document.createTextNode(w));return}var s=document.createElement('span');s.className='w';s.textContent=w;f.appendChild(s)});n.parentNode.replaceChild(f,n)});
    G.fromTo($$('.w',p),{opacity:.14},{opacity:1,stagger:.08,ease:'none',scrollTrigger:{trigger:p,start:'top 80%',end:'bottom 45%',scrub:true}});
  });

  /* Reel: crece de tarjeta redondeada a pantalla completa */
  var reel=$('.reel');
  if(reel){
    G.fromTo(reel,{scale:.62,borderRadius:'48px'},{scale:1,borderRadius:'0px',ease:'none',scrollTrigger:{trigger:'.reel-wrap',start:'top 85%',end:'top 5%',scrub:true}});
    G.fromTo($('img',reel),{scale:1.25},{scale:1.02,ease:'none',scrollTrigger:{trigger:'.reel-wrap',start:'top bottom',end:'bottom top',scrub:true}});
  }
  var creel=$('.c-reel .media');
  if(creel){G.fromTo(creel,{scale:.84,borderRadius:'56px'},{scale:1,borderRadius:'28px',ease:'none',scrollTrigger:{trigger:creel,start:'top 95%',end:'top 15%',scrub:true}})}

  /* Hero: el título se separa al salir */
  var heroH=$('.hero h1');
  if(heroH){
    var lns=$$('.ln',heroH);
    if(lns[0])G.to(lns[0],{xPercent:-12,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}});
    if(lns[1])G.to(lns[1],{xPercent:10,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}});
    if(hc)G.to(hc,{yPercent:-80,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}});
  }

  /* Paneles apilados: el de atrás se encoge y oscurece */
  var panels=$$('.panel');
  panels.forEach(function(p,i){var nx=panels[i+1];if(!nx)return;
    G.to(p,{scale:.94,filter:'brightness(.8)',ease:'none',scrollTrigger:{trigger:nx,start:'top 70%',end:'top '+(84+(i+1)*22)+'px',scrub:true}})});

  /* Texto gigante que viaja + tarjeta inclinada que lo cruza */
  $$('.giant,.c-giant').forEach(function(g){
    var rows=$$('.giant-row',g), card=$('.giant-card',g);
    rows.forEach(function(r,i){G.fromTo(r,{xPercent:i%2?-30:5},{xPercent:i%2?5:-30,ease:'none',scrollTrigger:{trigger:g,start:'top bottom',end:'bottom top',scrub:true}})});
    if(card)G.fromTo(card,{xPercent:-160,rotate:-14},{xPercent:60,rotate:6,ease:'none',scrollTrigger:{trigger:g,start:'top bottom',end:'bottom top',scrub:true}});
  });

  /* Proyectos: recorrido horizontal fijado (escritorio) */
  mm.add('(min-width: 900px)',function(){
    var work=$('.work'), track=$('.work-track'), bar=$('.work-progress i'); if(!work||!track)return;
    work.classList.add('pinned');
    var dist=function(){return Math.max(0,track.scrollWidth-innerWidth+parseFloat(getComputedStyle(track).paddingRight))};
    var tw=G.to(track,{x:function(){return -dist()},ease:'none',scrollTrigger:{trigger:work,start:'top top',end:function(){return '+='+dist()},pin:true,scrub:.6,invalidateOnRefresh:true,anticipatePin:1,onUpdate:function(s){if(bar)bar.style.transform='scaleX('+s.progress+')'}}});
    $$('.proj .media',track).forEach(function(m){G.fromTo(m,{rotate:-2},{rotate:2,ease:'none',scrollTrigger:{trigger:m,containerAnimation:tw,start:'left right',end:'right left',scrub:true}})});
    return function(){work.classList.remove('pinned');G.set(track,{clearProps:'transform'})};
  });
  mm.add('(max-width: 899px)',function(){
    var track=$('.work-track'), bar=$('.work-progress i'); if(!track||!bar)return;
    var f=function(){var m=track.scrollWidth-track.clientWidth;bar.style.transform='scaleX('+(m>0?track.scrollLeft/m:1)+')'};
    track.addEventListener('scroll',f,{passive:true}); f();
    return function(){track.removeEventListener('scroll',f)};
  });

  /* Contacto: texto gigante que corre */
  $$('.contact-big,.next h2').forEach(function(b){G.fromTo(b,{xPercent:6},{xPercent:-18,ease:'none',scrollTrigger:{trigger:b,start:'top bottom',end:'bottom top',scrub:true}})});

  /* Pantallas del caso: entrada escalonada */
  $$('.screen').forEach(function(s){if(!below(s))return;
    G.from(s,{y:80,opacity:0,duration:1.1,ease:'expo.out',scrollTrigger:{trigger:s,start:'top 92%'}})});

  window.addEventListener('load',function(){ST.refresh()});
})();
