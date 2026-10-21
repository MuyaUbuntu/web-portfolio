(function(){
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Carruseles */
  document.querySelectorAll('[data-carousel]').forEach(function(c){
    var track=c.querySelector('.track'), slides=[].slice.call(track.children);
    var count=c.querySelector('.count'), bar=c.querySelector('.bar span');
    var total=slides.length, pad=function(n){return String(n).padStart(2,'0')};
    function current(){
      var base=track.getBoundingClientRect().left+parseFloat(getComputedStyle(track).paddingLeft), best=0, d=1e9;
      slides.forEach(function(s,i){var x=Math.abs(s.getBoundingClientRect().left-base);if(x<d){d=x;best=i}});
      return best;
    }
    function update(){
      if(count) count.textContent=pad(current()+1)+' / '+pad(total);
      var max=track.scrollWidth-track.clientWidth; if(bar) bar.style.width=(max>0?(track.scrollLeft/max)*100:100)+'%';
    }
    function go(dir){var i=Math.max(0,Math.min(total-1,current()+dir));track.scrollTo({left:slides[i].offsetLeft-parseFloat(getComputedStyle(track).paddingLeft),behavior:reduce?'auto':'smooth'})}
    var p=c.querySelector('[data-prev]'), n=c.querySelector('[data-next]');
    if(p) p.addEventListener('click',function(){go(-1)});
    if(n) n.addEventListener('click',function(){go(1)});
    track.addEventListener('keydown',function(e){if(e.key==='ArrowRight'){e.preventDefault();go(1)}if(e.key==='ArrowLeft'){e.preventDefault();go(-1)}});
    track.addEventListener('scroll',update,{passive:true});
    var down=false,startX=0,startS=0,moved=false;
    track.addEventListener('pointerdown',function(e){if(e.pointerType!=='mouse')return;down=true;moved=false;startX=e.clientX;startS=track.scrollLeft;track.classList.add('dragging')});
    window.addEventListener('pointermove',function(e){if(!down)return;var dx=e.clientX-startX;if(Math.abs(dx)>3)moved=true;track.scrollLeft=startS-dx});
    window.addEventListener('pointerup',function(){if(!down)return;down=false;track.classList.remove('dragging');if(moved)go(0)});
    track.addEventListener('dragstart',function(e){e.preventDefault()});
    update(); window.addEventListener('resize',update);
  });

  /* Antes / después */
  document.querySelectorAll('.ba').forEach(function(b){
    var r=b.querySelector('input');
    function set(){b.style.setProperty('--pos',r.value+'%')}
    r.addEventListener('input',set); set();
  });

  /* Línea del pipeline (visible por defecto, se redibuja al entrar) */
  if('IntersectionObserver' in window && !reduce){
    var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('run');io.unobserve(en.target)}})},{threshold:.6});
    document.querySelectorAll('.flow').forEach(function(f){io.observe(f)});
  }

  /* Cursor personalizado */
  var cur=document.getElementById('cursor'), lab=document.getElementById('cursorLabel');
  if(cur && window.matchMedia('(pointer:fine)').matches && !reduce){
    document.documentElement.classList.add('has-cursor');
    var x=-100,y=-100,cx=x,cy=y;
    window.addEventListener('pointermove',function(e){x=e.clientX;y=e.clientY});
    (function loop(){cx+=(x-cx)*.22;cy+=(y-cy)*.22;cur.style.transform='translate('+cx+'px,'+cy+'px)';requestAnimationFrame(loop)})();
    document.addEventListener('pointerover',function(e){
      var t=e.target;
      if(t.closest('.track')){cur.className='cursor big';lab.textContent='Arrastra'}
      else if(t.closest('.ba')){cur.className='cursor big';lab.textContent='Desliza'}
      else if(t.closest('.card,.next,.pc')){cur.className='cursor big';lab.textContent='Ver caso'}
      else if(t.closest('.burger')){cur.className='cursor'}
      else if(t.closest('a,button')){cur.className='cursor link'}
      else{cur.className='cursor'}
    });
    document.documentElement.addEventListener('pointerleave',function(){cur.style.opacity='0'});
    document.documentElement.addEventListener('pointerenter',function(){cur.style.opacity=''});
  }

  /* Copiar correo */
  var btn=document.getElementById('copy'), mail=document.getElementById('mail');
  if(btn && mail){
    btn.addEventListener('click',function(){
      var done=function(){btn.textContent='Correo copiado';setTimeout(function(){btn.textContent='Copiar correo'},1800)};
      var fallback=function(){var r=document.createRange();r.selectNodeContents(mail);var s=getSelection();s.removeAllRanges();s.addRange(r);btn.textContent='Selecciona y copia'};
      try{navigator.clipboard.writeText(mail.textContent).then(done,fallback)}catch(e){fallback()}
    });
  }
})();

