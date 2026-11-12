/* Hero X: the discipline index drives the image stage. Hover/focus picks one; otherwise it cycles. */
(function(){
  var root=document.querySelector('.hx'); if(!root) return;
  var items=[].slice.call(root.querySelectorAll('.hx-list li')), imgs=[].slice.call(root.querySelectorAll('.hx-frame img'));
  var capT=root.querySelector('.hx-cap b'), capN=root.querySelector('.hx-cap span'), bar=root.querySelector('.hx-bar');
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches, i=0, timer=null, hold=false, DUR=4200;
  function show(k){
    i=(k+items.length)%items.length;
    items.forEach(function(li,j){li.classList.toggle('on',j===i)});
    imgs.forEach(function(im,j){im.classList.toggle('on',j===i)});
    capT.textContent=items[i].dataset.project; capN.textContent=String(i+1).padStart(2,'0')+' / '+String(items.length).padStart(2,'0');
    if(bar&&!reduce){bar.style.transition='none';bar.style.width='0';void bar.offsetWidth;if(!hold){bar.style.transition='width '+DUR+'ms linear';bar.style.width='100%';}}
  }
  function run(){clearInterval(timer);if(reduce)return;timer=setInterval(function(){if(!hold)show(i+1)},DUR)}
  items.forEach(function(li,j){
    var a=li.querySelector('a');
    a.addEventListener('mouseenter',function(){hold=true;show(j)});
    a.addEventListener('focus',function(){hold=true;show(j)});
    a.addEventListener('mouseleave',function(){hold=false;show(j);run()});
    a.addEventListener('blur',function(){hold=false;run()});
  });
  show(0); run();
})();
