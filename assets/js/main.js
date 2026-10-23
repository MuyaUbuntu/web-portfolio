/* Rodrigo López · Web Portfolio v3.1 — interactions and animation */
(function(){
  'use strict';
  var root=document.documentElement;
  /* Always open a page at the top (unless a #section was requested) */
  try{if('scrollRestoration' in history)history.scrollRestoration='manual'}catch(e){}
  function toTop(){if(!location.hash)window.scrollTo(0,0)}
  toTop();addEventListener('load',toTop);addEventListener('pageshow',function(e){if(!e.persisted)toTop()});
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine=matchMedia('(pointer:fine)').matches;
  var G=window.gsap, ST=window.ScrollTrigger, hasG=!!(G&&ST)&&!reduce;
  var $=function(s,c){return (c||document).querySelector(s)}, $$=function(s,c){return [].slice.call((c||document).querySelectorAll(s))};
  var below=function(el){return el.getBoundingClientRect().top>innerHeight*.92};

  /* ---------- Transition: circle from the click + chaotic white scribbles ---------- */
  var blot=$('.blot'), scrib=blot&&$('canvas',blot), scribRun=false;
  /* Hand-drawn scribbles: six kinds, a random one on every load (never the same twice in a row) */
  var W=260,H=180,CX=W/2,CY=H/2,R=Math.random;
  function rnd(a,b){return a+R()*(b-a)}
  function smooth(pts,steps){/* Catmull-Rom through control points → dense polyline */
    var out=[];for(var i=0;i<pts.length-1;i++){var p0=pts[i-1]||pts[i],p1=pts[i],p2=pts[i+1],p3=pts[i+2]||p2;
      for(var t=0;t<1;t+=1/steps){var t2=t*t,t3=t2*t;out.push([.5*((2*p1[0])+(-p0[0]+p2[0])*t+(2*p0[0]-5*p1[0]+4*p2[0]-p3[0])*t2+(-p0[0]+3*p1[0]-3*p2[0]+p3[0])*t3),
        .5*((2*p1[1])+(-p0[1]+p2[1])*t+(2*p0[1]-5*p1[1]+4*p2[1]-p3[1])*t2+(-p0[1]+3*p1[1]-3*p2[1]+p3[1])*t3)])}}
    return out}
  var KINDS={
    spiral:function(){var c=[],a=rnd(0,6.283),turns=rnd(5,7);for(var i=0;i<turns*14;i++){a+=6.283/14;var r=8+i*.62+rnd(-4,4);c.push([CX+Math.cos(a)*r*1.4,CY+Math.sin(a)*r])}return smooth(c,6)},
    zigzag:function(){var c=[],rows=rnd(9,13)|0,x0=CX-80,x1=CX+80,y=CY-52,dy=104/rows;for(var i=0;i<=rows;i++){c.push([i%2?x1+rnd(-8,8):x0+rnd(-8,8),y+i*dy+rnd(-4,4)+(i%2?8:-8)])}return smooth(c,10)},
    coil:function(){var c=[],x=CX-95,loops=rnd(6,8)|0,step=190/loops;for(var i=0;i<loops*8;i++){var a=i/8*6.283,r=rnd(20,30);c.push([x+i/8*step+Math.cos(a)*r*.75,CY+Math.sin(a)*r+rnd(-3,3)])}return smooth(c,5)},
    knot:function(){var c=[],fa=rnd(2.6,3.4),fb=2,ph=rnd(0,6.283),n=46;for(var i=0;i<=n;i++){var t=i/n*6.283*1.02;c.push([CX+Math.sin(fa*t+ph)*86+rnd(-1.5,1.5),CY+Math.sin(fb*t)*52+rnd(-1.5,1.5)])}return smooth(c,8)},
    squiggle:function(){var c=[],n=34,x0=CX-100;for(var i=0;i<=n;i++){var k=i/n,amp=10+Math.sin(k*3.14)*38;c.push([x0+k*200+rnd(-3,3),CY+Math.sin(i*1.35)*amp+rnd(-4,4)])}return smooth(c,8)}
  };
  function pickKind(){var keys=Object.keys(KINDS),last=null;try{last=sessionStorage.getItem('rl-scrib')}catch(e){}
    var pool=keys.filter(function(k){return k!==last}),k=pool[(R()*pool.length)|0];try{sessionStorage.setItem('rl-scrib',k)}catch(e){}return k}
  function scribble(){
    if(!scrib||scribRun)return; scribRun=true;
    var ctx=scrib.getContext('2d'),dpr=Math.min(2,devicePixelRatio||1);scrib.width=W*dpr;scrib.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);
    ctx.lineCap='round';ctx.lineJoin='round';ctx.strokeStyle='#fff';
    var pts=KINDS[pickKind()](),total=pts.length,t0=performance.now(),DUR=1100,drawn=1;
    /* a little hand tremor */
    pts=pts.map(function(p){return [p[0]+rnd(-.6,.6),p[1]+rnd(-.6,.6)]});
    ctx.clearRect(0,0,W,H);
    (function tick(now){if(!scribRun)return;
      var k=Math.min(1,(now-t0)/DUR),e=1-Math.pow(1-k,2),upto=Math.max(2,Math.floor(e*total));
      for(var i=drawn;i<upto;i++){ctx.lineWidth=1.6+Math.sin(i*.05)*.5;ctx.beginPath();ctx.moveTo(pts[i-1][0],pts[i-1][1]);ctx.lineTo(pts[i][0],pts[i][1]);ctx.stroke()}
      drawn=upto; if(k<1)requestAnimationFrame(tick)})(t0);
  }
  var arrived=false;
  try{arrived=sessionStorage.getItem('rl-go')==='1';sessionStorage.removeItem('rl-go')}catch(e){}
  if(arrived&&!reduce){root.classList.add('arriving');scribble();
    setTimeout(function(){root.classList.add('arrived');setTimeout(function(){root.classList.remove('arriving','arrived');scribRun=false},1600)},550)}
  /* ---------- Zoom transition: the image grows into the next page ---------- */
  function zoomFrom(a,e){var im=a.querySelector('.frame img,.peek img,.ph img')||null,src=a.getAttribute('data-img')||(im&&(im.currentSrc||im.src));if(!src)return false;
    var r=im&&im.getBoundingClientRect();if(!r||r.width<20||r.height<20){r={left:e.clientX-80,top:e.clientY-50,width:160,height:100}}
    var L=document.createElement('div');L.className='zoom-layer';L.innerHTML='<img alt="">';L.firstChild.src=src;
    var st=L.style;st.left=r.left+'px';st.top=r.top+'px';st.width=r.width+'px';st.height=r.height+'px';st.borderRadius='14px';document.body.appendChild(L);
    var t0=performance.now(),D=900,x0=r.left,y0=r.top,w0=r.width,h0=r.height,W=innerWidth,H=innerHeight;
    (function a2(now){var k=Math.min(1,(now-t0)/D),q=k<.5?4*k*k*k:1-Math.pow(-2*k+2,3)/2;st.left=x0*(1-q)+'px';st.top=y0*(1-q)+'px';st.width=(w0+(W-w0)*q)+'px';st.height=(h0+(H-h0)*q)+'px';st.borderRadius=(14*(1-q))+'px';if(k<1)requestAnimationFrame(a2)})(t0);
    try{sessionStorage.setItem('rl-zoom',src)}catch(err){}
    setTimeout(function(){location.href=a.getAttribute('href')},D+80);return true}
  (function(){var src=null;try{src=sessionStorage.getItem('rl-zoom');sessionStorage.removeItem('rl-zoom')}catch(e){}
    if(!src||reduce)return;var target=$('.c-cover,.m-stage');var L=document.createElement('div');L.className='zoom-layer';L.innerHTML='<img alt="">';L.firstChild.src=src;
    var st=L.style;st.left='0px';st.top='0px';st.width=innerWidth+'px';st.height=innerHeight+'px';document.body.appendChild(L);root.classList.add('zoomed');
    setTimeout(function(){var r=target?target.getBoundingClientRect():{left:innerWidth/2,top:innerHeight/2,width:0,height:0};
      var t0=performance.now(),D=850,W=innerWidth,H=innerHeight;
      (function a3(now){var k=Math.min(1,(now-t0)/D),q=1-Math.pow(1-k,3);st.left=(r.left*q)+'px';st.top=(r.top*q)+'px';st.width=(W+(r.width-W)*q)+'px';st.height=(H+(r.height-H)*q)+'px';st.borderRadius=(14*q)+'px';
        if(k<1)requestAnimationFrame(a3);else{L.style.transition='opacity .5s';L.style.opacity='0';setTimeout(function(){L.remove()},520)}})(t0)},250)})();
  $$('a[data-go]').forEach(function(a){a.addEventListener('click',function(e){
    if(reduce||e.metaKey||e.ctrlKey||e.shiftKey)return;
    if(a.hasAttribute('data-zoom')){var hz=a.getAttribute('href');if(hz&&hz.charAt(0)!=='#'){e.preventDefault();if(zoomFrom(a,e))return;location.href=hz;return}} var href=a.getAttribute('href'); if(!href||href.charAt(0)==='#')return;
    e.preventDefault(); if(blot){blot.style.setProperty('--bx',e.clientX+'px');blot.style.setProperty('--by',e.clientY+'px')}
    try{sessionStorage.setItem('rl-go','1')}catch(err){} root.classList.add('leaving'); scribble(); setTimeout(function(){location.href=href},1250);
  })});
  addEventListener('pageshow',function(e){if(e.persisted){root.classList.remove('leaving');scribRun=false}});

  /* ---------- Images: local file or published copy ---------- */
  $$('img[data-fallback]').forEach(function(img){
    function swap(){var f=img.getAttribute('data-fallback');if(f){img.removeAttribute('data-fallback');img.src=f}else img.style.opacity='0'}
    img.addEventListener('error',swap); if(img.complete&&img.naturalWidth===0)swap();
  });

  /* ---------- Smooth scroll ---------- */
  var lenis=null;
  if(hasG){G.registerPlugin(ST);if(!location.hash){ST.clearScrollMemory('manual');ST.addEventListener('refresh',function once(){if(!window.__topDone){window.__topDone=1;window.scrollTo(0,0);if(window.__lenis)window.__lenis.scrollTo(0,{immediate:true})}})}}
  if(hasG&&window.Lenis){lenis=new window.Lenis({lerp:.1,smoothWheel:true});window.__lenis=lenis;lenis.on('scroll',ST.update);G.ticker.add(function(t){lenis.raf(t*1000)});G.ticker.lagSmoothing(0);if(!location.hash){lenis.scrollTo(0,{immediate:true});addEventListener('load',function(){lenis.scrollTo(0,{immediate:true})})}}
  $$('a[href^="#"]').forEach(function(a){a.addEventListener('click',function(e){var id=a.getAttribute('href');if(id.length<2)return;var t=$(id);if(!t)return;e.preventDefault();
    if(lenis)lenis.scrollTo(t,{offset:-20,duration:1.3});else t.scrollIntoView({behavior:reduce?'auto':'smooth'})})});

  /* ---------- Cursor tag ---------- */
  var ctag=$('#ctag'), mx=0, my=0;
  addEventListener('pointermove',function(e){mx=e.clientX;my=e.clientY},{passive:true});
  if(ctag&&fine&&!reduce){var cx=0,cy=0;
    (function loop(){cx+=(mx-cx)*.22;cy+=(my-cy)*.22;ctag.style.transform='translate('+(cx+14)+'px,'+(cy+14)+'px)';requestAnimationFrame(loop)})();
    document.addEventListener('pointerover',function(e){var t=e.target.closest('[data-cursor]');if(t){ctag.textContent=t.getAttribute('data-cursor');ctag.classList.add('on')}else ctag.classList.remove('on')});
  }

  /* ---------- Nav pill ---------- */
  (function(){
    var wrap=$('.nav-links'), pill=$('.nav-pill'); if(!wrap||!pill)return;
    var links=$$('a',wrap), current=null;
    function moveTo(a){if(!a){pill.style.opacity='0';links.forEach(function(l){l.classList.remove('on')});return}
      pill.style.opacity='1';pill.style.width=a.offsetWidth+'px';pill.style.transform='translateX('+a.offsetLeft+'px)';links.forEach(function(l){l.classList.toggle('on',l===a)})}
    links.forEach(function(a){a.addEventListener('pointerenter',function(){moveTo(a)})});
    wrap.addEventListener('pointerleave',function(){moveTo(current)});
    var key=function(a){return a.getAttribute('href').replace(/^.*#/,'#')};
    var secs=links.map(function(a){return $(key(a))}).filter(Boolean);
    if(secs.length&&'IntersectionObserver' in window){
      var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){current=links.find(function(l){return key(l)==='#'+en.target.id})||null;moveTo(current)}})},{rootMargin:'-45% 0px -50% 0px'});
      secs.forEach(function(s){io.observe(s)});
      var h=$('.hero'); if(h)new IntersectionObserver(function(es){if(es[0].isIntersecting){current=null;moveTo(null)}},{rootMargin:'0px 0px -60% 0px'}).observe(h);
    }
  })();

  /* ---------- Drag (stickers): position eases toward the pointer, tilt follows smoothed velocity, inertia on release ---------- */
  function draggable(el){
    var tx=0,ty=0,cx=0,cy=0,rot=0,vx=0,vy=0,ox=0,oy=0,id=null,raf=0;
    function frame(){
      var px=cx,py=cy;
      if(id!==null){cx+=(tx-cx)*.32;cy+=(ty-cy)*.32}
      else{cx+=vx;cy+=vy;vx*=.9;vy*=.9}
      if(B){if(cx<B.x0){cx=B.x0;vx=Math.abs(vx)*.5}else if(cx>B.x1){cx=B.x1;vx=-Math.abs(vx)*.5}
        if(cy<B.y0){cy=B.y0;vy=Math.abs(vy)*.5}else if(cy>B.y1){cy=B.y1;vy=-Math.abs(vy)*.5}}
      var dx=cx-px; if(id!==null){vx=dx;vy=cy-py}
      var targetRot=Math.max(-14,Math.min(14,dx*.9));
      rot+=(targetRot-rot)*.18;
      el.style.transform='translate3d('+cx.toFixed(2)+'px,'+cy.toFixed(2)+'px,0) rotate('+rot.toFixed(2)+'deg)';
      if(id!==null||Math.abs(vx)>.05||Math.abs(vy)>.05||Math.abs(rot)>.05)raf=requestAnimationFrame(frame);
      else{raf=0;tx=cx;ty=cy;rot=0;el.style.transform='translate3d('+cx.toFixed(2)+'px,'+cy.toFixed(2)+'px,0)'}
    }
    function start(){if(!raf)raf=requestAnimationFrame(frame)}
    var B=null,host=el.closest('.hero')||document.body;
    function bounds(){var h=host.getBoundingClientRect(),r=el.getBoundingClientRect(),bl=r.left-cx,bt=r.top-cy,m=8;
      B={x0:Math.max(h.left,0)+m-bl,x1:Math.min(h.right,innerWidth)-m-(bl+r.width),y0:h.top+m-bt,y1:h.bottom-m-(bt+r.height)}}
    addEventListener('resize',function(){B=null;cancelAnimationFrame(raf);raf=0;tx=ty=cx=cy=vx=vy=rot=0;el.style.transform=''});
    el.addEventListener('pointerdown',function(e){bounds();id=e.pointerId;el.setPointerCapture(id);ox=e.clientX-cx;oy=e.clientY-cy;tx=cx;ty=cy;vx=vy=0;el.classList.add('dragging');el.style.transition='none';start()});
    el.addEventListener('pointermove',function(e){if(e.pointerId!==id)return;tx=e.clientX-ox;ty=e.clientY-oy});
    function up(e){if(e.pointerId!==id)return;id=null;el.classList.remove('dragging');vx=Math.max(-30,Math.min(30,vx));vy=Math.max(-30,Math.min(30,vy));start()}
    el.addEventListener('pointerup',up);el.addEventListener('pointercancel',up);
    el.addEventListener('lostpointercapture',up);
    el.addEventListener('dblclick',function(){cancelAnimationFrame(raf);raf=0;tx=ty=cx=cy=vx=vy=rot=0;el.style.transition='transform .8s cubic-bezier(.34,1.56,.64,1)';el.style.transform='';setTimeout(function(){el.style.transition=''},800)});
  }
  if(!reduce)$$('.stk').forEach(draggable);

  /* ---------- Dot grid that reacts to the cursor ---------- */
  (function(){
    var cv=$('.dots'); if(!cv||reduce)return; var ctx=cv.getContext('2d'),host=cv.parentElement,W=0,H=0,dpr=Math.min(2,devicePixelRatio||1),px=-999,py=-999,vis=true;
    function size(){var r=host.getBoundingClientRect();W=r.width;H=r.height;cv.width=W*dpr;cv.height=H*dpr}
    size(); addEventListener('resize',size);
    host.addEventListener('pointermove',function(e){var r=host.getBoundingClientRect();px=e.clientX-r.left;py=e.clientY-r.top});
    host.addEventListener('pointerleave',function(){px=py=-999});
    if('IntersectionObserver' in window)new IntersectionObserver(function(es){vis=es[0].isIntersecting}).observe(host);
    var GAP=28,t0=performance.now();
    (function draw(now){requestAnimationFrame(draw);if(!vis)return;
      ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,W,H);var t=(now-t0)/1000;
      for(var x=GAP/2;x<W;x+=GAP)for(var y=GAP/2;y<H;y+=GAP){
        var dx=x-px,dy=y-py,d=Math.sqrt(dx*dx+dy*dy),k=Math.max(0,1-d/160),wave=.5+.5*Math.sin(t*1.2+x*.012+y*.01);
        ctx.globalAlpha=.14+k*.8;ctx.fillStyle=k>.05?'#FF4B2B':'#141110';ctx.beginPath();ctx.arc(x-dx*k*.18,y-dy*k*.18,1+wave*.5+k*5,0,6.283);ctx.fill()}
      ctx.globalAlpha=1})(t0);
  })();

  /* ---------- Interactive statement: sketch → campaign ---------- */
  (function(){
    var say=$('.say'); if(!say)return;
    var peek=$('.peekimg'), pimg=$('img',peek), plab=$('span',peek), pop=$('.tools-pop'), pairs=JSON.parse(say.getAttribute('data-pairs')||'[]'), i=0, mode=null;
    pairs.forEach(function(p){[p.ref,p.fin].forEach(function(u){var im=new Image();im.src=u})});
    function place(x,y){var w=peek.offsetWidth,h=peek.offsetHeight,X=Math.min(innerWidth-w-12,Math.max(12,x+24)),Y=Math.min(innerHeight-h-12,Math.max(12,y-h-16));peek.style.transform='translate('+X+'px,'+Y+'px)';if(pop)pop.style.transform='translate('+Math.min(innerWidth-180,x+18)+'px,'+(y-58)+'px)'}
    function show(w,x,y){var k=w.getAttribute('data-k');$$('.hw',say).forEach(function(o){o.classList.toggle('on',o===w)});
      if(k==='co'){peek.classList.remove('on');pop&&pop.classList.add('on')}
      else{pop&&pop.classList.remove('on');var p=pairs[i%pairs.length];pimg.src=k==='sk'?p.ref:p.fin;plab.textContent=(k==='sk'?'Reference · ':'Final · ')+p.name;peek.classList.add('on')}
      mode=k;place(x,y)}
    function hide(){if(mode==='cp')i++;mode=null;peek.classList.remove('on');pop&&pop.classList.remove('on');$$('.hw',say).forEach(function(o){o.classList.remove('on')})}
    $$('.hw',say).forEach(function(w){
      w.addEventListener('pointerenter',function(e){if(e.pointerType==='mouse')show(w,e.clientX,e.clientY)});
      w.addEventListener('pointermove',function(e){if(mode)place(e.clientX,e.clientY)});
      w.addEventListener('pointerleave',function(e){if(e.pointerType==='mouse')hide()});
      w.addEventListener('click',function(e){var r=w.getBoundingClientRect();if(mode===w.getAttribute('data-k')){hide()}else show(w,r.left+r.width/2,r.top)});
    });
    addEventListener('scroll',function(){if(mode&&!fine)hide()},{passive:true});
  })();

  /* ---------- Services: accordion + big number ---------- */
  (function(){
    var big=$('.svc-big'), now=$('.svc-card .now b');
    function setNum(li){if(!big)return;var n=li.getAttribute('data-n');if(big.textContent===n)return;big.classList.add('flip');setTimeout(function(){big.textContent=n;big.classList.remove('flip')},180);if(now)now.textContent=$('h3',li).textContent}
    $$('.svc li').forEach(function(li,i,all){var b=$('button',li);b.setAttribute('aria-expanded',li.classList.contains('open'));
      li.addEventListener('pointerenter',function(){setNum(li)});
      b.addEventListener('click',function(){var o=!li.classList.contains('open');all.forEach(function(x){x.classList.remove('open');$('button',x).setAttribute('aria-expanded','false')});if(o){li.classList.add('open');b.setAttribute('aria-expanded','true')}setNum(li);setTimeout(function(){ST&&ST.refresh()},650)})});
    var svc=$('.svc');if(svc)svc.addEventListener('pointerleave',function(){var o=$('.svc li.open');if(o)setNum(o)});
  })();

  /* ---------- Odometer ---------- */
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

  /* ---------- Contact: button that chases the cursor, copies email ---------- */
  var blob=$('.blob');
  if(blob&&fine&&!reduce){var area=blob.closest('.contact'),bx=0,by=0,ax=0,ay=0;
    area.addEventListener('pointermove',function(e){var r=blob.getBoundingClientRect();var dx=e.clientX-(r.left+r.width/2-ax),dy=e.clientY-(r.top+r.height/2-ay);var k=Math.max(0,1-Math.sqrt(dx*dx+dy*dy)/420);bx=dx*k*.45;by=dy*k*.45});
    area.addEventListener('pointerleave',function(){bx=by=0});
    (function loop(){ax+=(bx-ax)*.12;ay+=(by-ay)*.12;blob.style.transform='translate('+ax+'px,'+ay+'px)';requestAnimationFrame(loop)})()}
  var mail=$('#mail');
  if(blob&&mail){var label=blob.innerHTML;blob.addEventListener('click',function(){
    var ok=function(){blob.innerHTML='Copied!';setTimeout(function(){blob.innerHTML=label},1600)};
    var fb=function(){var r=document.createRange();r.selectNodeContents(mail);var s=getSelection();s.removeAllRanges();s.addRange(r);blob.innerHTML='Select<br>&amp; copy'};
    try{navigator.clipboard.writeText(mail.textContent.trim()).then(ok,fb)}catch(e){fb()}})}

  /* ---------- Draggable gallery ---------- */
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

  /* ---------- Chapter index ---------- */
  (function(){var toc=$('.toc');if(!toc)return;var links=$$('a',toc),bar=$('.bar i',toc),chs=links.map(function(a){return $(a.getAttribute('href'))});
    function upd(){var mid=innerHeight*.4,on=0;chs.forEach(function(c,i){if(c&&c.getBoundingClientRect().top<mid)on=i});links.forEach(function(a,i){a.classList.toggle('on',i===on)});
      var wrap=toc.parentElement.getBoundingClientRect(),p=Math.min(1,Math.max(0,(mid-wrap.top)/wrap.height));if(bar)bar.style.transform='scaleX('+p+')';toc.classList.toggle('show',wrap.top<innerHeight*.75&&wrap.bottom>innerHeight*.6)}
    addEventListener('scroll',upd,{passive:true});upd()})();

  /* ---------- Case hero: fanned cards follow the cursor ---------- */
  (function(){var fan=$('.fan');if(!fan||!fine||reduce)return;var cards=$$('.card-img',fan),tx=0,ty=0,ax=0,ay=0;
    fan.parentElement.addEventListener('pointermove',function(e){var r=fan.getBoundingClientRect();tx=(e.clientX-r.left)/r.width-.5;ty=(e.clientY-r.top)/r.height-.5});
    fan.parentElement.addEventListener('pointerleave',function(){tx=ty=0});
    (function loop(){ax+=(tx-ax)*.07;ay+=(ty-ay)*.07;cards.forEach(function(c,i){var d=(i+1)*14;c.style.translate='calc(-50% + '+(ax*d)+'px) calc(-50% + '+(ay*d)+'px)'});requestAnimationFrame(loop)})()})();

  /* ---------- Iteration strips: a selection box hunts for the keeper ---------- */
  $$('.strip[data-pick]').forEach(function(s){
    var box=document.createElement('span');box.className='pick';s.appendChild(box);
    var n=+s.getAttribute('data-n')||6, keep=+s.getAttribute('data-pick'), i=0, t=null;
    function step(){i=(i+1)%n;box.style.left=(i*(100/n)+.5)+'%'}
    function run(){if(t||reduce)return;var hops=0;t=setInterval(function(){step();hops++;if(hops>n+2&&i===keep){clearInterval(t);t=null;setTimeout(run,2600)}},420)}
    box.style.left=(keep*(100/n)+.5)+'%';
    if('IntersectionObserver' in window)new IntersectionObserver(function(es){if(es[0].isIntersecting)run()}).observe(s);
  });

  /* ---------- Prompt card: typed when it scrolls in ---------- */
  $$('.prompt .typed').forEach(function(el){
    var full=el.textContent; if(reduce)return; el.textContent='';
    var go=function(){var k=0;(function tick(){el.textContent=full.slice(0,k);k+=2;if(k<=full.length+1)setTimeout(tick,22)})()};
    if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){go();io.disconnect()}},{threshold:.5});io.observe(el)}else el.textContent=full;
  });

  /* ---------- Before / after ---------- */
  $$('.compare').forEach(function(c){var r=$('input',c);function set(){c.style.setProperty('--pos',r.value+'%')}r.addEventListener('input',set);set();
    if(!reduce&&'IntersectionObserver' in window){var io=new IntersectionObserver(function(es){if(!es[0].isIntersecting)return;io.disconnect();var t0=performance.now();
      (function a(now){var k=Math.min(1,(now-t0)/1600),v=50+Math.sin(k*Math.PI*2)*22*(1-k);r.value=v;set();if(k<1)requestAnimationFrame(a);else{r.value=50;set()}})(t0)},{threshold:.6});io.observe(c)}});

  /* ---------- Happy Talks: the real landing scrolls inside a browser ---------- */
  $$('.browser').forEach(function(b){var v=$('.br-view',b),notes=$$('.br-notes li',b),ys=notes.map(function(n){return +n.getAttribute('data-y')}),user=false,vis=false,pos=0,last=0;
    function mark(){var f=(v.scrollTop+v.clientHeight*.35)/v.scrollHeight,on=0;ys.forEach(function(y,i){if(f>=y)on=i});notes.forEach(function(n,i){n.classList.toggle('on',i===on)})}
    function take(){if(!user){user=true;b.classList.add('user')}}
    v.addEventListener('scroll',mark,{passive:true});var coarse=matchMedia('(pointer:coarse)').matches;if(!coarse)['wheel','pointerdown','keydown'].forEach(function(ev){v.addEventListener(ev,take,{passive:true})});
    v.addEventListener('wheel',function(e){e.stopPropagation()},{passive:true});
    notes.forEach(function(n,i){n.addEventListener('click',function(){take();v.scrollTo({top:ys[i]*v.scrollHeight,behavior:'smooth'})})});
    if('IntersectionObserver' in window)new IntersectionObserver(function(es){vis=es[0].isIntersecting;if(vis)requestAnimationFrame(loop)}).observe(b);
    function loop(t){if(!vis||user||reduce)return;var dt=last?Math.min(50,t-last):16;last=t;pos+=dt*.06;if(pos>=v.scrollHeight-v.clientHeight){pos=0}v.scrollTop=pos;requestAnimationFrame(loop)}
    mark()});

  /* ---------- Happy Talks: sticker storm with simple physics ---------- */
  $$('.storm').forEach(function(box){var els=$$('.stk-p',box),W=0,H=0,bodies=[],running=false,vis=false;
    function size(){W=box.clientWidth;H=box.clientHeight}
    function drop(){size();bodies=els.map(function(el,i){return {el:el,w:el.offsetWidth||80,h:el.offsetHeight||60,x:Math.random()*(W-el.offsetWidth),y:-80-i*70-Math.random()*60,vx:(Math.random()-.5)*3,vy:0,r:(Math.random()-.5)*24,vr:(Math.random()-.5)*2.5,drag:false}});start()}
    function start(){if(!running){running=true;requestAnimationFrame(step)}}
    function step(){var moving=false;bodies.forEach(function(b){if(!b.drag){b.vy+=.6;b.x+=b.vx;b.y+=b.vy;b.r+=b.vr;
        if(b.y+b.h>H){b.y=H-b.h;b.vy*=-.38;b.vx*=.86;b.vr*=.5;if(Math.abs(b.vy)<1)b.vy=0}var onF=b.y+b.h>=H-1||Math.abs(b.vy)<.4;b.r=((b.r+180)%360+360)%360-180;if(onF){b.r+=(0-b.r)*.18;b.vr*=.6}else{b.vr*=.985}if(Math.abs(b.r)>.3)moving=true;
        if(b.x<0){b.x=0;b.vx*=-.6}if(b.x+b.w>W){b.x=W-b.w;b.vx*=-.6}
        if(Math.abs(b.vx)>.05||Math.abs(b.vy)>.05||b.y+b.h<H-1)moving=true;else{b.vx=0;b.vr=0}}else moving=true;
      });
      for(var it=0;it<3;it++)bodies.forEach(function(b){if(b.drag)return;bodies.forEach(function(o){if(o===b)return;var ox=Math.min(b.x+b.w,o.x+o.w)-Math.max(b.x,o.x),oy=Math.min(b.y+b.h,o.y+o.h)-Math.max(b.y,o.y);if(ox<=0||oy<=0)return;
        if(oy<ox){if(b.y<o.y){b.y-=oy;if(b.vy>0)b.vy*=-.15}}else{var d=(b.x+b.w/2<o.x+o.w/2)?-ox:ox;b.x+=d*.5;b.vx*=.5;if(b.x<0)b.x=0;if(b.x+b.w>W)b.x=W-b.w}})});
      bodies.forEach(function(b){b.el.style.transform='translate('+b.x.toFixed(1)+'px,'+b.y.toFixed(1)+'px) rotate('+b.r.toFixed(1)+'deg)'});
      if(moving&&vis)requestAnimationFrame(step);else running=false}
    bodies=[];els.forEach(function(el,i){el.addEventListener('pointerdown',function(e){var b=bodies[i];if(!b)return;b.drag=true;el.classList.add('drag');el.setPointerCapture(e.pointerId);var r=box.getBoundingClientRect(),ox=e.clientX-r.left-b.x,oy=e.clientY-r.top-b.y,lx=e.clientX,ly=e.clientY;
      function mv(ev){b.vx=ev.clientX-lx;b.vy=ev.clientY-ly;lx=ev.clientX;ly=ev.clientY;b.x=ev.clientX-r.left-ox;b.y=ev.clientY-r.top-oy;b.vr=Math.max(-6,Math.min(6,b.vx*.25));start()}
      function up(){b.drag=false;el.classList.remove('drag');el.removeEventListener('pointermove',mv);el.removeEventListener('pointerup',up);b.vx=Math.max(-40,Math.min(40,b.vx));b.vy=Math.max(-40,Math.min(40,b.vy));start()}
      el.addEventListener('pointermove',mv);el.addEventListener('pointerup',up)})});
    $('.storm-reset',box).addEventListener('click',drop);addEventListener('resize',size);
    var first=true;if('IntersectionObserver' in window)new IntersectionObserver(function(es){vis=es[0].isIntersecting;if(vis){if(first){first=false;drop()}else start()}},{threshold:.3}).observe(box);else{vis=true;drop()}});

  /* ---------- Happy Talks: the mic amplifies the words ---------- */
  $$('.micdrop').forEach(function(m){var wrap=$('.md-mic-wrap',m),ls=$$('.ml',m),x=0,tx=0,y=0,W=0,H=0,vis=false,first=true;
    function size(){W=m.clientWidth;H=m.clientHeight;if(first){x=tx=W*.72;y=H+40;first=false}}
    m.addEventListener('pointermove',function(e){var b=m.getBoundingClientRect();tx=Math.max(0,Math.min(W-wrap.offsetWidth,e.clientX-b.left-wrap.offsetWidth/2));m.classList.add('on')});
    m.addEventListener('pointerleave',function(){m.classList.remove('on')});
    function loop(t){if(!vis)return;size();x+=(tx-x)*.12;var rest=H-wrap.offsetHeight*.62;y+=(rest-y)*.08;
      wrap.style.transform='translate('+x.toFixed(1)+'px,'+(y+Math.sin(t/700)*4).toFixed(1)+'px) rotate('+((tx-x)*.04).toFixed(2)+'deg)';
      var mb=m.getBoundingClientRect(),mx=mb.left+x+wrap.offsetWidth*.62,on=m.classList.contains('on');
      ls.forEach(function(l,i){var r=l.getBoundingClientRect(),d=Math.abs(r.left+r.width/2-mx),a=on?Math.max(0,1-d/220):0,v=a*(.55+.45*Math.sin(t/85+i*1.7));
        l.style.transform='translateY('+(-v*14).toFixed(1)+'px) scaleY('+(1+v*.45).toFixed(3)+')';l.style.color=a>.25?'#57E3C3':''});
      requestAnimationFrame(loop)}
    if('IntersectionObserver' in window)new IntersectionObserver(function(es){vis=es[0].isIntersecting;if(vis)requestAnimationFrame(loop)}).observe(m)});

  /* ---------- Conexiones Mágicas: pop the cap ---------- */
  $$('.pop').forEach(function(b){var cap=$('.pop-cap',b),done=false,sx=0,sy=0,dragging=false,lx=0,ly=0,vx=0,vy=0;
    function fly(dx,dy){if(done)return;done=true;cap.style.animation='none';var x=0,y=0,r=0,ux=dx||(Math.random()<.5?-1:1)*14,uy=dy||-26,vr=ux*1.6;
      (function f(){x+=ux;y+=uy;uy+=1.3;r+=vr;cap.style.transform='translate('+x+'px,'+y+'px) rotate('+r+'deg)';if(y<innerHeight)requestAnimationFrame(f)})();b.classList.add('gone')}
    b.addEventListener('pointerdown',function(e){dragging=true;sx=lx=e.clientX;sy=ly=e.clientY;try{b.setPointerCapture(e.pointerId)}catch(err){}});
    b.addEventListener('pointermove',function(e){if(!dragging||done)return;vx=e.clientX-lx;vy=e.clientY-ly;lx=e.clientX;ly=e.clientY;cap.style.animation='none';cap.style.transform='translate('+(e.clientX-sx)+'px,'+(e.clientY-sy)+'px) rotate('+((e.clientX-sx)*.4)+'deg)'});
    b.addEventListener('pointerup',function(e){if(!dragging)return;dragging=false;var moved=Math.hypot(e.clientX-sx,e.clientY-sy);
      if(moved>8){var k=Math.max(1,Math.hypot(vx,vy));fly(vx/k*22,Math.min(-12,vy/k*22))}else fly()});
    b.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();fly()}})});

  /* ---------- Conexiones Mágicas: scrub the PSD layers ---------- */
  $$('.trick').forEach(function(t){var im=$$('.t-img',t),li=$$('.t-list li',t),nt=$$('.t-note',t),rg=$('.t-range',t),cur=0,timer=null,user=false;
    function show(i){cur=i;im.forEach(function(x,k){x.classList.toggle('on',k===i)});li.forEach(function(x,k){x.classList.toggle('on',k===i)});nt.forEach(function(x,k){x.classList.toggle('on',k===i)});rg.value=i}
    function stop(){user=true;clearInterval(timer)}
    rg.addEventListener('input',function(){stop();show(+rg.value)});li.forEach(function(x,k){x.addEventListener('click',function(){stop();show(k)})});
    if(!reduce&&'IntersectionObserver' in window)new IntersectionObserver(function(es){if(es[0].isIntersecting&&!user){clearInterval(timer);timer=setInterval(function(){show((cur+1)%im.length)},2200)}else clearInterval(timer)},{threshold:.4}).observe(t)});

  /* ---------- Lightbox: click a gallery image to see it whole ---------- */
  (function(){var SEL='.kv-grid img,.drag-track img,.stage-card .im img,.strip img,.b-img img,.refs img,.t-img img,.cap-two img',GROUP='.kv-grid,.drag-track,.flow,.b-stage,.refs,.t-stage,.cap-two';
    var lb=null,list=[],idx=0,dx=0,dy=0;
    addEventListener('pointerdown',function(e){dx=e.clientX;dy=e.clientY},true);
    function cap(im){var f=im.closest('figure');var c=f&&f.querySelector('figcaption');var t=c?c.textContent.replace(/\s+/g,' ').trim():'';return t||im.alt||''}
    function build(){lb=document.createElement('div');lb.className='lb';lb.setAttribute('role','dialog');lb.setAttribute('aria-modal','true');lb.setAttribute('aria-label','Image viewer');
      lb.innerHTML='<figure><img alt=""><figcaption></figcaption></figure><button type="button" class="lb-x" aria-label="Close">✕</button><button type="button" class="lb-p" aria-label="Previous">←</button><button type="button" class="lb-n" aria-label="Next">→</button>';
      lb.addEventListener('click',function(e){if(e.target.closest('.lb-p'))return go(-1);if(e.target.closest('.lb-n'))return go(1);close()});
      document.body.appendChild(lb)}
    function show(){var im=list[idx],big=$('img',lb);big.src=im.currentSrc||im.src;big.alt=im.alt||'';$('figcaption',lb).innerHTML=cap(im)+(list.length>1?'<span>'+(idx+1)+' / '+list.length+'</span>':'')}
    function go(d){idx=(idx+d+list.length)%list.length;show()}
    function open(im){if(!lb)build();var g=im.closest(GROUP);list=g?$$('img',g).filter(function(x){return x.matches(SEL)}):[im];idx=Math.max(0,list.indexOf(im));
      lb.classList.toggle('single',list.length<2);show();lb.hidden=false;requestAnimationFrame(function(){lb.classList.add('on')});if(window.__lenis)window.__lenis.stop();document.documentElement.style.overflow='hidden';$('.lb-x',lb).focus()}
    function close(){if(!lb||lb.hidden)return;lb.classList.remove('on');setTimeout(function(){lb.hidden=true},300);if(window.__lenis)window.__lenis.start();document.documentElement.style.overflow=''}
    document.addEventListener('click',function(e){var im=e.target.closest&&e.target.closest(SEL);if(!im||e.target.closest('a'))return;if(Math.abs(e.clientX-dx)>6||Math.abs(e.clientY-dy)>6)return;e.preventDefault();open(im)});
    addEventListener('keydown',function(e){if(!lb||lb.hidden)return;if(e.key==='Escape')close();else if(e.key==='ArrowRight')go(1);else if(e.key==='ArrowLeft')go(-1)})})();

  /* ---------- Index: the final art follows the cursor and bends with speed ---------- */
  (function(){var fl=$('.ix-float');if(!fl||!fine)return;var im=$('img',fl),x=0,y=0,cx=0,cy=0,on=false,raf=0;
    function loop(){var vx=x-cx;cx+=(x-cx)*.14;cy+=(y-cy)*.14;var sk=Math.max(-18,Math.min(18,vx*.25));
      fl.style.transform='translate3d('+(cx-fl.offsetWidth/2)+'px,'+(cy-fl.offsetHeight/2)+'px,0) skewX('+(-sk)+'deg) rotate('+(sk*.4)+'deg)';raf=on||Math.abs(vx)>.3?requestAnimationFrame(loop):0}
    $$('.ix-row').forEach(function(r){r.addEventListener('pointerenter',function(e){var u=r.getAttribute('data-img');if(u&&im.getAttribute('src')!==u)im.src=u;if(!on){cx=x=e.clientX;cy=y=e.clientY}on=true;fl.classList.add('on');if(!raf)raf=requestAnimationFrame(loop)});
      r.addEventListener('pointerleave',function(){on=false;fl.classList.remove('on')})});
    addEventListener('pointermove',function(e){x=e.clientX;y=e.clientY},{passive:true})})();

  /* ---------- Flashlight: the finals appear only where you point ---------- */
  (function(){var lp=$('.lamp');if(!lp)return;var x=.5,y=.5,tx=.5,ty=.5,rad=190,trad=190,user=false,last=0,vis=false;
    function set(e){var r=lp.getBoundingClientRect();tx=(e.clientX-r.left)/r.width;ty=(e.clientY-r.top)/r.height;user=true;last=performance.now()}
    lp.addEventListener('pointermove',set);lp.addEventListener('pointerdown',function(e){set(e);trad=320});addEventListener('pointerup',function(){trad=190});
    lp.addEventListener('pointerleave',function(){user=false});
    if('IntersectionObserver' in window)new IntersectionObserver(function(es){vis=es[0].isIntersecting;if(vis)requestAnimationFrame(loop)}).observe(lp);
    function loop(now){if(!vis)return;if(!user||now-last>2500){var t=now/1000;tx=.5+Math.sin(t*.7)*.32;ty=.5+Math.sin(t*1.1+1)*.28}
      x+=(tx-x)*.09;y+=(ty-y)*.09;rad+=(trad-rad)*.1;lp.style.setProperty('--x',(x*100)+'%');lp.style.setProperty('--y',(y*100)+'%');lp.style.setProperty('--rad',(reduce?260:rad)+'px');requestAnimationFrame(loop)}})();

  /* ---------- ArboTerra: same tree, four moods ---------- */
  (function(){var box=$('.moods');if(!box)return;var stage=$('.m-stage',box),tabs=$$('.m-tabs button',box),ls=$$('.m-layer',box),lk=$$('.lock',box),ids=tabs.map(function(b){return b.getAttribute('data-m')}),cur=0,t=null,user=false;
    function show(i){cur=i;var m=ids[i];ls.forEach(function(l){l.classList.toggle('on',l.getAttribute('data-m')===m)});lk.forEach(function(l){l.classList.toggle('on',l.getAttribute('data-m')===m)});tabs.forEach(function(b,k){b.setAttribute('aria-pressed',k===i?'true':'false')});
      ls.forEach(function(l){$$('img',l).forEach(function(im){im.loading='eager'})})}
    function auto(){if(reduce||user)return;clearInterval(t);t=setInterval(function(){show((cur+1)%ids.length)},3200)}
    tabs.forEach(function(b,i){b.addEventListener('click',function(){user=true;clearInterval(t);show(i)})});
    stage.addEventListener('click',function(){user=true;clearInterval(t);show((cur+1)%ids.length)});
    if(fine&&!reduce){var tx=0,ty=0,ax=0,ay=0;stage.addEventListener('pointermove',function(e){var r=stage.getBoundingClientRect();tx=(e.clientX-r.left)/r.width-.5;ty=(e.clientY-r.top)/r.height-.5});stage.addEventListener('pointerleave',function(){tx=ty=0});
      (function loop(){ax+=(tx-ax)*.06;ay+=(ty-ay)*.06;stage.style.setProperty('--tx',(ax*22)+'px');stage.style.setProperty('--ty',(ay*14)+'px');stage.style.setProperty('--bx',(-ax*14)+'px');stage.style.setProperty('--by',(-ay*10)+'px');requestAnimationFrame(loop)})()}
    if('IntersectionObserver' in window)new IntersectionObserver(function(es){if(es[0].isIntersecting)auto();else clearInterval(t)}).observe(stage);else auto()})();

  /* ---------- ArboTerra: scene built layer by layer ---------- */
  $$('.build').forEach(function(b){var btn=$$('.b-steps button',b),im=$$('.b-img',b),nt=$$('.b-note',b),cur=0,t=null,D=2600;
    function show(i){cur=i;btn.forEach(function(x,k){x.setAttribute('aria-pressed',k===i?'true':'false')});im.forEach(function(x,k){x.classList.toggle('on',k===i)});nt.forEach(function(x,k){x.classList.toggle('on',k===i)})}
    function run(){if(reduce){b.classList.add('paused');return}clearInterval(t);t=setInterval(function(){show((cur+1)%btn.length)},D)}
    btn.forEach(function(x,i){x.addEventListener('click',function(){clearInterval(t);b.classList.add('paused');show(i)})});
    if('IntersectionObserver' in window)new IntersectionObserver(function(es){if(es[0].isIntersecting){if(!b.classList.contains('paused'))run()}else clearInterval(t)},{threshold:.4}).observe(b)});

  if(!hasG)return;
  /* ===================== GSAP ===================== */
  var stks=$$('.stk');
  if(stks.length)G.from(stks,{y:-70,rotation:function(i){return (i%2?1:-1)*(10+i*3)},scale:.85,duration:1.1,ease:'elastic.out(1,.55)',stagger:.08,delay:.1,clearProps:'transform'});

  $$('.rail').forEach(function(r){
    var dir=r.closest('.alt')?1:-1,x=0,boost=0,w=r.scrollWidth/2;
    addEventListener('resize',function(){w=r.scrollWidth/2});
    ST.create({trigger:r,start:'top bottom',end:'bottom top',onUpdate:function(s){boost=s.getVelocity()/300}});
    G.ticker.add(function(){var sp=(1+Math.min(12,Math.abs(boost)))*(boost<0?-1:1);x+=dir*sp*.6;boost*=.92;if(x<-w)x+=w;if(x>0)x-=w;r.style.transform='translate3d('+x+'px,0,0) skewX('+(-boost*1.2)+'deg)'});
  });

  $$('.lm > span').forEach(function(s){if(!below(s))return;G.from(s,{yPercent:110,rotation:4,duration:1.1,ease:'expo.out',scrollTrigger:{trigger:s,start:'top 92%'}})});
  $$('[data-pop]').forEach(function(el){if(!below(el))return;G.from(el,{y:60,scale:.94,opacity:0,duration:1,ease:'back.out(1.6)',scrollTrigger:{trigger:el,start:'top 90%'}})});
  $$('.say .hw').forEach(function(w,i){if(!below(w))return;G.from(w,{y:30,rotation:i%2?8:-8,opacity:0,duration:.9,ease:'back.out(2)',scrollTrigger:{trigger:w,start:'top 88%'}})});

  $$('.card').forEach(function(c){var ph=$('.frame .ph',c),fr=$('.frame',c);
    if(ph)G.fromTo(ph,{yPercent:-6},{yPercent:6,ease:'none',scrollTrigger:{trigger:c,start:'top bottom',end:'bottom top',scrub:true}});
    if(below(c))G.from(fr,{y:120,rotation:c.matches(':nth-child(even)')?4:-4,duration:1.2,ease:'expo.out',scrollTrigger:{trigger:c,start:'top 92%'}});
    if(fine){var qx=G.quickTo(fr,'rotationY',{duration:.6,ease:'power3'}),qy=G.quickTo(fr,'rotationX',{duration:.6,ease:'power3'});G.set(fr,{transformPerspective:900});
      c.addEventListener('pointermove',function(e){var r=fr.getBoundingClientRect();qx(((e.clientX-r.left)/r.width-.5)*10);qy(-((e.clientY-r.top)/r.height-.5)*10)});
      c.addEventListener('pointerleave',function(){qx(0);qy(0)})}
  });
  var stage=$('.stage');if(stage)G.fromTo(stage,{borderRadius:'120px'},{borderRadius:'48px',ease:'none',scrollTrigger:{trigger:stage,start:'top bottom',end:'top 30%',scrub:true}});

  $$('.xp li').forEach(function(li,i){if(!below(li))return;G.from(li,{x:i%2?60:-60,opacity:0,duration:.9,ease:'expo.out',scrollTrigger:{trigger:li,start:'top 92%'}})});
  $$('.contact h2 .lm > span').forEach(function(s,i){G.fromTo(s,{xPercent:i%2?12:-12},{xPercent:0,ease:'none',scrollTrigger:{trigger:'.contact',start:'top bottom',end:'top 30%',scrub:true}})});

  var lts=$$('.c-title .lt');
  if(lts.length)G.from(lts,{yPercent:-40,rotation:function(){return G.utils.random(-25,25)},duration:1,ease:'elastic.out(1,.6)',stagger:.035,delay:.15,clearProps:'transform'});
  var fanCards=$$('.fan .card-img');
  if(fanCards.length)G.from(fanCards,{x:0,y:40,rotation:0,scale:.8,duration:1.3,ease:'elastic.out(1,.7)',stagger:.12,delay:.25,clearProps:'x,y,scale'});

  $$('.wipe,.shot-big').forEach(function(w){if(!below(w))return;G.fromTo(w,{clipPath:'inset(100% 0% 0% 0% round 22px)'},{clipPath:'inset(0% 0% 0% 0% round 22px)',duration:1.3,ease:'expo.inOut',scrollTrigger:{trigger:w,start:'top 85%'}});
    var im=$('img',w);if(im)G.from(im,{scale:1.25,duration:1.6,ease:'expo.out',scrollTrigger:{trigger:w,start:'top 85%'}})});
  $$('.quote').forEach(function(q,i){if(!below(q))return;G.from(q,{y:100,rotation:i%2?12:-12,opacity:0,duration:1.1,ease:'back.out(1.5)',scrollTrigger:{trigger:q,start:'top 90%'}})});
  $$('.flow .stage-card').forEach(function(s,i){if(!below(s))return;G.from(s,{y:80,rotation:(i-1)*6,opacity:0,duration:1.1,delay:i*.12,ease:'back.out(1.4)',scrollTrigger:{trigger:s.parentElement,start:'top 85%'}})});
  $$('.pull').forEach(function(p){if(!below(p))return;G.from(p,{x:-60,opacity:0,duration:1,ease:'expo.out',scrollTrigger:{trigger:p,start:'top 88%'}})});

  addEventListener('load',function(){ST.refresh()});
  if(document.fonts&&document.fonts.ready)document.fonts.ready.then(function(){ST.refresh()});
})();