/* ===== V3 · capa dinámica ===== */
(function(){
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var vh=function(){return window.innerHeight};

  /* Contadores: solo animan los que están fuera de pantalla al cargar */
  var nums=[].slice.call(document.querySelectorAll('[data-counters] b'));
  function animate(el){
    var txt=el.getAttribute('data-final')||el.textContent;el.setAttribute('data-final',txt);
    var m=txt.match(/^([^\d]*)([\d.,]+)(.*)$/); if(!m) return;
    var target=parseFloat(m[2].replace(/,/g,'')), dec=(m[2].split('.')[1]||'').length, t0=null, dur=1300;
    function step(t){if(!t0)t0=t;var k=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-k,3);
      el.textContent=m[1]+(target*e).toFixed(dec)+m[3]; if(k<1)requestAnimationFrame(step); else el.textContent=txt;}
    requestAnimationFrame(step);
  }
  if(!reduce && 'IntersectionObserver' in window){
    var co=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){animate(en.target);co.unobserve(en.target)}})},{threshold:.6});
    nums.forEach(function(n){if(n.getBoundingClientRect().top>vh())co.observe(n)});

    /* Reveal suave para lo que está debajo del pliegue */
    var rv=[].slice.call(document.querySelectorAll('.rv'));
    var ro=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.remove('pre');ro.unobserve(en.target)}})},{threshold:.15});
    rv.forEach(function(el){if(el.getBoundingClientRect().top>vh()){el.classList.add('pre');ro.observe(el)}});
  }

  /* Tarjetas apiladas: la de atrás se encoge y oscurece */
  var sts=[].slice.call(document.querySelectorAll('.st'));
  function stack(){
    sts.forEach(function(st,i){
      var card=st.querySelector('.pc'), next=sts[i+1]; if(!next){card.style.transform='';card.style.filter='';return}
      var a=st.getBoundingClientRect().top, b=next.getBoundingClientRect().top, h=st.offsetHeight;
      var p=Math.max(0,Math.min(1,1-(b-a)/h));
      card.style.transform='scale('+(1-p*.07)+')'; card.style.filter='brightness('+(1-p*.45)+')';
    });
  }

  /* Polaroids del hero siguen al mouse */
  var fls=[].slice.call(document.querySelectorAll('.fl'));
  if(fls.length && !reduce && window.matchMedia('(pointer:fine)').matches){
    window.addEventListener('pointermove',function(e){
      var dx=(e.clientX/innerWidth-.5), dy=(e.clientY/innerHeight-.5);
      fls.forEach(function(f,i){var d=(i%2?1:-1)*(14+i*6);f.style.setProperty('--px',(dx*d)+'px');f.style.setProperty('--py',(dy*d)+'px')});
    });
  }

  /* El sello se oculta sobre el contacto */
  var seal=document.querySelector('.seal'), contact=document.getElementById('contacto');
  function sealVis(){if(!seal||!contact)return;seal.classList.toggle('hide',contact.getBoundingClientRect().top<vh()*.8)}

  if(!reduce){window.addEventListener('scroll',function(){stack();sealVis()},{passive:true});stack()}
  sealVis();
})();

/* Lente de peso: la letra bajo el cursor pasa a light y el efecto se desvanece hacia las vecinas */
window.__lens=[];
document.querySelectorAll('[data-lens]').forEach(function(h){
  var src=h.querySelector('.lens-txt'); if(!src) return;
  var lines=src.innerHTML.split(/<br\s*\/?>/i).map(function(l){return l.trim()});
  var frag=document.createDocumentFragment();
  lines.forEach(function(l){var ln=document.createElement('span');ln.className='ln';ln.setAttribute('aria-hidden','true');
    Array.from(l).forEach(function(c){var s=document.createElement('span');s.className='ch';s.textContent=c===' '?'\u00a0':c;ln.appendChild(s)});frag.appendChild(ln)});
  h.replaceChildren(frag);
  var chars=[].slice.call(h.querySelectorAll('.ch')), BOLD=850, LIGHT=200, centers=[];
  function measure(){
    chars.forEach(function(c){c.style.width='';c.style.setProperty('--w',BOLD)});
    chars.forEach(function(c){c.style.width=c.getBoundingClientRect().width+'px'});
    var hr=h.getBoundingClientRect();
    centers=chars.map(function(c){var r=c.getBoundingClientRect();return {x:r.left-hr.left+r.width/2,y:r.top-hr.top+r.height/2,w:r.width,h:r.height}});
  }
  function move(e){
    var hr=h.getBoundingClientRect(), x=e.clientX-hr.left, y=e.clientY-hr.top;
    centers.forEach(function(c,i){
      var dx=(x-c.x)/(c.w*2.6), dy=(y-c.y)/(c.h*.9);
      var d=Math.sqrt(dx*dx+dy*dy), k=Math.max(0,1-d); k=k*k*(3-2*k);
      chars[i].style.setProperty('--w',Math.round(BOLD-(BOLD-LIGHT)*k));
    });
  }
  function out(){chars.forEach(function(c){c.style.setProperty('--w',BOLD)})}
  measure(); if(document.fonts&&document.fonts.ready) document.fonts.ready.then(measure); window.addEventListener('resize',measure);
  h.addEventListener('pointermove',move);h.addEventListener('pointerdown',move);
  h.addEventListener('pointerleave',out);h.addEventListener('pointerup',function(e){if(e.pointerType!=='mouse')out()});h.addEventListener('pointercancel',out);
  window.__lens.push(measure);
});

