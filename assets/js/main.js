/* Rodrigo López · Web Portfolio v3 — interacciones y animaciones */
(function(){
  'use strict';
  var root=document.documentElement;
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine=matchMedia('(pointer:fine)').matches;
  var G=window.gsap, ST=window.ScrollTrigger, hasG=!!(G&&ST)&&!reduce;
  var $=function(s,c){return (c||document).querySelector(s)}, $$=function(s,c){return [].slice.call((c||document).querySelectorAll(s))};
  var below=function(el){return el.getBoundingClientRect().top>innerHeight*.92};

  /* ---------- Transición: círculo que crece desde el clic ---------- */
  var blot=$('.blot'), arrived=false;
  try{arrived=sessionStorage.getItem('rl-go')==='1';sessionStorage.removeItem('rl-go')}catch(e){}
  if(arrived&&!reduce){root.classList.add('arriving');requestAnimationFrame(function(){requestAnimationFrame(function(){root.classList.add('arrived');setTimeout(function(){root.classList.remove('arriving','arrived')},900)})})}
  $$('a[data-go]').forEach(function(a){a.addEventListener('click',function(e){
    if(reduce||e.metaKey||e.ctrlKey||e.shiftKey)return; var href=a.getAttribute('href'); if(!href||href.charAt(0)==='#')return;
    e.preventDefault(); if(blot){blot.style.setProperty('--bx',e.clientX+'px');blot.style.setProperty('--by',e.clientY+'px')}
    try{sessionStorage.setItem('rl-go','1')}catch(err){} root.classList.add('leaving'); setTimeout(function(){location.href=href},620);
  })});
  addEventListener('pageshow',function(e){if(e.persisted)root.classList.remove('leaving')});

  /* ---------- Imágenes: archivo local o copia publicada en Behance ---------- */
  $$('img[data-fallback]').forEach(function(img){
    function swap(){var f=img.getAttribute('data-fallback');if(f){img.removeAttribute('data-fallback');img.src=f}else img.style.opacity='0'}
    img.addEventListener('error',swap); if(img.complete&&img.naturalWidth===0)swap();
  });

  /* ---------- Scroll suave ---------- */
  var lenis=null;
  if(hasG){G.registerPlugin(ST)}
  if(hasG&&window.Lenis){
    lenis=new window.Lenis({lerp:.1,smoothWheel:true});
    lenis.on('scroll',ST.update); G.ticker.add(function(t){lenis.raf(t*1000)}); G.ticker.lagSmoothing(0);
  }
  $$('a[href^="#"]').forEach(function(a){a.addEventListener('click',function(e){var id=a.getAttribute('href');if(id.length<2)return;var t=$(id);if(!t)return;e.preventDefault();
    if(lenis)lenis.scrollTo(t,{offset:-20,duration:1.3});else t.scrollIntoView({behavior:reduce?'auto':'smooth'})})});

  /* ---------- Cursor-etiqueta ---------- */
  var ctag=$('#ctag');
  if(ctag&&fine&&!reduce){
    var x=0,y=0,cx=0,cy=0;
    addEventListener('pointermove',function(e){x=e.clientX;y=e.clientY});
    (function loop(){cx+=(x-cx)*.22;cy+=(y-cy)*.22;ctag.style.transform='translate('+(cx+14)+'px,'+(cy+14)+'px)';requestAnimationFrame(loop)})();
    document.addEventListener('pointerover',function(e){var t=e.target.closest('[data-cursor]');if(t){ctag.textContent=t.getAttribute('data-cursor');ctag.classList.add('on')}else ctag.classList.remove('on')});
  }

  /* ---------- Navegación: píldora que sigue al enlace ---------- */
  (function(){
    var wrap=$('.nav-links'), pill=$('.nav-pill'); if(!wrap||!pill)return;
    var links=$$('a',wrap), current=null;
    function moveTo(a){if(!a){pill.style.opacity='0';links.forEach(function(l){l.classList.remove('on')});return}
      pill.style.opacity='1';pill.style.width=a.offsetWidth+'px';pill.style.transform='translateX('+a.offsetLeft+'px)';links.forEach(function(l){l.classList.toggle('on',l===a)})}
    links.forEach(function(a){a.addEventListener('pointerenter',function(){moveTo(a)})});
    wrap.addEventListener('pointerleave',function(){moveTo(current)});
    var secs=links.map(function(a){return $(a.getAttribute('href').replace(/^.*#/,'#'))}).filter(Boolean);
    if(secs.length&&'IntersectionObserver' in window){
      var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){current=links.find(function(l){return l.getAttribute('href').replace(/^.*#/,'#')==='#'+en.target.id})||null;moveTo(current)}})},{rootMargin:'-45% 0px -50% 0px'});
      secs.forEach(function(s){io.observe(s)});
      var top=new IntersectionObserver(function(es){if(es[0].isIntersecting){current=null;moveTo(null)}},{rootMargin:'0px 0px -60% 0px'});
      var h=$('.hero'); if(h)top.observe(h);
    }
  })();

  /* ---------- Arrastrar (stickers y polaroids) ---------- */
  function draggable(el){
    var sx=0,sy=0,ox=0,oy=0,tx=0,ty=0,lx=0,vx=0,rot=0,id=null;
    el.addEventListener('pointerdown',function(e){id=e.pointerId;el.setPointerCapture(id);sx=e.clientX;sy=e.clientY;ox=tx;oy=ty;lx=e.clientX;el.classList.add('dragging');el.style.transition='none'});
    el.addEventListener('pointermove',function(e){if(e.pointerId!==id)return;tx=ox+e.clientX-sx;ty=oy+e.clientY-sy;vx=e.clientX-lx;lx=e.clientX;rot=Math.max(-18,Math.min(18,vx*1.4));
      el.style.transform='translate('+tx+'px,'+ty+'px) rotate('+rot+'deg)'});
    function up(e){if(e.pointerId!==id)return;id=null;el.classList.remove('dragging');el.style.transition='transform .7s cubic-bezier(.34,1.56,.64,1)';el.style.transform='translate('+tx+'px,'+ty+'px) rotate(0deg)'}
    el.addEventListener('pointerup',up);el.addEventListener('pointercancel',up);
    el.addEventListener('dblclick',function(){tx=ty=0;el.style.transition='transform .8s cubic-bezier(.34,1.56,.64,1)';el.style.transform=''});
  }
  if(!reduce)$$('.stk,.pola').forEach(draggable);

  /* ---------- Retícula de puntos que reacciona al cursor ---------- */
  (function(){
    var cv=$('.dots'); if(!cv||reduce)return; var ctx=cv.getContext('2d'), host=cv.parentElement, W=0,H=0,dpr=Math.min(2,devicePixelRatio||1),mx=-999,my=-999,vis=true,ink='#1B1410',tom='#FF4B2B';
    function size(){var r=host.getBoundingClientRect();W=r.width;H=r.height;cv.width=W*dpr;cv.height=H*dpr;ink=getComputedStyle(root).getPropertyValue('--ink').trim()||ink}
    size(); addEventListener('resize',size);
    host.addEventListener('pointermove',function(e){var r=host.getBoundingClientRect();mx=e.clientX-r.left;my=e.clientY-r.top});
    host.addEventListener('pointerleave',function(){mx=my=-999});
    if('IntersectionObserver' in window)new IntersectionObserver(function(es){vis=es[0].isIntersecting}).observe(host);
    var GAP=28,t0=performance.now();
    (function draw(now){requestAnimationFrame(draw);if(!vis)return;
      ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,W,H);var t=(now-t0)/1000;
      for(var x=GAP/2;x<W;x+=GAP)for(var y=GAP/2;y<H;y+=GAP){
        var dx=x-mx,dy=y-my,d=Math.sqrt(dx*dx+dy*dy),k=Math.max(0,1-d/160);
        var wave=.5+.5*Math.sin(t*1.2+x*.012+y*.01);
        var r=1+wave*.5+k*5;ctx.globalAlpha=.16+k*.8;ctx.fillStyle=k>.05?tom:ink;
        ctx.beginPath();ctx.arc(x-dx*k*.18,y-dy*k*.18,r,0,6.283);ctx.fill()}
      ctx.globalAlpha=1})(t0);
  })();

  /* ---------- Servicios: acordeón ---------- */
  $$('.svc li').forEach(function(li,i,all){var b=$('button',li);b.setAttribute('aria-expanded',li.classList.contains('open'));
    b.addEventListener('click',function(){var o=!li.classList.contains('open');all.forEach(function(x){x.classList.remove('open');$('button',x).setAttribute('aria-expanded','false')});if(o){li.classList.add('open');b.setAttribute('aria-expanded','true')}setTimeout(function(){ST&&ST.refresh()},650)})});

  /* ---------- Odómetro ---------- */
  var odos=$$('.odo').map(function(el){
    var txt=el.getAttribute('data-v');el.setAttribute('aria-label',txt);el.textContent='';
    var cols=Array.from(txt).map(function(ch){var c=document.createElement('span');c.className='col';c.setAttribute('aria-hidden','true');
      if(/\d/.test(ch)){for(var n=0;n<=9;n++){var s=document.createElement('span');s.textContent=n;c.appendChild(s)}c.dataset.d=ch}else{var s2=document.createElement('span');s2.textContent=ch;c.appendChild(s2)}
      el.appendChild(c);return c});
    return {el:el,roll:function(instant){cols.forEach(function(c,i){if(c.dataset.d==null)return;if(instant)c.style.transition='none';else c.style.transitionDelay=(i*.08)+'s';c.style.transform='translateY(-'+(c.dataset.d*1.15)+'em)'})}};
  });
  if(reduce||!('IntersectionObserver' in window))odos.forEach(function(o){o.roll(true)});
  else{var oio=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){odos.forEach(function(o){if(o.el===en.target)o.roll(false)});oio.unobserve(en.target)}})},{threshold:.6});
    odos.forEach(function(o){if(below(o.el))oio.observe(o.el);else o.roll(true)})}

  /* ---------- Botón que persigue al cursor (contacto) ---------- */
  var blob=$('.blob');
  if(blob&&fine&&!reduce){var area=blob.closest('.contact'),bx=0,by=0,ax=0,ay=0;
    area.addEventListener('pointermove',function(e){var r=blob.getBoundingClientRect();var dx=e.clientX-(r.left+r.width/2-ax),dy=e.clientY-(r.top+r.height/2-ay);var d=Math.sqrt(dx*dx+dy*dy);var k=Math.max(0,1-d/420);bx=dx*k*.45;by=dy*k*.45});
    area.addEventListener('pointerleave',function(){bx=by=0});
    (function loop(){ax+=(bx-ax)*.12;ay+=(by-ay)*.12;blob.style.transform='translate('+ax+'px,'+ay+'px)';requestAnimationFrame(loop)})()}
  var mail=$('#mail');
  if(blob&&mail){var label=blob.innerHTML;blob.addEventListener('click',function(){
    var ok=function(){blob.innerHTML='¡Copiado!';setTimeout(function(){blob.innerHTML=label},1600)};
    var fb=function(){var r=document.createRange();r.selectNodeContents(mail);var s=getSelection();s.removeAllRanges();s.addRange(r);blob.innerHTML='Selecciona<br>y copia'};
    try{navigator.clipboard.writeText(mail.textContent.trim()).then(ok,fb)}catch(e){fb()}})}

  /* ---------- Galería arrastrable ---------- */
  $$('.drag').forEach(function(d){
    var tr=$('.drag-track',d),bar=$('.drag-ui .bar i',d),prev=$('[data-prev]',d),next=$('[data-next]',d);
    function upd(){var m=tr.scrollWidth-tr.clientWidth;if(bar)bar.style.transform='scaleX('+(m>0?Math.max(.06,tr.scrollLeft/m):1)+')'}
    tr.addEventListener('scroll',upd,{passive:true});upd();
    var step=function(){var s=tr.querySelector('.shot');return s?s.offsetWidth+14:400};
    prev&&prev.addEventListener('click',function(){tr.scrollBy({left:-step(),behavior:reduce?'auto':'smooth'})});
    next&&next.addEventListener('click',function(){tr.scrollBy({left:step(),behavior:reduce?'auto':'smooth'})});
    tr.addEventListener('keydown',function(e){if(e.key==='ArrowRight')tr.scrollBy({left:step()});if(e.key==='ArrowLeft')tr.scrollBy({left:-step()})});
    if(!fine)return; var down=false,sx=0,sl=0,v=0,lx=0,moved=false;
    tr.addEventListener('pointerdown',function(e){if(e.pointerType!=='mouse')return;down=true;moved=false;sx=lx=e.clientX;sl=tr.scrollLeft;v=0});
    addEventListener('pointermove',function(e){if(!down)return;var dx=e.clientX-sx;if(Math.abs(dx)>4&&!moved){moved=true;tr.classList.add('grab')}v=e.clientX-lx;lx=e.clientX;tr.scrollLeft=sl-dx});
    addEventListener('pointerup',function(){if(!down)return;down=false;tr.classList.remove('grab');if(!moved)return;var vel=-v*18;(function glide(){if(Math.abs(vel)<.5)return;tr.scrollLeft+=vel;vel*=.92;requestAnimationFrame(glide)})()});
  });

  /* ---------- Índice de capítulos ---------- */
  (function(){var toc=$('.toc');if(!toc)return;var links=$$('a',toc),bar=$('.bar i',toc),chs=links.map(function(a){return $(a.getAttribute('href'))});
    function upd(){var mid=innerHeight*.4,on=0;chs.forEach(function(c,i){if(c&&c.getBoundingClientRect().top<mid)on=i});links.forEach(function(a,i){a.classList.toggle('on',i===on)});
      var wrap=toc.parentElement.getBoundingClientRect(),p=Math.min(1,Math.max(0,(mid-wrap.top)/wrap.height));if(bar)bar.style.transform='scaleX('+p+')'}
    addEventListener('scroll',upd,{passive:true});upd()})();

  if(!hasG)return;
  /* ===================== Animaciones con GSAP ===================== */

  /* Stickers: caen con rebote al cargar (siempre visibles) */
  var stks=$$('.stk');
  if(stks.length)G.from(stks,{y:-70,rotation:function(i){return (i%2?1:-1)*(10+i*3)},scale:.85,duration:1.1,ease:'elastic.out(1,.55)',stagger:.08,delay:.1,clearProps:'transform'});

  /* Cintas: avanzan solas y aceleran con la velocidad del scroll */
  $$('.rail').forEach(function(r,i){
    var dir=r.closest('.alt')?1:-1,x=0,boost=0,w=r.scrollWidth/2;
    addEventListener('resize',function(){w=r.scrollWidth/2});
    ST.create({trigger:r,start:'top bottom',end:'bottom top',onUpdate:function(s){boost=s.getVelocity()/300}});
    G.ticker.add(function(){var sp=(1+Math.min(12,Math.abs(boost)))*(boost<0?-1:1);x+=dir*sp*.6;boost*=.92;if(x<-w)x+=w;if(x>0)x-=w;r.style.transform='translate3d('+x+'px,0,0) skewX('+(-boost*1.2)+'deg)'});
  });

  /* Títulos: líneas que suben desde una máscara */
  $$('.lm > span').forEach(function(s){if(!below(s))return;G.from(s,{yPercent:110,rotation:4,duration:1.1,ease:'expo.out',scrollTrigger:{trigger:s,start:'top 92%'}})});
  $$('[data-pop]').forEach(function(el){if(!below(el))return;G.from(el,{y:60,scale:.94,opacity:0,duration:1,ease:'back.out(1.6)',scrollTrigger:{trigger:el,start:'top 90%'}})});

  /* Tarjetas: paralaje de la imagen y giro 3D con el cursor */
  $$('.card').forEach(function(c){var ph=$('.frame .ph',c),fr=$('.frame',c);
    if(ph)G.fromTo(ph,{yPercent:-6},{yPercent:6,ease:'none',scrollTrigger:{trigger:c,start:'top bottom',end:'bottom top',scrub:true}});
    if(below(c))G.from(fr,{y:120,rotation:c.matches(':nth-child(even)')?4:-4,duration:1.2,ease:'expo.out',scrollTrigger:{trigger:c,start:'top 92%'}});
    if(fine){var qx=G.quickTo(fr,'rotationY',{duration:.6,ease:'power3'}),qy=G.quickTo(fr,'rotationX',{duration:.6,ease:'power3'});G.set(fr,{transformPerspective:900});
      c.addEventListener('pointermove',function(e){var r=fr.getBoundingClientRect();qx(((e.clientX-r.left)/r.width-.5)*10);qy(-((e.clientY-r.top)/r.height-.5)*10)});
      c.addEventListener('pointerleave',function(){qx(0);qy(0)})}
  });

  /* Polaroids: entran girando */
  $$('.polas').forEach(function(p){if(!below(p))return;G.from($$('.pola,.bubble',p),{y:140,rotation:function(i){return i?18:-18},opacity:0,duration:1.2,ease:'back.out(1.4)',stagger:.12,scrollTrigger:{trigger:p,start:'top 85%'}})});

  /* Contacto: el título se separa con el scroll */
  $$('.contact h2 .lm > span').forEach(function(s,i){G.fromTo(s,{xPercent:i%2?12:-12},{xPercent:0,ease:'none',scrollTrigger:{trigger:'.contact',start:'top bottom',end:'top 30%',scrub:true}})});

  /* Caso: letras del título con rebote */
  var lts=$$('.c-title .lt');
  if(lts.length)G.from(lts,{yPercent:-40,rotation:function(){return G.utils.random(-25,25)},duration:1,ease:'elastic.out(1,.6)',stagger:.035,delay:.15,clearProps:'transform'});

  /* Portada: se destapa con el scroll */
  var cov=$('.cover .ph');
  if(cov)G.fromTo(cov,{clipPath:'inset(7% 9% 7% 9% round 48px)'},{clipPath:'inset(0% 0% 0% 0% round 22px)',ease:'none',scrollTrigger:{trigger:cov,start:'top 90%',end:'top 20%',scrub:true}});

  /* Imágenes que se barren desde abajo */
  $$('.wipe').forEach(function(w){if(!below(w))return;G.fromTo(w,{clipPath:'inset(100% 0% 0% 0% round 22px)'},{clipPath:'inset(0% 0% 0% 0% round 22px)',duration:1.3,ease:'expo.inOut',scrollTrigger:{trigger:w,start:'top 85%'}});
    G.from($('img',w),{scale:1.25,duration:1.6,ease:'expo.out',scrollTrigger:{trigger:w,start:'top 85%'}})});

  /* Tarjetas del reto */
  $$('.quote').forEach(function(q,i){if(!below(q))return;G.from(q,{y:100,rotation:i?12:-12,opacity:0,duration:1.1,ease:'back.out(1.5)',scrollTrigger:{trigger:q,start:'top 90%'}})});

  addEventListener('load',function(){ST.refresh()});
  if(document.fonts&&document.fonts.ready)document.fonts.ready.then(function(){ST.refresh()});
})();

/* ---------- Zona para dibujar: el cursor traza, el título queda fijo ---------- */
(function(){
  var sec=document.querySelector('.play'); if(!sec)return;
  var cv=sec.querySelector('.play-canvas'), ctx=cv.getContext('2d'), pen=sec.querySelector('.pen'), btn=sec.querySelector('.reset');
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var COLORS=['#FF4B2B','#FFB3D1','#FFD84D','#9FD3FF','#1B1410','#3DDC97'];
  var dpr=Math.min(2,window.devicePixelRatio||1), W=0, H=0, last=null, mid=null, ci=0, travel=0, drawn=false;
  function size(){
    var r=sec.getBoundingClientRect(), nw=Math.round(r.width), nh=Math.round(r.height);
    if(nw===W&&nh===H)return;
    var keep=null; if(W&&H&&drawn){keep=document.createElement('canvas');keep.width=cv.width;keep.height=cv.height;keep.getContext('2d').drawImage(cv,0,0)}
    W=nw;H=nh;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);ctx.lineCap='round';ctx.lineJoin='round';
    if(keep)ctx.drawImage(keep,0,0,keep.width/dpr,keep.height/dpr);
  }
  size(); addEventListener('resize',size);
  function color(){return COLORS[ci%COLORS.length]}
  function setPen(){sec.style.setProperty('--pen',color())}
  setPen();
  function pos(e){var r=cv.getBoundingClientRect();return {x:e.clientX-r.left,y:e.clientY-r.top,t:performance.now()}}
  function firstStroke(){if(drawn)return;drawn=true;sec.classList.add('drawn');btn.hidden=false;btn.classList.remove('out');btn.classList.add('wiggle')}
  function move(e){
    var p=pos(e);
    if(pen)pen.style.transform='translate('+p.x+'px,'+p.y+'px)';
    if(e.pointerType!=='mouse'&&e.buttons===0&&e.type!=='pointerdown')return;
    if(!last){last=p;mid=p;return}
    var dx=p.x-last.x,dy=p.y-last.y,d=Math.sqrt(dx*dx+dy*dy); if(d<1.5)return;
    if(d>140){last=p;mid=p;return} /* salto grande: empieza un trazo nuevo */
    var dt=Math.max(1,p.t-last.t), speed=d/dt;
    var w=Math.max(3,Math.min(14,14-speed*5));
    var m={x:(last.x+p.x)/2,y:(last.y+p.y)/2};
    ctx.strokeStyle=color(); ctx.lineWidth=w;
    ctx.beginPath(); ctx.moveTo(mid.x,mid.y); ctx.quadraticCurveTo(last.x,last.y,m.x,m.y); ctx.stroke();
    mid=m; last=p; travel+=d;
    if(travel>420){travel=0;ci++;setPen()}
    firstStroke();
  }
  sec.addEventListener('pointerenter',function(e){sec.classList.add('hover');last=null});
  sec.addEventListener('pointerleave',function(){sec.classList.remove('hover');last=null;ci++;setPen()});
  sec.addEventListener('pointermove',move);
  sec.addEventListener('pointerdown',function(e){if(e.target.closest('.reset'))return;last=null;move(e)});
  sec.addEventListener('pointerup',function(e){if(e.pointerType!=='mouse')last=null});
  btn.addEventListener('pointerenter',function(){last=null});
  btn.addEventListener('click',function(e){
    e.stopPropagation(); last=null;
    var done=function(){ctx.clearRect(0,0,W,H);drawn=false;travel=0;sec.classList.remove('drawn');btn.classList.remove('wiggle');btn.classList.add('out');setTimeout(function(){btn.hidden=true;btn.classList.remove('out')},450)};
    if(reduce)return done();
    /* Borrado animado: una franja blanca barre el lienzo */
    var t0=performance.now(),D=650;
    (function sweep(now){var k=Math.min(1,(now-t0)/D),e=k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2;
      ctx.save();ctx.globalCompositeOperation='destination-out';ctx.fillStyle='#000';ctx.fillRect(0,0,W*e,H);ctx.restore();
      if(k<1)requestAnimationFrame(sweep);else done()})(t0);
  });
})();