/* ---------- Playground: the cursor draws, the title stays ---------- */
(function(){
  var sec=document.querySelector('.play'); if(!sec)return;
  var cv=sec.querySelector('.play-canvas'), ctx=cv.getContext('2d'), pen=sec.querySelector('.pen'), btn=sec.querySelector('.reset');
  var pens=[].slice.call(document.querySelectorAll('.pens button'));
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var COLORS=['#FF4B2B','#FFB3D1','#FFD84D','#9FD3FF','#141110','#3DDC97'];
  var dpr=Math.min(2,window.devicePixelRatio||1), W=0, H=0, last=null, mid=null, ci=0, travel=0, drawn=false, fixed=null, wiping=false;
  function size(){
    var r=sec.getBoundingClientRect(), nw=Math.round(r.width), nh=Math.round(r.height); if(nw===W&&nh===H)return;
    var keep=null; if(W&&H&&drawn){keep=document.createElement('canvas');keep.width=cv.width;keep.height=cv.height;keep.getContext('2d').drawImage(cv,0,0)}
    W=nw;H=nh;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);ctx.lineCap='round';ctx.lineJoin='round';
    if(keep)ctx.drawImage(keep,0,0,keep.width/dpr,keep.height/dpr);
  }
  size(); addEventListener('resize',size);
  function color(){return fixed||COLORS[ci%COLORS.length]}
  function setPen(){sec.style.setProperty('--pen',color())}
  setPen();
  pens.forEach(function(b){b.addEventListener('click',function(){pens.forEach(function(o){o.setAttribute('aria-pressed',o===b)});var c=b.getAttribute('data-c');fixed=c==='mix'?null:c;setPen()})});
  function showBtn(){btn.classList.remove('off');btn.classList.add('wiggle');btn.removeAttribute('tabindex');btn.setAttribute('aria-hidden','false')}
  function hideBtn(){btn.classList.add('off');btn.classList.remove('wiggle');btn.setAttribute('tabindex','-1');btn.setAttribute('aria-hidden','true')}
  hideBtn();
  function pos(e){var r=cv.getBoundingClientRect();return {x:e.clientX-r.left,y:e.clientY-r.top,t:performance.now()}}
  function move(e){
    if(wiping||e.target.closest('.reset'))return;
    var p=pos(e); if(pen)pen.style.transform='translate('+p.x+'px,'+p.y+'px)';
    if(e.pointerType!=='mouse'&&e.buttons===0&&e.type!=='pointerdown')return;
    if(!last){last=p;mid=p;return}
    var dx=p.x-last.x,dy=p.y-last.y,d=Math.sqrt(dx*dx+dy*dy); if(d<1.5)return;
    if(d>140){last=p;mid=p;return}
    var speed=d/Math.max(1,p.t-last.t), m={x:(last.x+p.x)/2,y:(last.y+p.y)/2};
    ctx.strokeStyle=color(); ctx.lineWidth=Math.max(3,Math.min(14,14-speed*5));
    ctx.beginPath(); ctx.moveTo(mid.x,mid.y); ctx.quadraticCurveTo(last.x,last.y,m.x,m.y); ctx.stroke();
    mid=m; last=p; travel+=d; if(travel>420){travel=0;ci++;setPen()}
    if(!drawn){drawn=true;sec.classList.add('drawn');showBtn()}
  }
  sec.addEventListener('pointerenter',function(){sec.classList.add('hover');last=null});
  sec.addEventListener('pointerleave',function(){sec.classList.remove('hover');last=null;ci++;setPen()});
  sec.addEventListener('pointermove',move);
  sec.addEventListener('pointerdown',function(e){if(e.target.closest('.reset'))return;last=null;move(e)});
  sec.addEventListener('pointerup',function(e){if(e.pointerType!=='mouse')last=null});
  btn.addEventListener('pointerenter',function(){last=null});
  btn.addEventListener('pointerleave',function(){last=null});
  btn.addEventListener('click',function(e){
    e.stopPropagation(); if(wiping)return; last=null; wiping=true; hideBtn();
    function done(){ctx.clearRect(0,0,W,H);drawn=false;travel=0;wiping=false;last=null;sec.classList.remove('drawn')}
    if(reduce)return done();
    var t0=performance.now(),D=650;
    (function sweep(now){var k=Math.min(1,(now-t0)/D),q=k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2;
      ctx.save();ctx.globalCompositeOperation='destination-out';ctx.fillRect(0,0,W*q,H);ctx.restore();
      if(k<1)requestAnimationFrame(sweep);else done()})(t0);
  });
})();
