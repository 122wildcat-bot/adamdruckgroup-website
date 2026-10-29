(function(){
'use strict';
const fmt = n => (n<0?'−':'') + '$' + Math.abs(Math.round(n)).toLocaleString('en-US');
const sgn = n => (n>0?'+':n<0?'−':'') + '$' + Math.abs(Math.round(n)).toLocaleString('en-US');
const RATE_AG = 90, RATE_BG = 35, SUBJ_AG = 2210, SUBJ_BG = 724;

const subject = {id:'you', addr:'195 Joshua Dr', lat:39.763662, lng:-76.971327};
const active = {id:'act', addr:'357 Joshua Ct', lat:39.766524, lng:-76.968444, price:450000, note:'Active · reduced from $475,000'};

const comps = [
  {id:'48', addr:'48 Joshua Dr', lat:39.761505, lng:-76.968531, price:425000, date:'Aug. 4, 2026', ag:2115, bg:0, bgNote:'Unfinished walkout', beds:'4', baths:'2.5', lot:'0.34 ac', built:'2014 (rebuilt 2024)', weight:.45,
   other:[{l:'Your extra full bath', v:10000},{l:'Recent full rebuild', v:-10000}],
   why:'The closest match in size and layout, and the most recent sale. It was rebuilt in 2024, so it gets credit for newer finishes and systems. It carries the most weight.',
   src:'https://www.redfin.com/PA/Hanover/48-Joshua-Dr-17331/home/140690812', srcName:'Redfin listing history'},
  {id:'204', addr:'204 Joshua Dr', lat:39.763594, lng:-76.97186, price:434000, date:'Dec. 19, 2025', ag:2342, bg:690, bgNote:'Finished', beds:'5', baths:'3.5', lot:'0.35 ac', built:'2010', weight:.30,
   other:[{l:'Your condition advantage', v:10000}],
   why:'Practically next door with a similar finished lower level and the same 3.5 baths. It has a Cape Cod layout, and your home gets credit for its excellent condition.',
   src:'https://www.realtor.com/realestateandhomes-detail/204-Joshua-Dr_Hanover_PA_17331_M35474-58191', srcName:'Realtor.com listing details'},
  {id:'244', addr:'244 Joshua Dr', lat:39.764591, lng:-76.972255, price:500000, date:'Feb. 27, 2026', ag:3188, bg:500, bgNote:'Partially finished', beds:'5', baths:'2.5', lot:'0.39 ac', built:'2008', weight:.10,
   other:[{l:'Your extra full bath', v:10000}],
   why:'A few doors away, but nearly 1,000 sq ft larger above grade. The large size adjustment makes it a supporting comp rather than a primary one.',
   src:'https://www.zillow.com/homedetails/244-Joshua-Dr-Hanover-PA-17331/88872227_zpid/', srcName:'Zillow listing details'},
  {id:'132', addr:'132 Joshua Dr', lat:39.762405, lng:-76.970638, price:490000, date:'June 22, 2026', ag:2838, bg:741, bgNote:'Finished', beds:'7 (as marketed)', baths:'3.5', lot:'0.34 ac', built:'2007', weight:.05,
   other:[{l:'Inground pool & outdoor living', v:-15000},{l:'Your age/condition edge', v:5000}],
   why:'A much larger home with an inground pool. It confirms the top of the street but needs big adjustments, so its weight is small.',
   src:'https://www.redfin.com/PA/Hanover/132-Joshua-Dr-17331/home/140651748', srcName:'Redfin listing history'},
  {id:'12', addr:'12 Joshua Dr', lat:39.761084, lng:-76.967268, price:375000, date:'Jan. 23, 2026', ag:1768, bg:0, bgNote:'Not reported as finished', beds:'5', baths:'2.5', lot:'0.63 ac', built:'2014', weight:.10,
   other:[{l:'Your extra full bath', v:10000},{l:'Larger lot', v:-8000},{l:'Recent renovation', v:-5000}],
   why:'Smaller and recently renovated, on a larger lot. It is a useful lower bound, but a lower-level finish was not reported, so it carries less weight.',
   src:'https://www.redfin.com/PA/Hanover/12-Joshua-Dr-17331/home/140651725', srcName:'Redfin listing history'}
];

comps.forEach(c=>{
  c.adjAg = (SUBJ_AG - c.ag) * RATE_AG;
  c.adjBg = (SUBJ_BG - c.bg) * RATE_BG;
  c.adjOther = c.other.reduce((a,o)=>a+o.v,0);
  c.pre = c.price + c.adjAg + c.adjBg + c.adjOther;
});

function miles(a,b){
  const R=3958.8, toR=x=>x*Math.PI/180;
  const dLat=toR(b.lat-a.lat), dLng=toR(b.lng-a.lng);
  const h=Math.sin(dLat/2)**2+Math.cos(toR(a.lat))*Math.cos(toR(b.lat))*Math.sin(dLng/2)**2;
  return 2*R*Math.asin(Math.sqrt(h));
}
comps.forEach(c=>c.dist=miles(subject,c));
active.dist=miles(subject,active);

/* ---------- Pricing ladder ---------- */
const tiers = {quick:{p:429900,l:'Quick Sale'}, rec:{p:439900,l:'Recommended'}, test:{p:449900,l:'Upper-End Test'}};
const ladder = document.getElementById('ladder');
const MIN=360000, MAX=510000;
const pct = v => ((v-MIN)/(MAX-MIN)*100);
function buildLadder(){
  const pts=[...comps].map(c=>({k:'sold',t:`${c.addr.replace(' Joshua Dr','')} Joshua · ${fmt(c.price)}`,v:c.price}))
    .concat([{k:'act',t:`357 Joshua · ${fmt(active.price)} active`,v:active.price}]).sort((a,b)=>a.v-b.v);
  const W = ladder.clientWidth || 1000;
  const rowsEnd=[]; const ROWH=26;
  pts.forEach(p=>{
    const w = (p.t.length*7.2+16)/W*100; const x=pct(p.v);
    let s=x-w/2, e=x+w/2; if(s<0){s=0;e=w;} if(e>100){e=100;s=100-w;}
    let r=0; while(rowsEnd[r]!==undefined && rowsEnd[r]>s-1) r++;
    rowsEnd[r]=e; p.row=r; p.s=s; p.w=w;
  });
  const nRows=rowsEnd.length, axisY=nRows*ROWH+18;
  ladder.style.height=(axisY+92)+'px';
  let h=`<div class="ladder__axis" style="top:${axisY}px"></div>`;
  h += `<div class="ladder__band" style="top:${axisY-4}px;left:${pct(425000)}%;width:${pct(445000)-pct(425000)}%"></div>`;
  for(let v=375000; v<=500000; v+=25000) h += `<span class="ladder__tick" style="top:${axisY+10}px;left:${pct(v)}%">$${v/1000}K</span>`;
  pts.forEach(p=>{
    const y=(nRows-1-p.row)*ROWH;
    h += `<span class="ladder__lbl ladder__lbl--${p.k}" style="top:${y}px;left:${p.s}%;width:${p.w}%">${p.t}</span>`;
    h += `<span class="ladder__lead" style="left:${pct(p.v)}%;top:${y+20}px;height:${axisY-y-20}px"></span>`;
    h += `<span class="ladder__dot ladder__dot--${p.k}" style="left:${pct(p.v)}%;top:${axisY-6}px"></span>`;
  });
  h += `<div class="ladder__you" id="you" style="left:${pct(439900)}%;top:${axisY-10}px"><b></b><span id="youlbl">Recommended · $439,900</span></div>`;
  ladder.innerHTML = h;
  if(!ladder.nextElementSibling || !ladder.nextElementSibling.classList.contains('ladder__legend')){
  const leg = document.createElement('div');
  leg.className='ladder__legend';
  leg.innerHTML = `<span><i class="lg" style="background:var(--sky)"></i>Recent sale on Joshua Dr</span><span><i class="lg" style="background:var(--neg);border-radius:2px"></i>Active competitor</span><span><i class="lg" style="background:rgba(65,143,222,.35);border-radius:999px;width:22px"></i>Estimated value range</span><span><i class="lg" style="background:var(--navy);width:3px;border-radius:0"></i>Selected list price</span>`;
  ladder.after(leg);}
  const cur=document.querySelector('.tier[aria-checked="true"]'); if(cur) setTimeout(()=>setTier(cur.dataset.tier));
}
buildLadder();
let _rz;window.addEventListener('resize',()=>{clearTimeout(_rz);_rz=setTimeout(buildLadder,150);});
function setTier(key){
  document.querySelectorAll('.tier').forEach(b=>b.setAttribute('aria-checked', String(b.dataset.tier===key)));
  const t=tiers[key];
  document.getElementById('you').style.left = pct(t.p)+'%';
  document.getElementById('youlbl').textContent = `${t.l} · ${fmt(t.p)}`;
}
document.querySelectorAll('.tier').forEach(b=>{
  b.addEventListener('click',()=>setTier(b.dataset.tier));
  b.addEventListener('keydown',e=>{
    const keys=['quick','rec','test']; const i=keys.indexOf(b.dataset.tier);
    if(e.key==='ArrowRight'||e.key==='ArrowDown'){e.preventDefault();const n=keys[(i+1)%3];setTier(n);document.querySelector(`[data-tier="${n}"]`).focus();}
    if(e.key==='ArrowLeft'||e.key==='ArrowUp'){e.preventDefault();const n=keys[(i+2)%3];setTier(n);document.querySelector(`[data-tier="${n}"]`).focus();}
  });
});

/* ---------- Comparable explorer ---------- */
let soft = 0.03;
const tabs = document.getElementById('comptabs');
const panel = document.getElementById('comppanel');
tabs.innerHTML = comps.map((c,i)=>`<button role="tab" id="tab-${c.id}" aria-selected="${i===0}" aria-controls="comppanel" data-id="${c.id}">${c.addr}</button>`).join('');
function renderComp(id){
  const c = comps.find(x=>x.id===id);
  tabs.querySelectorAll('button').forEach(b=>b.setAttribute('aria-selected', String(b.dataset.id===id)));
  const allowance = -c.pre*soft, adj = c.pre+allowance;
  const steps = [{l:'Sale price', v:c.price, base:true}, {l:'Above-grade area', v:c.adjAg, n:`${(SUBJ_AG-c.ag).toLocaleString()} sq ft × $${RATE_AG}`}, {l:'Finished lower level', v:c.adjBg, n:`${(SUBJ_BG-c.bg).toLocaleString()} sq ft × $${RATE_BG}`}];
  c.other.forEach(o=>steps.push({l:o.l, v:o.v}));
  steps.push({l:`Slower market (${(soft*100).toFixed(1)}%)`, v:allowance});
  const lo=Math.min(340000, ...[c.price,c.pre,adj]), hi=Math.max(520000, c.price, c.pre);
  const p = v => ((v-lo)/(hi-lo)*100);
  let run=0, rows='';
  steps.forEach(s=>{
    if(s.base){ run=s.v; rows += `<div class="wf__row wf__row--base"><span class="lab">${s.l}</span><div class="wf__bar"><i style="left:0;width:${p(run)}%"></i></div><span class="val">${fmt(run)}</span></div>`; return; }
    const a=run, b=run+s.v; run=b;
    const left=p(Math.min(a,b)), w=Math.max(Math.abs(p(b)-p(a)),.6);
    rows += `<div class="wf__row ${s.v>=0?'pos':'neg'}"><span class="lab">${s.l}${s.n?`<span class="wf__note" style="display:block">${s.n}</span>`:''}</span><div class="wf__bar"><i style="left:${left}%;width:${w}%"></i></div><span class="val">${s.v===0?'$0':sgn(s.v)}</span></div>`;
  });
  rows += `<div class="wf__row wf__row--total"><span class="lab">Indicated value for your home</span><div class="wf__bar"><i style="left:0;width:${p(adj)}%"></i></div><span class="val">${fmt(adj)}</span></div>`;
  panel.setAttribute('aria-labelledby','tab-'+c.id);
  panel.innerHTML = `
    <div>
      <h3>${c.addr}</h3>
      <p class="comp__sold">Sold <strong>${fmt(c.price)}</strong> · ${c.date} · ${c.dist.toFixed(2)} mi away</p>
      <div class="spec">
        <div class="h"></div><div class="h">This sale</div><div class="h">Your home</div>
        <div class="k">Above grade</div><div>${c.ag.toLocaleString()} sq ft</div><div>2,210 sq ft</div>
        <div class="k">Lower level</div><div>${c.bg? c.bg.toLocaleString()+' sq ft':'—'}<br><small>${c.bgNote}</small></div><div>≈ 724 sq ft<br><small>Finished</small></div>
        <div class="k">Bedrooms</div><div>${c.beds}</div><div>4 + 1 lower</div>
        <div class="k">Baths</div><div>${c.baths}</div><div>3.5</div>
        <div class="k">Lot</div><div>${c.lot}</div><div>0.389 ac</div>
        <div class="k">Built</div><div>${c.built}</div><div>2012</div>
      </div>
      <p class="comp__why">${c.why}</p>
      <p class="comp__src">Details: <a href="${c.src}" target="_blank" rel="noopener">${c.srcName}</a></p>
    </div>
    <div>
      <div class="wf">${rows}</div>
      <div class="wf__weight"><span>Weight in final value</span><span class="meter"><i style="width:${c.weight*100}%"></i></span><strong>${Math.round(c.weight*100)}%</strong></div>
      <p class="note">Green adds value because your home is superior in that respect; rust subtracts because the sale is superior.</p>
    </div>`;
}
tabs.addEventListener('click',e=>{const b=e.target.closest('button'); if(b) renderComp(b.dataset.id);});
tabs.addEventListener('keydown',e=>{
  const btns=[...tabs.querySelectorAll('button')]; const i=btns.indexOf(document.activeElement); if(i<0) return;
  let n=null; if(e.key==='ArrowRight') n=(i+1)%btns.length; if(e.key==='ArrowLeft') n=(i-1+btns.length)%btns.length;
  if(n!==null){e.preventDefault(); btns[n].focus(); renderComp(btns[n].dataset.id);}
});
let currentComp='48';
const _render=renderComp; renderComp=function(id){currentComp=id;_render(id);};

/* ---------- Weighted bars ---------- */
const bars = document.getElementById('bars');
function renderBars(){
  const lo=380000, hi=460000, p=v=>Math.max(0,Math.min(100,(v-lo)/(hi-lo)*100));
  let total=0, pre=0;
  let h = [...comps].sort((a,b)=>b.weight-a.weight).map(c=>{
    const adj=c.pre*(1-soft); total+=adj*c.weight; pre+=c.pre*c.weight;
    return `<div class="bar"><span class="nm">${c.addr.replace(' Dr','')}<small>${Math.round(c.weight*100)}% weight</small></span><span class="tr"><i style="width:${p(adj)}%"></i><em style="left:${p(435000)}%" title="$435,000 reconciled value"></em></span><span class="v">${fmt(adj)}</span></div>`;
  }).join('');
  h += `<div class="bars__foot"><span>Scale: $380K to $460K</span><span>Navy line = $435,000 reconciled value</span></div>`;
  bars.innerHTML = h;
  document.getElementById('weighted').textContent = fmt(Math.round(total/100)*100);
  document.getElementById('weightednote').textContent = `Before the allowance: ${fmt(Math.round(pre/100)*100)}`;
}
const softIn=document.getElementById('soft'), softOut=document.getElementById('softout');
softIn.addEventListener('input',()=>{
  soft = Number(softIn.value)/100; softOut.textContent = (soft*100).toFixed(1)+'%';
  renderBars(); renderComp(currentComp);
});
renderComp('48'); renderBars();

/* ---------- Map ---------- */
const list = document.getElementById('maplist');
const items = [{...subject, kind:'you', label:'★', title:'Your home', sub:'195 Joshua Dr · 0.389 ac'}]
  .concat(comps.map((c,i)=>({...c, kind:'sold', label:String(i+1), title:c.addr, sub:`Sold ${fmt(c.price)} · ${c.date}`})))
  .concat([{...active, kind:'act', label:'A', title:active.addr, sub:`Listed ${fmt(active.price)} · reduced from $475,000`}]);
list.innerHTML = items.map(it=>`<li><button data-id="${it.id}"><span class="num ${it.kind==='you'?'num--you':it.kind==='act'?'num--act':''}">${it.label}</span><span>${it.title}<small>${it.sub}</small></span><span class="d">${it.kind==='you'?'':it.dist.toFixed(2)+' mi'}</span></button></li>`).join('');

let map=null; const markers={};
function initMap(){
  if(typeof L==='undefined'){document.getElementById('leaflet').innerHTML='<p style="padding:1rem">The map could not load. The list shows all locations.</p>';return;}
  map = L.map('leaflet',{scrollWheelZoom:false, zoomControl:true}).setView([subject.lat,subject.lng],16);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:19, attribution:'&copy; OpenStreetMap contributors'}).addTo(map);
  const bounds=[];
  items.forEach(it=>{
    const cls = it.kind==='you'?'pin pin--you':it.kind==='act'?'pin pin--act':'pin';
    const sz = it.kind==='you'?34:28;
    const icon = L.divIcon({className:'', html:`<span class="${cls}">${it.label}</span>`, iconSize:[sz,sz], iconAnchor:[sz/2,sz/2]});
    const m = L.marker([it.lat,it.lng],{icon, title:it.title, zIndexOffset: it.kind==='you'?1000:0}).addTo(map);
    m.bindPopup(`<strong>${it.title}</strong><br>${it.sub}${it.kind==='you'?'':'<br>'+it.dist.toFixed(2)+' mi from your home'}`);
    m.on('click',()=>highlight(it.id,false));
    markers[it.id]=m; bounds.push([it.lat,it.lng]);
  });
  map.fitBounds(bounds,{padding:[40,40]});
}
function highlight(id, fly){
  list.querySelectorAll('button').forEach(b=>b.classList.toggle('on', b.dataset.id===id));
  if(map && markers[id]){ if(fly) map.panTo(markers[id].getLatLng()); markers[id].openPopup(); }
}
list.addEventListener('click',e=>{const b=e.target.closest('button'); if(!b) return; highlight(b.dataset.id,true);
  if(comps.some(c=>c.id===b.dataset.id)) renderComp(b.dataset.id);
});
if(document.readyState==='complete') initMap(); else window.addEventListener('load', initMap);
})();
