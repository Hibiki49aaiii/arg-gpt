(function(){
'use strict';

var KEY='district8-act6-state';
var canonical={
  S1:'PARK',
  S2:'VENDING_MACHINE',
  S3:'BLUE_FENCE',
  S4:'OLD_EIGHT_MEETING_HALL',
  S5:'BUS_STOP',
  S6:'RESIDENTIAL_CLUSTER'
};

function fresh(){
  return {
    state:'MAP_INCOMPLETE',
    realityB:false,
    observed:{site007:false,site00108:false},
    ending:null,
    baseline:{site007:'A',site00108:'A'}
  };
}
function load(){
  try{
    var raw=localStorage.getItem(KEY);
    if(!raw)return fresh();
    var data=JSON.parse(raw);
    return Object.assign(fresh(),data,{observed:Object.assign({site007:false,site00108:false},data.observed||{})});
  }catch(e){return fresh();}
}
function save(s){try{localStorage.setItem(KEY,JSON.stringify(s));}catch(e){}}
function setState(next){save(next);return next;}

function solveMap(){
  var s=load();
  var chosen={};
  Object.keys(canonical).forEach(function(slot){
    var el=document.getElementById('slot-'+slot);
    chosen[slot]=el?el.value:'';
  });
  var values=Object.values(chosen);
  var unique=(new Set(values.filter(Boolean))).size===6;
  var correct=unique&&Object.keys(canonical).every(function(k){return chosen[k]===canonical[k];});
  var out=document.querySelector('[data-map-status]');
  if(!out)return;
  out.hidden=false;
  if(!correct){
    out.textContent='この配置では、部分地図と距離表を同時に満たしません。各資料の関係を再確認してください。';
    return;
  }
  s.state='MAP_COMPLETE_UNOBSERVED';
  s.realityB=true;
  s.observed={site007:false,site00108:false};
  setState(s);
  out.textContent='統合復元図を保存しました。';
  var after=document.querySelector('[data-map-solved]');
  if(after)after.hidden=false;
}
function resetMap(){
  Object.keys(canonical).forEach(function(slot){
    var el=document.getElementById('slot-'+slot);
    if(el)el.selectedIndex=0;
  });
  var out=document.querySelector('[data-map-status]');
  if(out)out.hidden=true;
}

function markAnchor(which){
  var s=load();
  if(!s.realityB)return s;
  s.observed[which]=true;
  if(s.observed.site007&&s.observed.site00108){
    s.state='PZ012_OBSERVED';
  }else{
    s.state='REALITY_CHANGE_OBSERVED';
  }
  return setState(s);
}

function initWorkspace(){
  if(!document.querySelector('[data-workspace]'))return;
  var solve=document.querySelector('[data-check-map]');
  var reset=document.querySelector('[data-reset-map]');
  if(solve)solve.addEventListener('click',solveMap);
  if(reset)reset.addEventListener('click',resetMap);

  var s=load();
  if(s.state!=='MAP_INCOMPLETE'){
    var after=document.querySelector('[data-map-solved]');
    if(after)after.hidden=false;
  }
  if(s.state==='PZ012_OBSERVED'||s.ending){
    var synthesis=document.querySelector('[data-pz012-observed]');
    if(synthesis)synthesis.hidden=false;
  }
}

function initGeneratedMap(){
  var root=document.querySelector('[data-generated-map]');
  if(!root)return;
  var s=load();
  var unavailable=document.querySelector('[data-map-unavailable]');
  var artifact=document.querySelector('[data-map-artifact]');
  if(s.state==='MAP_INCOMPLETE'){
    if(unavailable)unavailable.hidden=false;
    if(artifact)artifact.hidden=true;
  }else{
    if(unavailable)unavailable.hidden=true;
    if(artifact)artifact.hidden=false;
  }
}

function initSite007(){
  if(!document.querySelector('[data-site007]'))return;
  var s=load();
  var row=document.querySelector('[data-area8-row]');
  var legend=document.querySelector('[data-area8-legend]');
  if(s.realityB){
    if(row)row.hidden=false;
    if(legend)legend.hidden=false;
    markAnchor('site007');
  }else{
    if(row)row.hidden=true;
    if(legend)legend.hidden=true;
  }
}

function initOld08(){
  if(!document.querySelector('[data-old08]'))return;
  var s=load();
  var a=document.querySelector('[data-old08-a]');
  var b=document.querySelector('[data-old08-b]');
  if(s.realityB){
    if(a)a.hidden=true;
    if(b)b.hidden=false;
    markAnchor('site00108');
  }else{
    if(a)a.hidden=false;
    if(b)b.hidden=true;
  }
}

function initEnding(){
  if(!document.querySelector('[data-ending]'))return;
  var s=load();
  var locked=document.querySelector('[data-ending-locked]');
  var choices=document.querySelector('[data-ending-choices]');
  var allowed=(s.state==='PZ012_OBSERVED'||!!s.ending);
  if(locked)locked.hidden=allowed;
  if(choices)choices.hidden=!allowed;

  document.querySelectorAll('button[data-ending-choice]').forEach(function(btn){
    btn.addEventListener('click',function(){
      var id=btn.dataset.endingChoice;
      var st=load();
      if(st.state!=='PZ012_OBSERVED'&&!st.ending)return;
      st.ending=id;
      st.state='ENDING_SELECTED';
      st.realityB=(id==='END-A');
      setState(st);
      location.href='/ending/result/';
    });
  });
}

function initEndingResult(){
  if(!document.querySelector('[data-ending-result]'))return;
  var s=load();
  var blocks=document.querySelectorAll('[data-result-id]');
  blocks.forEach(function(x){x.hidden=x.dataset.resultId!==s.ending;});
  var none=document.querySelector('[data-result-none]');
  if(none)none.hidden=!!s.ending;
}

function initMeta(){
  if(!document.querySelector('[data-meta-tool]'))return;
  var out=document.querySelector('[data-state-json]');
  function render(){if(out)out.value=JSON.stringify(load(),null,2);}
  var reset=document.querySelector('[data-reset-state]');
  if(reset)reset.addEventListener('click',function(){try{localStorage.removeItem(KEY);}catch(e){}render();});
  render();
}

document.addEventListener('DOMContentLoaded',function(){
  initWorkspace();
  initGeneratedMap();
  initSite007();
  initOld08();
  initEnding();
  initEndingResult();
  initMeta();
});
})();