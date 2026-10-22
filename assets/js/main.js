/* Rodrigo López · Web Portfolio v3.1 — interactions and animation */
(function(){
  'use strict';
  var root=document.documentElement;
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
    tangle:function(){var c=[],a=rnd(0,6.283),n=42;for(var i=0;i<n;i++){a+=rnd(.9,1.9);var r=rnd(26,64),ox=rnd(-10,10),oy=rnd(-8,8);c.push([CX+ox+Math.cos(a)*r*1.3,CY+oy+Math.sin(a)*r])}return smooth(c,12)},
    spiral:function(){var c=[],a=rnd(0,6.283),turns=rnd(5,7);for(var i=0;i<turns*14;i++){a+=6.283/14;var r=8+i*.62+rnd(-4,4);c.push([CX+Math.cos(a)*r*1.4,CY+Math.sin(a)*r])}return smooth(c,6)},
    zigzag:function(){var c=[],rows=rnd(9,13)|0,x0=CX-80,x1=CX+80,y=CY-52,dy=104/rows;for(var i=0;i<=rows;i++){c.push([i%2?x1+rnd(-8,8):x0+rnd(-8,8),y+i*dy+rnd(-4,4)+(i%2?8:-8)])}
      for(var j=rows;j>=0;j-=2)c.push([CX+rnd(-70,70),CY+rnd(-45,45)]);return smooth(c,10)},
    coil:function(){var c=[],x=CX-95,loops=rnd(6,8)|0,step=190/loops;for(var i=0;i<loops*8;i++){var a=i/8*6.283,r=rnd(20,30);c.push([x+i/8*step+Math.cos(a)*r*.75,CY+Math.sin(a)*r+rnd(-3,3)])}return smooth(c,5)},
    clouds:function(){var c=[],k=rnd(5,7)|0;for(var j=0;j<k;j++){var cx=CX+rnd(-70,70),cy=CY+rnd(-35,35),r=rnd(14,30),a0=rnd(0,6.283);for(var i=0;i<=16;i++){var a=a0+i/14*6.283;c.push([cx+Math.cos(a)*r*rnd(.85,1.15),cy+Math.sin(a)*r*rnd(.85,1.15)])}}return smooth(c,5)},
    burst:function(){var c=[[CX,CY]],n=rnd(14,20)|0;for(var i=0;i<n;i++){var a=rnd(0,6.283),r=rnd(40,80);c.push([CX+Math.cos(a)*r*1.3,CY+Math.sin(a)*r]);c.push([CX+rnd(-14,14),CY+rnd(-12,12)])}return smooth(c,8)}
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
  $$('a[data-go]').forEach(function(a){a.addEventListener('click',function(e){
    if(reduce||e.metaKey||e.ctrlKey||e.shiftKey)return; var href=a.getAttribute('href'); if(!href||href.charAt(0)==='#')return;
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
  if(hasG)G.registerPlugin(ST);
  if(hasG&&window.Lenis){lenis=new window.Lenis({lerp:.1,smoothWheel:true});lenis.on('scroll',ST.update);G.ticker.add(function(t){lenis.raf(t*1000)});G.ticker.lagSmoothing(0)}
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
      var dx=cx-px; if(id!==null){vx=dx;vy=cy-py}
      var targetRot=Math.max(-14,Math.min(14,dx*.9));
      rot+=(targetRot-rot)*.18;
      el.style.transform='translate3d('+cx.toFixed(2)+'px,'+cy.toFixed(2)+'px,0) rotate('+rot.toFixed(2)+'deg)';
      if(id!==null||Math.abs(vx)>.05||Math.abs(vy)>.05||Math.abs(rot)>.05)raf=requestAnimationFrame(frame);
      else{raf=0;tx=cx;ty=cy;rot=0;el.style.transform='translate3d('+cx.toFixed(2)+'px,'+cy.toFixed(2)+'px,0)'}
    }
    function start(){if(!raf)raf=requestAnimationFrame(frame)}
    el.addEventListener('pointerdown',function(e){id=e.pointerId;el.setPointerCapture(id);ox=e.clientX-cx;oy=e.clientY-cy;tx=cx;ty=cy;vx=vy=0;el.classList.add('dragging');el.style.transition='none';start()});
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
      var wrap=toc.parentElement.getBoundingClientRect(),p=Math.min(1,Math.max(0,(mid-wrap.top)/wrap.height));if(bar)bar.style.transform='scaleX('+p+')'}
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
