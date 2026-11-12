/* Home hero: "the headline is the piece". Builds the hero inside a shadow root (isolated from main.css / minimal.css). */
(function(){
"use strict";
var host=document.getElementById("hx-host");if(!host||!host.attachShadow)return;
var R=host.attachShadow({mode:"open"});
R.innerHTML='<link rel="stylesheet" href="assets/hero/hero.css">'+"<section class=\"hero\" id=\"hero\">\n  <div class=\"meta\"><div>Rodrigo L\u00f3pez<b>Designer &amp; art director</b></div><div>Based in<b>Mexico \u00b7 Remote</b></div><div>Practice<b>10+ years, since 2016</b></div><div class=\"live\">Status<b>Open to projects &amp; roles</b></div></div>\n\n  <div class=\"stage\" id=\"stage\">\n    <div class=\"bg\"></div>\n    <span class=\"mode-tag\" id=\"tag\"></span>\n    <h1 class=\"rows\" id=\"rows\" aria-label=\"Creative ideas, big results.\">\n      <span class=\"row\"><span class=\"tx\"><span class=\"w w1\">Creative</span> <span class=\"w w2\"><em>ideas,</em></span></span></span>\n      <span class=\"row\"><span class=\"tx\"><span class=\"w w3\">big results.</span><span class=\"reg\">\u00ae</span></span></span>\n    </h1>\n    <div class=\"deco\" id=\"deco\">\n      <div class=\"bb\" id=\"bb\"></div>\n      <div class=\"ad\" id=\"ad\"></div>\n      <div class=\"ai\" id=\"ai\"><div class=\"pbox\" id=\"pbox\"><div class=\"ph empty\" id=\"ph\">Describe a style for the headline\u2026</div><div class=\"rowb\"><span class=\"chip\"><i></i>Image model \u00b7 v7</span><span class=\"chip\" id=\"ratio\">16:9</span><span class=\"gen\" id=\"gen\">Generating\u2026</span><span class=\"go\" id=\"go\"><svg viewBox=\"0 0 16 16\"><path d=\"M8 13V3M3.5 7.5 8 3l4.5 4.5\"/></svg></span></div></div></div>\n      <div class=\"stk\" id=\"stk\"></div>\n      <div class=\"fig\" id=\"fig\">\n        <span class=\"frame-l\">Hero / Desktop \u2014 1440</span>\n        <div class=\"sel\" id=\"sel\"><i></i><i></i><i></i><i></i><b id=\"selb\"></b></div>\n        <div class=\"cursor\" id=\"c1\" style=\"--c:#0d99ff\"><svg viewBox=\"0 0 18 18\"><path d=\"M1 1l6 15 2.5-6.5L16 7z\" fill=\"#0d99ff\" stroke=\"#fff\" stroke-width=\"1.2\"/></svg><span>Rodrigo</span></div>\n        <div class=\"cursor\" id=\"c2\" style=\"--c:#e9437a\"><svg viewBox=\"0 0 18 18\"><path d=\"M1 1l6 15 2.5-6.5L16 7z\" fill=\"#e9437a\" stroke=\"#fff\" stroke-width=\"1.2\"/></svg><span>Client</span></div>\n        <div class=\"cursor\" id=\"c3\" style=\"--c:#14ae5c\"><svg viewBox=\"0 0 18 18\"><path d=\"M1 1l6 15 2.5-6.5L16 7z\" fill=\"#14ae5c\" stroke=\"#fff\" stroke-width=\"1.2\"/></svg><span>Dev</span></div>\n        <div class=\"cmt\" id=\"cmt\"><span class=\"pin\">CL</span><span class=\"bub\"><b>Client</b>Love this headline \u2726</span></div>\n      </div>\n      <svg width=\"0\" height=\"0\" style=\"position:absolute\" aria-hidden=\"true\"><filter id=\"dream\" x=\"-10%\" y=\"-10%\" width=\"120%\" height=\"120%\"><feTurbulence id=\"dturb\" type=\"fractalNoise\" baseFrequency=\"0.008 0.03\" numOctaves=\"1\" seed=\"3\" result=\"n\"/><feDisplacementMap id=\"ddisp\" in=\"SourceGraphic\" in2=\"n\" scale=\"0\" xChannelSelector=\"R\" yChannelSelector=\"G\" result=\"d\"/><feGaussianBlur id=\"dblur\" in=\"d\" stdDeviation=\"0\"/></filter></svg><div class=\"d3\" id=\"d3\"><div class=\"rig\" id=\"rig\"></div></div><div class=\"x3\"><div class=\"rig3\" id=\"rig3\"></div></div>\n      <div class=\"vid\" id=\"vid\"></div>\n    </div>\n  </div>\n\n  <div class=\"bar\">\n    <p class=\"intro\">Campaigns and visual systems for global brands, from the first sketch to production. <b>Slide or tap a discipline</b> and the headline takes its form.</p>\n    <div class=\"sl\" id=\"sl\">\n      <div class=\"sl-hint\"><span>\u2190 Drag to switch discipline \u2192</span><span id=\"cnt\">01 / 07</span></div>\n      <div class=\"sl-track\" id=\"track\" role=\"tablist\" aria-label=\"Disciplines\"><div class=\"sl-thumb\" id=\"thumb\"><i></i></div></div>\n    </div>\n  </div>\n</section>";
var css=R.querySelector("link");function boot(){
(function(){
"use strict";
var reduce=matchMedia("(prefers-reduced-motion: reduce)").matches;
var M=[
 {k:"ui",t:"UX/UI",d:"Live in a Figma file",dur:8000},
 {k:"ai",t:"AI imagery",d:"A prompt restyles the headline",dur:22400},
 {k:"brand",t:"Brand systems",d:"Brand guidelines · page 04",dur:7000},
 {k:"art",t:"Art direction",d:"Live review and type exploration",dur:9000},
 {k:"vid",t:"AI video",d:"An edit timeline animates each word",dur:8000},
 {k:"int",t:"Internal campaigns",d:"A wall that gets stickered",dur:6500},
 {k:"3d",t:"3D",d:"Extruded in real time · move your cursor",dur:8000}
];
var stage=R.getElementById("stage"),rowsEl=R.getElementById("rows"),rows=[].slice.call(rowsEl.querySelectorAll(".row")),words=[].slice.call(rowsEl.querySelectorAll(".w"));
var track=R.getElementById("track"),thumb=R.getElementById("thumb"),cnt=R.getElementById("cnt"),tag=R.getElementById("tag");
track.insertAdjacentHTML("beforeend",M.map(function(m,i){return '<button type="button" role="tab" aria-selected="false" data-i="'+i+'"><span>'+String(i+1).padStart(2,"0")+'</span><b>'+m.t+'</b></button>'}).join(""));
var btns=[].slice.call(track.querySelectorAll("button")),cur=-1,timer=null,hold=false,subs=[],busy=false,pend=-1;

function fit(){
  var W=stage.clientWidth,f=1e9;rows.forEach(function(r){r.style.fontSize="100px"});
  rows.forEach(function(r){var w=r.querySelector(".tx").getBoundingClientRect().width;f=Math.min(f,100*W/w*.995)});
  if(stage.classList.contains("m-int"))f*=.9;
  if(stage.classList.contains("m-art"))f*=.92;
  rows.forEach(function(r){r.style.fontSize=f+"px"});return f;
}
function wbox(el){var S=stage.getBoundingClientRect(),b=el.getBoundingClientRect();return {x:b.left-S.left,y:b.top-S.top,w:b.width,h:b.height}}
function clearSubs(){subs.forEach(function(f){f()});subs=[]}
function every(fn,ms){var id=setInterval(fn,ms);subs.push(function(){clearInterval(id)});return id}
function after(fn,ms){var id=setTimeout(fn,ms);subs.push(function(){clearTimeout(id)});return id}
function moveThumb(i){thumb.style.transform="translateX("+(i*100)+"%)"}

function show(i,instant){
  if(i===cur)return;if(busy){pend=i;return}var go=function(){
    cur=i;clearSubs();var m=M[i];
    stage.className="stage m-"+m.k;
    words.forEach(function(w){w.className=w.className.replace(/\b(alt1|slap|hit)\b/g,"").trim();w.style.cssText=""});
    tag.textContent=String(i+1).padStart(2,"0")+" · "+m.t+" — "+m.d;cnt.textContent=String(i+1).padStart(2,"0")+" / 07";
    btns.forEach(function(b,j){b.setAttribute("aria-selected",j===i)});moveThumb(i);
    thumb.style.setProperty("--dur",m.dur+"ms");thumb.classList.remove("run");void thumb.offsetWidth;if(!hold&&!reduce)thumb.classList.add("run");
    fit();
    ({brand:runBrand,art:runArt,ai:runAI,int:runInt,ui:runUI,"3d":run3D,vid:runVid}[m.k])();
    requestAnimationFrame(function(){stage.classList.remove("out")});
    schedule();busy=false;if(pend>=0){var q=pend;pend=-1;if(q!==cur)show(q)}
  };
  if(instant||cur<0||reduce){go();return}
  busy=true;stage.classList.add("out");setTimeout(go,320);
}
function schedule(){clearTimeout(timer);if(reduce||hold)return;timer=setTimeout(function(){show((cur+1)%M.length)},M[cur].dur)}

/* ---------- 1 · brandbook ---------- */
function runBrand(){
  var bb=R.getElementById("bb"),S=stage.getBoundingClientRect(),W=S.width,H=S.height;
  function lb(w,i){var n=w.querySelector("em")?w.querySelector("em").firstChild:w.firstChild,r=document.createRange();r.setStart(n,i);r.setEnd(n,i+1);var b=r.getBoundingClientRect();return {x:b.left-S.left,y:b.top-S.top,w:b.width,h:b.height}}
  var fs=parseFloat(rows[0].style.fontSize),r0=wbox(words[0]),r2=wbox(words[2]);
  var cap0=r0.y+r0.h*.2,base0=r0.y+r0.h*.84,x0=r0.y+r0.h*.39,base1=r2.y+r2.h*.84,x1=r2.y+r2.h*.39,cap1=r2.y+r2.h*.2;
  var C=lb(words[0],0),e=lb(words[0],2),a=lb(words[1],3),g=lb(words[2],2),o=lb(words[2],4);
  var out="",k=0;
  function circ(cx,cy,r){k++;return '<circle class="cn draw" style="--len:'+(6.3*r+4)+';transition-delay:'+(k*.07)+'s" cx="'+cx+'" cy="'+cy+'" r="'+r+'"/>'}
  function ln(x1,y1,x2,y2){k++;return '<path class="cn draw" style="--len:'+(Math.hypot(x2-x1,y2-y1)+2)+';transition-delay:'+(k*.05)+'s" d="M'+x1+' '+y1+'L'+x2+' '+y2+'"/>'}
  [cap0,x0,base0,cap1,x1,base1].forEach(function(y){out+=ln(-10,y,W+10,y)});
  // construction circles on key letters
  var cr=(base0-cap0)/2;out+=circ(C.x+C.w*.55,(cap0+base0)/2,cr)+circ(C.x+C.w*.55,(cap0+base0)/2,cr*.62);
  var xr=(base0-x0)/2;out+=circ(e.x+e.w/2,x0+xr,xr)+circ(a.x+a.w/2,x0+xr,xr);
  var xr1=(base1-x1)/2;out+=circ(g.x+g.w/2,x1+xr1,xr1)+circ(g.x+g.w/2,base1+xr1*.55,xr1*.7)+circ(o.x+o.w/2,x1+xr1,xr1);
  [C.x,C.x+C.w,a.x+a.w,g.x,o.x+o.w].forEach(function(x){out+=ln(x,cap0-fs*.12,x,base1+fs*.1)});
  var svg='<svg viewBox="0 0 '+W+' '+H+'">'+out+
   '<text class="gl fade" x="'+(W)+'" y="'+(cap0-5)+'" text-anchor="end">Cap height</text><text class="gl fade" x="'+(W)+'" y="'+(x0-5)+'" text-anchor="end">x-height</text><text class="gl fade" x="'+(W)+'" y="'+(base0-5)+'" text-anchor="end">Baseline</text></svg>';
  var spx=r2.x+r2.w+fs*.35,spw=W-spx;
  var spec=spw>220?'<div class="spec fade" style="left:'+spx+'px;top:'+(r2.y+r2.h*.08)+'px;width:'+Math.min(spw,380)+'px"><small>Primary typeface: Inter Tight</small><div class="sa">Regular <i>Italic</i></div><p>ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz<br>0123456789 — &amp;@%</p></div>':'';
  var cols=[["#F7F7F5","Paper","#141414"],["#ECEBE6","Bone","#141414"],["#D9D8D2","Stone","#141414"],["#BDBCB6","Ash","#141414"],["#9A9994","Smoke","#fff"],["#6E6D69","Slate","#fff"],["#3A3A38","Graphite","#fff"],["#141414","Ink","#fff"],["#FF4417","Signal","#fff"]];
  bb.innerHTML='<div class="hd"><b>2.1</b><span>Typography<br>&amp; construction</span><em>Rodrigo López<br>Brand guidelines · v2.1</em></div>'+svg+spec+
   '<div class="strip">'+cols.map(function(c,j){return '<div style="--c:'+c[0]+';--t:'+c[2]+';transition-delay:'+(.5+j*.06)+'s"><b>'+(j+1)+'</b><span>'+c[1]+'<br>'+c[0]+'</span></div>'}).join("")+'</div>';
  after(function(){stage.classList.add("on")},60);
  subs.push(function(){stage.classList.remove("on");bb.innerHTML=""});
}

/* ---------- 2 · art direction ---------- */
function runArt(){
  var ad=R.getElementById("ad"),S=stage.getBoundingClientRect(),SW=S.width,mob=SW<600;
  ad.innerHTML='<svg viewBox="0 0 '+SW+' '+S.height+'" style="inset:0;width:100%;height:100%"><path/><path/><path/><path/></svg>'+
   '<span class="note"></span><span class="note">hand-made feel ✓</span><span class="note">'+(mob?'more weight · tighten kerning':'more weight<br>tighten kerning')+'</span>'+
   '<div class="opts"><span>Inter</span><span>Instrument</span><span class="on">Fraunces</span></div><span class="drop" id="drop"></span>';
  if(mob)ad.querySelectorAll(".note")[1].style.display="none";
  var paths=[].slice.call(ad.querySelectorAll("path")),notes=[].slice.call(ad.querySelectorAll(".note")),opts=ad.querySelector(".opts"),drop=R.getElementById("drop"),spans=opts.querySelectorAll("span");
  var faces=[['"Inter Tight",sans-serif',"normal","Inter Tight","too neutral? try a serif"],['"Instrument Serif",serif',"italic","Instrument","elegant, but needs weight"],['"Fraunces",serif',"italic","Fraunces","serif? italic 700 ✓"]],fi=2;
  notes[0].textContent=faces[fi][3];
  function place(n,x,y){n.style.left=x+"px";n.style.top=y+"px";var w=n.offsetWidth;if(x+w>SW-4)n.style.left=Math.max(0,SW-4-w)+"px"}
  function layout(){
    var b1=wbox(words[0]),b2=wbox(words[1]),b3=wbox(words[2]);
    b2.w=Math.min(b2.x+b2.w,SW-12)-b2.x;
    var arrow="M"+(b1.x+b1.w*.55)+" "+(b1.y+b1.h*.05)+" C "+(b1.x+b1.w*.6)+" "+(b1.y-30)+", "+(b1.x+b1.w*.85)+" "+(b1.y-34)+", "+(b1.x+b1.w*.95)+" "+(b1.y-6)+" M"+(b1.x+b1.w*.95-12)+" "+(b1.y-14)+" L"+(b1.x+b1.w*.95)+" "+(b1.y-6)+" L"+(b1.x+b1.w*.95+4)+" "+(b1.y-20);
    var circ="M"+(b2.x-10)+" "+(b2.y+b2.h*.5)+" C "+(b2.x-10)+" "+(b2.y-8)+", "+(b2.x+b2.w+16)+" "+(b2.y-4)+", "+(b2.x+b2.w+10)+" "+(b2.y+b2.h*.55)+" C "+(b2.x+b2.w+4)+" "+(b2.y+b2.h+10)+", "+(b2.x-6)+" "+(b2.y+b2.h+6)+", "+(b2.x+18)+" "+(b2.y+b2.h*.1);
    var under="M"+(b3.x)+" "+(b3.y+b3.h*.94)+" Q "+(b3.x+b3.w*.5)+" "+(b3.y+b3.h*1.02)+", "+(b3.x+b3.w)+" "+(b3.y+b3.h*.9);
    var kern="M"+(b3.x+b3.w*.22)+" "+(b3.y+b3.h*.15)+" L"+(b3.x+b3.w*.24)+" "+(b3.y+b3.h*.8)+" M"+(b3.x+b3.w*.2)+" "+(b3.y+b3.h*.15)+" L"+(b3.x+b3.w*.28)+" "+(b3.y+b3.h*.15);
    [arrow,circ,under,"M0 0"].forEach(function(d,j){paths[j].setAttribute("d",d);paths[j].style.setProperty("--len",paths[j].getTotalLength())});
    place(notes[0],b1.x+b1.w*.62,b1.y-56);
    place(notes[1],b2.x+b2.w*.35,b2.y+b2.h+12);
    if(mob)place(notes[2],SW,b3.y+b3.h+14);else place(notes[2],b3.x+b3.w+20,b3.y+b3.h*.3);
    if(!opts.style.top){opts.style.left=b1.x+"px";opts.style.top=(b1.y-26)+"px"}
    drop.style.left=(drop.classList.contains("go")?b3.x+b3.w*.5:b3.x)+"px";drop.style.top=(drop.classList.contains("go")?b3.y-30:b3.y)+"px";
  }
  layout();
  var seq=[function(){opts.classList.add("go")},function(){paths[0].classList.add("go")},function(){notes[0].classList.add("go")},function(){paths[1].classList.add("go")},function(){notes[1].classList.add("go")},function(){paths[2].classList.add("go")},function(){notes[2].classList.add("go")},
   function(){drop.classList.add("go");drop.style.background="#FF4417";layout()},function(){words[2].classList.add("alt1")}];
  if(reduce){seq.forEach(function(f){f()});return}
  seq.forEach(function(f,k){after(f,120+k*340)});
  // type exploration: the font changes, the red note says why, the marks follow the new shapes
  var cols=["#FF4417","#2457ff","#7c3aed"],ci=0;
  function swap(){
    fi=(fi+1)%3;var f=faces[fi];ci=(ci+1)%3;
    spans.forEach(function(s,j){s.classList.toggle("on",j===fi)});
    notes[0].classList.remove("go");paths[0].classList.remove("go");
    words[0].classList.add("morph");words[2].style.color=cols[ci];drop.style.background=cols[ci];
    after(function(){words[0].style.fontFamily=f[0];words[0].style.fontStyle=f[1];
      requestAnimationFrame(function(){words[0].classList.remove("morph");layout();notes[0].textContent=f[3];place(notes[0],parseFloat(notes[0].style.left),parseFloat(notes[0].style.top));
        after(function(){layout();paths[0].classList.add("go");notes[0].classList.add("go")},250)})},420);
  }
  after(function(){swap();every(swap,2200)},3400);
  var ro=function(){layout()};addEventListener("resize",ro);words[0].addEventListener("transitionend",ro);
  subs.push(function(){ad.innerHTML="";removeEventListener("resize",ro);words[0].removeEventListener("transitionend",ro)});
}

/* ---------- 3 · AI imagery ---------- */
var P=[["assets/hero/img/3d1.jpg","3D headline made of soft pastel fur, pink, violet and aqua, studio light"],["assets/hero/img/3d2.jpg","glossy ripe strawberries shaped into the letters, tiny leaves on top"],["assets/hero/img/3d3.jpg","letters built from fresh broccoli florets on a white table"],["assets/hero/img/3d4.jpg","hand-piped lime-green guacamole lettering, top view"]];
var aiK=0,aiImg=null;
function runAI(){
  var rig=R.getElementById("rig"),W=stage.clientWidth,ph=R.getElementById("ph"),go=R.getElementById("go"),gen=R.getElementById("gen");
  var iw=W<600?W/0.82:W/0.9*0.8;rig.style.width=iw+"px";rig.style.height=(iw*.5625)+"px";
  P.forEach(function(p){var i=new Image();i.src=p[0]});
  function el(u,base){var d=document.createElement("div");d.className="im"+(base?" base":"");d.style.backgroundImage="url("+u+")";
    d.style.setProperty("--mx",(25+Math.random()*50)+"%");d.style.setProperty("--my",(30+Math.random()*40)+"%");rig.appendChild(d);return d}
  if(aiImg){el(aiImg,true);stage.classList.add("has-img")}
  var turb=R.getElementById("dturb"),disp=R.getElementById("ddisp"),blur=R.getElementById("dblur"),draf;
  subs.push(function(){cancelAnimationFrame(draf);rig.style.filter="";rowsEl.style.filter="";rowsEl.style.opacity=""});
  function apply(u){var n=el(u);var txtOn=!stage.classList.contains("has-img");aiImg=u;
    var olds=[].slice.call(rig.querySelectorAll(".im")).filter(function(x){return x!==n}),first=!olds.length&&!stage.querySelector(".m-ai .rows[style]");
    var hadText=!rig.querySelector(".im.base")&&olds.length===0;
    if(reduce){stage.classList.add("has-img");n.style.opacity=1;olds.forEach(function(o){o.remove()});return}
    var D=1900,t0=performance.now(),seed=Math.random()*100;rig.style.filter="url(#dream)";
    var txt=txtOn&&!reduce?rowsEl:null;if(txt)txt.style.filter="url(#dream)";else stage.classList.add("has-img");
    (function f(now){var t=Math.min(1,(now-t0)/D),w=Math.sin(Math.PI*t),e=t*t*(3-2*t);
      disp.setAttribute("scale",(w*w*90).toFixed(1));blur.setAttribute("stdDeviation",(w*w*7).toFixed(2));
      var ph=(now-t0)/1000;turb.setAttribute("baseFrequency",(0.006+0.004*Math.sin(ph*3)).toFixed(4)+" "+(0.03+0.012*Math.cos(ph*2.3)).toFixed(4));turb.setAttribute("seed",Math.floor(seed+ph*6));
      var o=Math.min(1,Math.max(0,(t-.3)/.4));n.style.opacity=o*o*(3-2*o);n.style.transform="scale("+(1.06-.06*e)+")";
      if(txt)txt.style.opacity=1-o;
      olds.forEach(function(x){x.style.opacity=1-o;x.style.transform="scale("+(1+.05*e)+")"});
      if(t<1)draf=requestAnimationFrame(f);else{rig.style.filter="";if(txt){txt.style.filter="";txt.style.opacity="";stage.classList.add("has-img")}olds.forEach(function(x){x.remove()});n.classList.add("base");n.style.transform=""}})(t0);
  }
  function one(){
    var p=P[aiK%P.length],n=0,fast=!aiImg;aiK++;ph.classList.remove("empty");go.classList.remove("ready");
    if(reduce){ph.textContent=p[1];apply(p[0]);return}
    var id=every(function(){n++;ph.innerHTML=p[1].slice(0,n)+'<span class="c"></span>';if(n>=p[1].length){clearInterval(id);go.classList.add("ready");
      after(function(){gen.classList.add("on");go.classList.remove("ready")},fast?150:450);
      after(function(){apply(p[0]);gen.classList.remove("on")},fast?450:1200);
    }},fast?14:30);
  }
  one();every(one,5600);
  subs.push(function(){rig.innerHTML="";stage.classList.remove("has-img");ph.textContent="Describe a style for the headline…";ph.classList.add("empty")});
}

/* ---------- 4 · internal campaigns ---------- */
function runInt(){
  var stk=R.getElementById("stk");
  var b1=wbox(words[0]),b2=wbox(words[1]),b3=wbox(words[2]);
  var W=stage.clientWidth,k=W<600?.6:1,B=b3.y+b3.h,RX=b3.x+b3.w;
  function cx(x,w){return Math.max(0,Math.min(W-w,x))}
  var extra=[
    {t:"Hi,<br>team!",bg:"#ffe14d",c:"#141414",x:0,y:-78*k,w:70,h:70,r:"-10deg",round:"50%"},
    {t:"5/5",bg:"#7c5cff",c:"#fff",x:W*.46,y:-70*k,w:62,h:62,r:"-14deg",round:"50%"},
    {t:"Team<br>2024",bg:"#16a34a",c:"#fff",x:W-90*k,y:-86*k,w:86,h:86,r:"12deg",round:"50%"},
    {t:"Values",bg:"#FF4417",c:"#fff",x:RX+24*k,y:b3.y+b3.h*.12,w:118,h:44,r:"-8deg",round:"999px"},
    {t:"★ Live it",bg:"#fff",c:"#141414",x:W*.05,y:B+18*k,w:112,h:40,r:"6deg",round:"6px"}
  ];
  var stamps=[
    {t:"Kick-off<br>Q3",c:"#1d4ed8",x:W*.24,y:-84*k,s:84,r:"14deg"},
    {t:"We did<br>it!",c:"#7c3aed",x:W*.68,y:-80*k,s:78,r:"18deg"},
    {t:"Approved<br>★ HR ★",c:"#d6261c",x:RX+40*k,y:b3.y+b3.h*.55,s:92,r:"-16deg"},
    {t:"Best<br>place to<br>work",c:"#16a34a",x:W-100*k,y:B+6*k,s:96,r:"-8deg"},
    {t:"Townhall · Fri",c:"#d6261c",x:W*.36,y:B+30*k,rect:1,r:"-4deg"},
    {t:"Internal only",c:"#141414",x:W*.62,y:B+22*k,rect:1,r:"6deg"}
  ];
  extra.forEach(function(e){e.w*=k;e.h*=k;e.x=cx(e.x,e.w)});stamps.forEach(function(e){if(e.s){e.s*=k;e.x=cx(e.x,e.s)}else e.x=cx(e.x,140*k)});
  stk.innerHTML=extra.map(function(e){return '<span class="s" style="left:'+e.x+'px;top:'+e.y+'px;width:'+e.w+'px;height:'+e.h+'px;background:'+e.bg+';color:'+e.c+';border-radius:'+e.round+';--r:'+e.r+';--r0:calc('+e.r+' * -2);text-align:center">'+e.t+'</span>'}).join("")+
    stamps.map(function(e){return '<span class="stamp'+(e.rect?' rect':'')+'" style="left:'+e.x+'px;top:'+e.y+'px;'+(e.s?'width:'+e.s+'px;height:'+e.s+'px;':'')+'--sc:'+e.c+';--r:'+e.r+'">'+e.t+'</span>'}).join("")+
    '<span class="tape" style="left:'+(b1.x-20)+'px;top:'+(b1.y-6)+'px;transform:rotate(-24deg)"></span><span class="tape" style="left:'+(b3.x+b3.w-50)+'px;top:'+(b3.y+b3.h-12)+'px;transform:rotate(-18deg)"></span>';
  var all=[words[0],words[1],words[2]].concat([].slice.call(stk.querySelectorAll(".s"))),tapes=stk.querySelectorAll(".tape"),st=[].slice.call(stk.querySelectorAll(".stamp"));
  function round(){
    var rs=[-2.5,3,-1.2];
    words.forEach(function(w,j){w.style.setProperty("--r",(rs[j]+(Math.random()*1.6-.8)).toFixed(2)+"deg");w.style.setProperty("--r0",(rs[j]*-4)+"deg");w.classList.remove("slap");w.style.opacity=reduce?1:0});
    stk.querySelectorAll(".s").forEach(function(s){s.classList.remove("slap");s.style.opacity=reduce?1:0});tapes.forEach(function(t){t.classList.remove("slap")});
    st.forEach(function(s){s.classList.remove("thud");s.style.opacity=reduce?.9:0});
    if(reduce){all.forEach(function(e){e.style.opacity=1});return}
    all.forEach(function(e,j){after(function(){void e.offsetWidth;e.style.opacity="";e.classList.add("slap")},120+j*220)});
    var t0=120+all.length*220;
    after(function(){tapes.forEach(function(t){t.classList.add("slap")})},t0);
    st.forEach(function(s,j){after(function(){void s.offsetWidth;s.style.opacity="";s.classList.add("thud")},t0+200+j*330)});
  }
  round();every(round,7000);
  subs.push(function(){stk.innerHTML="";words.forEach(function(w){w.style.opacity=""})});
}

/* ---------- 5 · UX/UI ---------- */
function runUI(){
  var sel=R.getElementById("sel"),selb=R.getElementById("selb"),cmt=R.getElementById("cmt"),cs=["c1","c2","c3"].map(function(id){return R.getElementById(id)});
  var k=0;function box(el){var b=wbox(el);return {x:b.x,y:b.y+b.h*.06,w:b.w,h:b.h*.88}}
  function step(){var S=stage.getBoundingClientRect(),b=box(words[k%3]);
    sel.style.left=b.x+"px";sel.style.top=b.y+"px";sel.style.width=b.w+"px";sel.style.height=b.h+"px";selb.textContent=Math.round(b.w)+" × "+Math.round(b.h);
    cs[0].style.left=(b.x+b.w*.92)+"px";cs[0].style.top=(b.y+b.h*.95)+"px";
    cs[1].style.left=(S.width*(.55+.3*Math.random()))+"px";cs[1].style.top=(S.height*(.15+.6*Math.random()))+"px";
    cs[2].style.left=(S.width*(.1+.35*Math.random()))+"px";cs[2].style.top=(S.height*(.2+.7*Math.random()))+"px";k++;}
  var b2=box(words[1]);cmt.style.left=Math.min(b2.x+b2.w+16,stage.clientWidth-30)+"px";cmt.style.top=(b2.y+8)+"px";
  step();if(!reduce)every(step,1900);
}

function run3D(){
  var rig=R.getElementById("rig3"),N=12,html="";
  for(var z=N;z>=0;z--){var t=z/N,c="rgb("+Math.round(200-110*t)+","+Math.round(194-108*t)+","+Math.round(184-104*t)+")";
    html+='<div class="lyr'+(z===0?" front":"")+'" style="transform:translateZ('+(-z*2.8)+'px);--c:'+c+'">'+rowsEl.innerHTML+'</div>';}
  rig.innerHTML='<div class="shadow"></div>'+html;
  rig.querySelectorAll(".row").forEach(function(r,j){r.style.fontSize=rows[j%2].style.fontSize});
  var tx=0,ty=0,ax=0,ay=0,t0=performance.now(),raf;
  function mv(e){var S=stage.getBoundingClientRect();tx=((e.clientX-S.left)/S.width-.5);ty=((e.clientY-S.top)/S.height-.5)}
  addEventListener("pointermove",mv);
  (function loop(now){raf=requestAnimationFrame(loop);var s=(now-t0)/1000;
    var sx=reduce?0:Math.sin(s*.7)*.35,sy=reduce?0:Math.cos(s*.5)*.2;
    ax+=((tx||sx)-ax)*.06;ay+=((ty||sy)-ay)*.06;
    rig.style.transform="rotateY("+(ax*26)+"deg) rotateX("+(-ay*18+6)+"deg) translateZ(0)";})(t0);
  subs.push(function(){cancelAnimationFrame(raf);removeEventListener("pointermove",mv);rig.innerHTML=""});
}
/* ---------- 7 · AI video: the voice times the words ---------- */
function runVid(){
  /* an editing timeline: the playhead (auto or dragged) drives each part of the headline */
  var v=R.getElementById("vid");
  var clips=[
    {tr:0,a:.04,b:.30,n:"Creative · slide in",c:"#4f7cff",w:0},
    {tr:1,a:.26,b:.52,n:"ideas, · scale + rotate",c:"#a855f7",w:1},
    {tr:0,a:.50,b:.80,n:"big results. · mask reveal",c:"#16a34a",w:2},
    {tr:2,a:.78,b:.98,n:"Flash · grade",c:"#FF4417",w:3}
  ];
  var tracks=["V1","V2","FX","A1"];
  var bars="";for(var i=0;i<120;i++){bars+='<i style="height:'+Math.round(20+Math.abs(Math.sin(i*.31)*Math.cos(i*.11))*75)+'%"></i>'}
  v.innerHTML='<div class="tl" id="tl"><div class="tl-top"><span>Sequence · Hero_v07</span><span class="tc" id="tcv">00:00:00:00</span><span>24 fps</span></div>'+
    '<div class="tl-ruler" id="rul">'+Array.apply(null,{length:11}).map(function(_,j){return '<span style="left:'+(j*10)+'%">'+String(j).padStart(2,"0")+'s</span>'}).join("")+'</div>'+
    tracks.map(function(t,j){return '<div class="tl-row"><span class="lab">'+t+'</span><div class="lane">'+(j<3?clips.filter(function(c){return c.tr===j}).map(function(c){return '<span class="clip" data-w="'+c.w+'" style="left:'+(c.a*100)+'%;width:'+((c.b-c.a)*100)+'%;--c:'+c.c+'"><em>'+c.n+'</em><i class="kf" style="left:0"></i><i class="kf" style="left:calc(100% - 9px)"></i></span>'}).join(""):'<div class="aud">'+bars+'</div>')+'</div></div>'}).join("")+
    '<div class="tl-head" id="tlh"><b></b></div></div>';
  var tl=R.getElementById("tl"),head=R.getElementById("tlh"),tcv=R.getElementById("tcv"),lanes=tl.querySelector(".lane"),cl=[].slice.call(tl.querySelectorAll(".clip")),aud=[].slice.call(tl.querySelectorAll(".aud i"));
  var w1=words[0],w2=words[1],w3=words[2];
  function ease(x){x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}
  function seg(p,a,b){return ease((p-a)/(b-a))}
  function render(p){
    var L=lanes.getBoundingClientRect(),T=tl.getBoundingClientRect();
    head.style.left=(L.left-T.left+p*L.width)+"px";
    var s=p*10,fr=Math.floor((s%1)*24);tcv.textContent="00:00:"+String(Math.floor(s)).padStart(2,"0")+":"+String(fr).padStart(2,"0");
    var k1=seg(p,.04,.30),k2=seg(p,.26,.52),k3=seg(p,.50,.80),k4=p>.78?Math.sin(Math.min(1,(p-.78)/.2)*Math.PI):0;
    w1.style.transform="translateX("+((1-k1)*-40)+"%)";w1.style.opacity=k1;w1.style.filter="blur("+((1-k1)*12)+"px)";
    w2.style.transform="scale("+(.3+.7*k2)+") rotate("+((1-k2)*-18)+"deg)";w2.style.opacity=k2;
    w3.style.clipPath="inset(0 "+((1-k3)*100)+"% 0 0)";w3.style.opacity=k3>0?1:0;
    stage.style.setProperty("--flash",k4.toFixed(3));
    cl.forEach(function(c,j){var C=clips[j];c.classList.toggle("on",p>=C.a&&p<=C.b);c.classList.toggle("done",p>C.b)});
    var n=Math.floor(p*aud.length);aud.forEach(function(b,j){b.classList.toggle("p",j<=n)});
  }
  var p=0,last=performance.now(),raf,drag=false;
  function loop(now){raf=requestAnimationFrame(loop);var dt=(now-last)/1000;last=now;if(!drag&&!reduce){p+=dt/6.2;if(p>1.12)p=0}render(Math.min(p,1))}
  function setFromX(x){var L=lanes.getBoundingClientRect();p=Math.max(0,Math.min(1,(x-L.left)/L.width))}
  tl.addEventListener("pointerdown",function(e){drag=true;hold=true;clearTimeout(timer);thumb.classList.remove("run");tl.setPointerCapture(e.pointerId);setFromX(e.clientX)});
  tl.addEventListener("pointermove",function(e){if(drag)setFromX(e.clientX)});
  tl.addEventListener("pointerup",function(){drag=false});
  if(reduce){render(1);return}
  raf=requestAnimationFrame(loop);
  subs.push(function(){cancelAnimationFrame(raf);v.innerHTML="";[w1,w2,w3].forEach(function(w){w.style.cssText=""});stage.style.removeProperty("--flash")});
}

/* ---------- selector: click, drag, keys ---------- */
/* ---------- selector: click (no capture), drag only after real movement, keys ---------- */
btns.forEach(function(b,i){b.addEventListener("click",function(){if(moved)return;hold=true;clearTimeout(timer);thumb.classList.remove("run");show(i)})});
var down=false,moved=false,sx=0;
function idxAt(x){var r=track.getBoundingClientRect();return Math.max(0,Math.min(6,Math.floor((x-r.left)/r.width*7)))}
track.addEventListener("pointerdown",function(e){down=true;moved=false;sx=e.clientX});
track.addEventListener("pointermove",function(e){if(!down)return;
  if(!moved&&Math.abs(e.clientX-sx)>8){moved=true;hold=true;clearTimeout(timer);thumb.classList.remove("run");thumb.style.transition="none";try{track.setPointerCapture(e.pointerId)}catch(_){}}
  if(!moved)return;var r=track.getBoundingClientRect(),f=Math.max(0,Math.min(6,(e.clientX-r.left)/r.width*7-.5));thumb.style.transform="translateX("+(f*100)+"%)";
  var i=idxAt(e.clientX);if(i!==cur)show(i,true)});
function endDrag(){if(!down)return;down=false;thumb.style.transition="";moveThumb(cur);setTimeout(function(){moved=false},0)}
track.addEventListener("pointerup",endDrag);track.addEventListener("pointercancel",endDrag);

track.addEventListener("keydown",function(e){if(e.key==="ArrowRight"){hold=true;show(Math.min(6,cur+1))}if(e.key==="ArrowLeft"){hold=true;show(Math.max(0,cur-1))}});
var rz;addEventListener("resize",function(){clearTimeout(rz);rz=setTimeout(function(){var i=cur;cur=-1;show(i,true)},150)});
document.fonts&&document.fonts.ready.then(function(){var i=cur<0?0:cur;cur=-1;show(i,true)});
show(0,true);
if("IntersectionObserver" in window){var paused=false;new IntersectionObserver(function(es){var v=es[0].isIntersecting;
  if(!v&&!paused){paused=true;clearSubs();clearTimeout(timer);thumb.classList.remove("run")}
  else if(v&&paused){paused=false;var i=cur;cur=-1;show(i,true)}},{threshold:0}).observe(stage)}
})();
}
if(css.sheet)boot();else css.addEventListener("load",boot);
})();
