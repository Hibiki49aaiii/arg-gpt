(function(){
'use strict';
var STATE_KEY='district8-vs-state';
var EVENT_KEY='district8-vs-events';

function readJson(key,fallback){
  try{return JSON.parse(localStorage.getItem(key)||'')||fallback}catch(e){return fallback}
}
function writeJson(key,value){
  try{localStorage.setItem(key,JSON.stringify(value))}catch(e){}
}
function setState(name){
  if(!name)return;
  var state=readJson(STATE_KEY,{});
  state[name]=true;
  writeJson(STATE_KEY,state);
}
function event(name,props){
  if(!name)return;
  var events=readJson(EVENT_KEY,[]);
  events.push({name:name,at:new Date().toISOString(),props:props||{}});
  if(events.length>100)events=events.slice(-100);
  writeJson(EVENT_KEY,events);
}
function initMeta(){
  document.querySelectorAll('[data-meta-toggle]').forEach(function(btn){
    btn.addEventListener('click',function(){
      var id=btn.getAttribute('aria-controls');
      var panel=document.getElementById(id);
      if(!panel)return;
      var expanded=btn.getAttribute('aria-expanded')==='true';
      btn.setAttribute('aria-expanded',String(!expanded));
      panel.hidden=expanded;
      event('document_metadata_toggled',{document:document.body.getAttribute('data-document')||''});
    });
  });
}
function initDistrict(){
  var root=document.querySelector('[data-district-detail]');
  if(!root)return;
  var params=new URLSearchParams(location.search);
  var id=params.get('id')||'01';
  var districts={
    '01':['中央第一','中央公民館','area01.gif'],
    '02':['中央第二','凪代文化会館','area02.gif'],
    '03':['東部','東部小学校体育館','area03.gif'],
    '04':['西部','西部地区センター','area04.gif'],
    '05':['北部','北部公民館','area05.gif'],
    '06':['南部','南部小学校体育館','area06.gif'],
    '07':['臨海','臨海地区センター','area07.gif']
  };
  if(!districts[id])id='01';
  root.querySelector('[data-name]').textContent='第'+Number(id)+'避難区（'+districts[id][0]+'）';
  root.querySelector('[data-place]').textContent=districts[id][1];
  root.querySelector('[data-file]').textContent=districts[id][2];
  document.title='第'+Number(id)+'避難区｜旧凪代市防災情報';
  if(id==='07'){
    var note=root.querySelector('[data-route-a]');
    note.hidden=false;
    event('area08_trace_seen',{route:'A'});
    setState('found_area08');
  }
  setState('visited_area_index');
}
function renderSearch(form){
  var q=form.querySelector('input[name=q]').value.trim();
  var result=document.querySelector('[data-search-result]');
  result.hidden=false;
  if(q==='旧八号集会所'){
    result.innerHTML='<p><strong>検索結果 0件</strong></p><p>該当する公開資料はありません。</p>';
    event('archive_exact_search_zero',{term:'old-hachigo-hall'});
  }else if(q){
    result.innerHTML='<p><strong>検索結果 1件</strong></p><p><a href="#">地域施設台帳（公開分）</a> — 入力語に近い一般資料です。</p>';
  }else{
    result.innerHTML='<p>検索語を入力してください。</p>';
  }
}
function initSearch(){
  var form=document.querySelector('[data-archive-search]');
  if(!form)return;
  var params=new URLSearchParams(location.search);
  var initial=params.get('q');
  if(initial){
    form.querySelector('input[name=q]').value=initial;
    renderSearch(form);
  }
  form.addEventListener('submit',function(e){
    e.preventDefault();
    renderSearch(form);
  });
}
document.addEventListener('DOMContentLoaded',function(){
  var body=document.body;
  event(body.getAttribute('data-event')||'page_view',{path:location.pathname});
  setState(body.getAttribute('data-state'));
  initMeta();
  initDistrict();
  initSearch();
  document.querySelectorAll('[data-state]').forEach(function(el){
    if(el===body)return;
    el.addEventListener('click',function(){setState(el.getAttribute('data-state'));});
  });
  document.querySelectorAll('[data-clue-route]').forEach(function(el){
    el.addEventListener('click',function(){
      event('area08_trace_seen',{route:el.getAttribute('data-clue-route')});
      setState('found_area08');
    });
  });
});
})();