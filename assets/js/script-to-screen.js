/* Script to Screen. To add a video to the series: add one entry to VIDEOS and its files in assets/video/script-to-screen/. */
(function(){
"use strict";
var $=function(id){return document.getElementById(id)};
var IMG="../assets/img/script-to-screen/", VID="../assets/video/script-to-screen/";
var reduce=matchMedia("(prefers-reduced-motion: reduce)").matches;

var VIDEOS=[
 {id:"v1",title:"This is Bracco",len:"29.9 s",poster:"p1"},
 {id:"v2",title:"What is a Point Spread",len:"28.5 s",poster:"p2"},
 {id:"v3",title:"What is an Over/Under",len:"23.4 s",poster:"p3"},
 {id:"v4",title:"What is a Parlay",len:"20.3 s",poster:"p4"},
 {id:"v5",title:"What is a Moneyline",len:"22.1 s",poster:"p5"},
 {id:"v6",title:"MNF Bills vs Vikings",len:"28.0 s",poster:"p6",formats:true}
];
var byId={};VIDEOS.forEach(function(v){byId[v.id]=v});

/* Lazy video: src is only set when the element nears the viewport */
var io=("IntersectionObserver" in window)?new IntersectionObserver(function(es){es.forEach(function(e){
  var v=e.target;
  if(e.isIntersecting){if(!v.src){v.src=v.dataset.src;v.load();}if(v.dataset.auto&&!reduce){var p=v.play();p&&p.catch(function(){});}}
  else if(v.dataset.auto&&!v.paused)v.pause();
})},{rootMargin:"300px 0px"}):null;
function vid(file,poster,o){o=o||{};var v=document.createElement("video");
  v.muted=true;v.playsInline=true;v.setAttribute("playsinline","");v.preload="none";v.poster=IMG+poster+".jpg";
  v.dataset.src=VID+file+".mp4";if(o.loop)v.loop=true;if(o.auto)v.dataset.auto="1";
  v.setAttribute("aria-label",o.label||"");v.setAttribute("disablepictureinpicture","");
  if(io)io.observe(v);else v.src=v.dataset.src;return v;}
function ensure(v){if(!v.src){v.src=v.dataset.src;v.load();}}
function seek(v,t,play){ensure(v);var go=function(){try{v.currentTime=t}catch(e){}if(play&&!reduce){var p=v.play();p&&p.catch(function(){})}else v.pause();};
  if(v.readyState>=1)go();else v.addEventListener("loadedmetadata",go,{once:true});}

/* Hero: Vid1, Vid6, Vid3, muted loops */
["v1","v6","v3"].forEach(function(id){var V=byId[id],d=document.createElement("div");d.className="ph9";
  d.appendChild(vid(id+"-9x16",V.poster,{loop:true,auto:true,label:V.title}));$("fan").appendChild(d);});

/* Intro diagram: real voice envelope and word times, 5.6 s to 23.7 s of Video 6 */
(function(){
 var W=[6,82,55,75,88,46,79,62,65,55,74,46,100,46,63,63,76,59,6,6,65,61,70,72,84,59,58,58,59,44,34,17,65,85,42,6,6,71,63,82,44,70,39,60,86,25,48,100,69,89,60,30,63,6,24,87,43,84,76,54,65,68,61,44,46,61,35,64,80,63,71,45],T0=5.6,T1=23.7;
 var pct=function(t){return (t-T0)/(T1-T0)*100};
 var B=[["6-1",6.14,8.3,"stat card"],["3-4",7.48,10.1,"stat card"],["75+",11.30,14.6,"stat card"],["receiving total",16.16,19,"stat card"],["anytime touchdown",20.48,21.8,"stat card"]];
 var lab=["6-1","3-4","75+","rec. total","anytime TD"];
 $("dWave").innerHTML=W.map(function(h){return '<i style="height:'+h+'%"></i>'}).join("");
 $("dWords").insertAdjacentHTML("beforeend",B.map(function(b,i){return '<span class="tick" data-i="'+i+'" style="left:'+pct(b[1])+'%">'+lab[i]+'</span>'}).join(""));
 $("dGfx").insertAdjacentHTML("beforeend",B.map(function(b,i){return '<span class="gfx" data-i="'+i+'" style="left:'+pct(b[1])+'%;width:'+(pct(b[2])-pct(b[1]))+'%"></span>'}).join(""));
 $("dScr").innerHTML='Bills are <span class="sk" data-i="0">6-1</span>, but <span class="sk" data-i="1">3-4</span> in the first quarter. James Cook has topped <span class="sk" data-i="2">75+</span> rushing yards. Keon Coleman cleared his <span class="sk" data-i="3">receiving total</span>. How about a Josh Allen <span class="sk" data-i="4">anytime touchdown</span>?';
 var v=vid("v6-9x16","s_12.2",{label:"Video 6 frame triggered by the highlighted word"});$("dBox").appendChild(v);
 var started=false;
 function show(i){var b=B[i];document.querySelectorAll(".sk,.tick,.gfx").forEach(function(e){e.classList.toggle("on",+e.dataset.i===i)});
  ["dH1","dH2","dH3"].forEach(function(h){$(h).style.left=pct(b[1])+"%"});
  if(started)seek(v,b[1]+.9,true);
  $("dCap").innerHTML='<b>&ldquo;'+b[0]+'&rdquo;</b> heard at '+b[1].toFixed(2)+' s &rarr; '+b[3]+' fires';}
 var i=2;show(i);
 var box=$("dBox"),run=null;
 function start(){if(run||reduce)return;started=true;show(i);run=setInterval(function(){i=(i+1)%B.length;show(i)},2400);}
 function stop(){clearInterval(run);run=null;v.pause();}
 if("IntersectionObserver" in window)new IntersectionObserver(function(es){es[0].isIntersecting?start():stop()},{threshold:.3}).observe(box);
 if(reduce){started=true;}
})();

/* Script to screen: real word times from Video 6 */
var S=[
 ["Searching for value on ",["Monday Night Football","2.6",1.18]," in ",["Week 9","4.8",2.02],"."],
 ["Bills are ",["6-1","7.0",6.14]," on the season, but are ",["3-4","9.7",7.48]," straight up in the first quarter."],
 ["James Cook has topped ",["75+","12.2",11.30]," rushing yards in ",["6 straight games","14.2",13.14],"."],
 ["Keon Coleman has cleared his ",["receiving total","16.9",16.16]," in ",["4 of his last 6","18.8",17.26]," games."],
 ["How about a Josh Allen ",["anytime touchdown","21.1",20.48],"? He leads the NFL with ",["9","23.5",23.16],"."],
 ["Build a ",["Same Game Parlay","25.4",24.18]," on Bracco. ",["Download","27.4",25.98]," the app today."]];
$("scr").innerHTML=S.map(function(p){return "<p>"+p.map(function(x){return typeof x==="string"?x:'<button type="button" class="sw" aria-pressed="false" data-f="'+x[1]+'" data-t="'+x[2]+'">'+x[0]+'</button>'}).join("")+"</p>"}).join("");
var sv=vid("v6-9x16","s_16.9",{label:"Video 6"});$("sBox").appendChild(sv);
function pick(b,play){document.querySelectorAll(".sw").forEach(function(e){e.setAttribute("aria-pressed",e===b)});
 sv.poster=IMG+"s_"+b.dataset.f+".jpg";sv.setAttribute("aria-label","Video 6 at "+b.textContent);
 $("sW").textContent=b.textContent;$("sT").textContent="fires at "+(+b.dataset.t).toFixed(2)+" s";
 if(play)seek(sv,+b.dataset.t,true);}
document.querySelectorAll(".sw").forEach(function(b){b.onclick=function(){pick(b,true)}});
pick(document.querySelectorAll(".sw")[3],false);

/* Pipeline (stays as stills) */
var P=[
 {n:"Brief",t:"Interview",who:1,tool:"Claude Code + brand rules",i:"Script, notes, take",o:"proyecto.json",d:"Reads the notes, then asks only what they leave open: graphics, music, and which passages show the presenter.",img:"st_raw",c:'"formats": ["1080x1920","1080x1350",\n            "1080x1080","1920x1080"],\n"duracion_max_s": 30'},
 {n:"Transcribe",t:"Whisper",tool:"OpenAI Whisper",i:"Audio track",o:"words.json",d:"Every word gets a start and end time. The script only corrects spelling and flags false starts; captions show what was actually said.",img:"st_raw",c:'{"w":"Bills","start":3.32}\n{"w":"and","start":3.64}\n{"w":"Vikings.","start":3.78}'},
 {n:"Cut",t:"FFmpeg",who:1,tool:"FFmpeg + audio energy analysis",i:"Words + loudness",o:"keep.json, cut.mp4",d:"Removes pauses and failed takes, and keeps half a second of tail. I approve the transcript and the cuts.",img:"st_raw",c:'{"segments":[[1.50,7.16],\n  [9.62,27.80],\n  [45.34,49.45]]}'},
 {n:"Key",t:"FFmpeg",who:1,tool:"FFmpeg chroma key + despill",i:"cut.mp4",o:"plate.mp4, matte-vo.mp4",d:"The key colour is measured per take. The matte also hides the presenter through voice-over passages. A one-frame test is approved first.",img:"st_matte",c:'chromakey=0x00B358:0.12:0.08,\ndespill=type=green:mix=0.6'},
 {n:"Keywords",t:"captions.py",who:1,tool:"Skill script",i:"Words + phrase list",o:"captions.json",d:"Phrases are split into short chunks with marked keywords, approved before any animation exists.",img:"st_final",c:'Bills are | *6-1* | on the season,\nbut are | *3-4* | straight up'},
 {n:"Plan",t:"Graphics table",who:1,tool:"Claude Code",i:"Script + brand references",o:"plan-graficos.md",d:"A table of what appears, on which word and why, checked against the brand rules. Nothing is built until it is approved.",img:"st_final",c:'| "3-4" | 7.48 s | stat card |\n| "75+" | 11.30 s | stat card |'},
 {n:"Background",t:"HyperFrames",tool:"HyperFrames + FFmpeg",i:"Layout table, plate, matte",o:"bg.mp4, base.mp4",d:"Renders the animated backdrop and behind-the-head titles, then composites the presenter on top.",img:"st_base",c:'[bg][glow]overlay[b1];\n[b1][fg]overlay'},
 {n:"Motion",t:"HyperFrames + GSAP",who:1,tool:"HyperFrames + GSAP",i:"base.mp4, captions, word times",o:"reel-video.mp4",d:"Cards, scenes, captions and legal copy, written as HTML and rendered frame by frame. Snapshots at key moments are checked before the full render.",img:"st_final",c:'gtl.fromTo("#s1b", CARD_IN, 7.43);'},
 {n:"Sound",t:"SynthFlow + mix",who:1,tool:"SynthFlow + FFmpeg",i:"Voice, music, cue list",o:"FINAL mp4",d:"New synthwave for each video, effects cued to graphics, music ducked under the voice, master verified at −14 LUFS on the final file.",img:"st_final",c:'{"file":"sfx/impact.wav",\n "t":7.43,"db":-21}'}];
$("pipe").innerHTML=P.map(function(s,i){return '<button type="button" class="st" role="tab" data-i="'+i+'" '+(s.who?'data-who="you"':'')+' aria-selected="false"><b>'+(i+1)+'. '+s.n+'</b><i>'+s.t+'</i></button>'}).join("");
function st(i){document.querySelectorAll(".st").forEach(function(e,k){e.setAttribute("aria-selected",k===i)});var s=P[i];
 $("det").innerHTML='<img src="'+IMG+s.img+'.jpg" alt="'+s.n+' stage frame" loading="lazy"><div><h3>'+s.n+'</h3><p>'+s.d+'</p><dl class="io"><dt>Tool</dt><dd>'+s.tool+'</dd><dt>Input</dt><dd>'+s.i+'</dd><dt>Output</dt><dd class="so">'+s.o+'</dd></dl><pre>'+s.c+'</pre></div>';}
document.querySelectorAll(".st").forEach(function(b){b.onclick=function(){st(+b.dataset.i)}});st(3);

/* Ledger: add a row only when a video brought a new rule */
var L=[
 ["V1","Brand guide becomes numbers","The style guide was translated into hex values, pixel sizes and durations, and approved before use.","Orange only on keywords, figures and borders",null],
 ["V1","Late revision: a restricted word","One word could not be used. Only that passage was replaced with new audio, and animation, captions and effects were re-timed to it, without redoing the cut or the key.","Restricted term banned in audio and on screen",["r_word_after","After the fix"]],
 ["V1","Hide the presenter for the whole voice-over","I spotted a reading take showing through the crossfades. The fix went into the matte itself.","Matte = 0 between the voice-over cuts",null],
 ["V2","Cards need room under the chin","In the tighter formats, cards sat too close to the face.","4:5 card top: 615 → 700 px",["r_low_before","V1, before","r_low_after","V2, after"]],
 ["V2","Match the client's real social language","A balance-scale idea was replaced with the segmented bars from the client's own posts.","Client references outrank generic metaphors",["r_ref_before","Client reference","r_ref_after","V2 scene"]],
 ["V3","Dark clothes vanish on a dark brand","A black hoodie lost its silhouette, so a soft orange rim was added from the matte itself.","Dark wardrobe = 55% orange glow",["r_glow_before","Without","r_glow_after","With"]],
 ["V4","Never end abruptly","Half a second of tail became permanent, and a loss state used the palette's existing functional red.","Tail 0.5 s · loss colour #d24c35",["r_red_after","Loss state"]],
 ["V5","First single pass","With the rules in place, one video ran start to finish without stopping, and I reviewed the result.","Baseline for the time estimate",null],
 ["V6","Photos, and a useful miss","Still photos gained motion and data cards. Running unattended, the system assumed the whole video was voice-over; the opening and closing needed the presenter. Review by stages came back, plus one new question up front.","Always confirm who is on screen, and when",["r_vo_before","First pass","r_vo_after","Corrected"]]];
$("led").innerHTML=L.map(function(r){var m=r[4],f="";if(m){f='<div class="ba'+(m.length===2?" one":"")+'">';for(var i=0;i<m.length;i+=2)f+='<figure><img src="'+IMG+m[i]+'.jpg" alt="'+m[i+1]+'" loading="lazy"><figcaption>'+m[i+1]+'</figcaption></figure>';f+="</div>";}
 return '<div class="rule"><div class="vid">'+r[0]+'</div><div><h3>'+r[1]+'</h3><p class="snote">'+r[2]+'</p><span class="code">'+r[3]+'</span></div><div>'+f+'</div></div>'}).join("");

/* Formats: Video 6 in four synced players; chips jump to a moment */
var MO=[["Opening",1.0],["Photo + data",12.2],["Parlay ticket",24.6],["Call to action",26.6]];
var R=[["9x16","1080x1920","9:16 master","9/16"],["4x5","1080x1350","4:5","4/5"],["1x1","1080x1080","1:1","1/1"],["16x9","1920x1080","16:9","16/9"]];
$("fc").innerHTML=MO.map(function(m,i){return '<button type="button" class="chip" data-i="'+i+'" aria-pressed="false">'+m[0]+'</button>'}).join("");
var FV=R.map(function(r){var fig=document.createElement("figure"),b=document.createElement("div");b.className="fbox";b.style.aspectRatio=r[3];
  var v=vid("v6-"+r[0],"f1_"+r[1],{loop:true,label:"Video 6 in "+r[2]});b.appendChild(v);fig.appendChild(b);
  fig.insertAdjacentHTML("beforeend","<figcaption>"+r[2]+"</figcaption>");$("fm").appendChild(fig);return v;});
var lead=FV[0],fmOn=false;
lead.addEventListener("timeupdate",function(){for(var k=1;k<FV.length;k++){var o=FV[k];if(o.readyState>=1&&Math.abs(o.currentTime-lead.currentTime)>.2){try{o.currentTime=lead.currentTime}catch(e){}}}});
function fm(i,play){document.querySelectorAll(".chip").forEach(function(e,k){e.setAttribute("aria-pressed",k===i)});
 FV.forEach(function(v,k){v.poster=IMG+"f"+i+"_"+R[k][1]+".jpg";if(play)seek(v,MO[i][1],true);});}
document.querySelectorAll(".chip").forEach(function(b){b.onclick=function(){fm(+b.dataset.i,true)}});
fm(1,false);
if("IntersectionObserver" in window)new IntersectionObserver(function(es){
  if(es[0].isIntersecting){if(!fmOn&&!reduce){fmOn=true;FV.forEach(function(v){seek(v,MO[1][1],true)});}else if(!reduce)FV.forEach(function(v){ensure(v);var p=v.play();p&&p.catch(function(){})});}
  else FV.forEach(function(v){v.pause()});
},{threshold:.25}).observe($("fm"));

/* Series: click to play with sound */
var GV=[];
$("gal").innerHTML="";
VIDEOS.forEach(function(V){var fig=document.createElement("figure"),b=document.createElement("div");b.className="ph9";
  b.setAttribute("role","button");b.tabIndex=0;b.setAttribute("aria-label","Play "+V.title+" with sound");
  var v=vid(V.id+"-9x16",V.poster,{label:V.title});b.appendChild(v);b.insertAdjacentHTML("beforeend",'<span class="sts-pl" aria-hidden="true"></span>');GV.push(v);
  function toggle(){ensure(v);if(v.paused){GV.concat(FV,[sv]).forEach(function(o){if(o!==v)o.pause()});GV.forEach(function(o){o.parentNode.classList.remove("on")});v.muted=false;v.controls=true;b.classList.add("on");var p=v.play();p&&p.catch(function(){});}else{v.pause();}}
  b.addEventListener("click",function(e){if(!v.controls)toggle()});
  b.addEventListener("keydown",function(e){if(e.key==="Enter"||e.key===" "){e.preventDefault();toggle()}});
  v.addEventListener("pause",function(){if(v.ended){b.classList.remove("on");v.controls=false}});
  fig.appendChild(b);
  fig.insertAdjacentHTML("beforeend","<figcaption><b>"+V.title+"</b><small>"+V.len+" · 4 formats</small><span class=\"tag sslot\">Live link: pending release</span></figcaption>");
  $("gal").appendChild(fig);});
})();