/* Trazos a mano: cada hover usa una variante distinta */
(function(){
  var V=[
    'M2 12 C40 5 80 17 120 10 S178 7 198 11',
    'M2 16 Q100 1 198 8',
    'M3 8 C60 12 140 4 196 9 M12 16 C70 19 130 13 188 16',
    'M2 12 C50 12 120 13 160 11 C190 9 193 2 179 4 C165 6 171 16 198 15',
    'M2 10 L40 14 L80 8 L120 14 L160 8 L198 12',
    'M2 9 C60 7 140 7 184 9 C196 10 197 17 185 18'
  ], n=Math.floor(Math.random()*V.length);
  document.querySelectorAll('a.hl').forEach(function(a){
    var p=a.querySelector('.stroke path'); p.setAttribute('d',V[n%V.length]);
    function next(){n=(n+1)%V.length;p.style.transition='none';p.setAttribute('d',V[n]);p.getBoundingClientRect();p.style.transition=''}
    a.addEventListener('pointerleave',function(){setTimeout(next,520)});
    a.addEventListener('blur',function(){setTimeout(next,520)});
  });
})();

/* Burger: líneas → círculo (hover) → X (abierto), con morph elástico */
(function(){
  var btn=document.getElementById('burger'), menu=document.getElementById('menu'); if(!btn||!menu) return;
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var P=[].slice.call(btn.querySelectorAll('path'));
  function ln(y){return [4,y, 7.33,y, 10.67,y, 14,y, 17.33,y, 20.67,y, 24,y]}
  var k=4.97, S={
    lines:[ln(8),ln(14),ln(20)],
    circle:[[5,14, 5,14-k, 14-k,5, 14,5, 14+k,5, 23,14-k, 23,14],
            [14,14, 14,14, 14,14, 14,14, 14,14, 14,14, 14,14],
            [5,14, 5,14+k, 14-k,23, 14,23, 14+k,23, 23,14+k, 23,14]],
    x:[[6,6, 8.67,8.67, 11.33,11.33, 14,14, 16.67,16.67, 19.33,19.33, 22,22],
       [14,14, 14,14, 14,14, 14,14, 14,14, 14,14, 14,14],
       [6,22, 8.67,19.33, 11.33,16.67, 14,14, 16.67,11.33, 19.33,8.67, 22,6]]
  };
  var cur=S.lines.map(function(a){return a.slice()}), from=null, to=null, t0=0, raf=0, DUR=620;
  function d(a){return 'M'+a[0]+' '+a[1]+'C'+a.slice(2,8).join(' ')+'C'+a.slice(8,14).join(' ')}
  function draw(){P.forEach(function(p,i){p.setAttribute('d',d(cur[i]))})}
  function ease(t){var c=1.45;return 1+(c+1)*Math.pow(t-1,3)+c*Math.pow(t-1,2)} /* easeOutBack: rebote orgánico */
  function go(name){
    to=S[name]; from=cur.map(function(a){return a.slice()}); t0=performance.now(); cancelAnimationFrame(raf);
    if(reduce){cur=to.map(function(a){return a.slice()});draw();return}
    (function step(now){
      var t=Math.min(1,(now-t0)/DUR), e=ease(t);
      cur=from.map(function(a,i){return a.map(function(v,j){
        var w=Math.sin((j/13)*Math.PI)*(1-t)*.9*(i===1?0:1); /* leve onda durante el cambio */
        return v+(to[i][j]-v)*e+(j%2?w:0)})});
      draw(); if(t<1) raf=requestAnimationFrame(step);
    })(t0);
  }
  draw();
  var open=false, hover=false;
  function state(){go(open?'x':(hover?'circle':'lines'))}
  btn.addEventListener('pointerenter',function(e){if(e.pointerType==='mouse'){hover=true;state()}});
  btn.addEventListener('pointerleave',function(e){if(e.pointerType==='mouse'){hover=false;state()}});
  function setOpen(v){
    open=v; var r=btn.getBoundingClientRect();
    menu.style.setProperty('--ox',(r.left+r.width/2)+'px'); menu.style.setProperty('--oy',(r.top+r.height/2)+'px');
    document.documentElement.classList.toggle('menu-open',v);
    btn.setAttribute('aria-expanded',v); btn.setAttribute('aria-label',v?'Cerrar menú':'Abrir menú'); menu.setAttribute('aria-hidden',!v);
    if(v){(window.__lens||[]).forEach(function(m){m()}); setTimeout(function(){var a=menu.querySelector('a');a&&a.focus({preventScroll:true})},400)}
    else btn.focus({preventScroll:true});
    state();
  }
  btn.addEventListener('click',function(){setOpen(!open)});
  menu.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){setOpen(false)})});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&open)setOpen(false)});
})();
