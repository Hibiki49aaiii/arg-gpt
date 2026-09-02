(function(){
'use strict';

function initMap(){
  var root=document.querySelector('[data-map-compare]');
  if(!root)return;
  var status=document.querySelector('[data-map-status]');
  var solved=document.querySelector('[data-map-solved]');
  document.querySelector('[data-lock-map]').addEventListener('click',function(){
    var a=document.getElementById('anchor-a').value;
    var b=document.getElementById('anchor-b').value;
    var c=document.getElementById('anchor-c').value;
    var ok=a==='river'&&b==='civic'&&c==='railway';
    if(ok){
      status.textContent='固定基準点A/B/Cを登録しました。4版を同一座標系で比較できます。';
      status.className='good';
      solved.hidden=false;
      try{localStorage.setItem('district8-act5-map','1')}catch(e){}
    }else{
      status.textContent='基準点の対応が一致しません。変化していない河川・公共施設・鉄道位置を確認してください。';
      status.className='bad';
      solved.hidden=true;
    }
  });
}

function initCitation(){
  var root=document.querySelector('[data-reverse-citation]');
  if(!root)return;
  var status=document.querySelector('[data-citation-status]');
  var solved=document.querySelector('[data-citation-solved]');
  document.querySelector('[data-synthesize-citations]').addEventListener('click',function(){
    var checked=Array.prototype.slice.call(root.querySelectorAll('input[data-citation]')).filter(function(x){return x.checked});
    if(checked.length===4){
      status.textContent='4.3を参照する生存箇所を4件まとめました。';
      status.className='good';
      solved.hidden=false;
      try{localStorage.setItem('district8-act5-citations','1')}catch(e){}
    }else{
      status.textContent='欠落節を直接推測せず、4.3を参照している箇所をすべて集めてください。';
      status.className='bad';
      solved.hidden=true;
    }
  });
}

var saegusaCorrect=['S-1999','S-2005','S-2007','S-2008','S-2009'];

function initSaegusa(){
  var list=document.querySelector('[data-saegusa-list]');
  if(!list)return;
  var status=document.querySelector('[data-saegusa-status]');
  var solved=document.querySelector('[data-saegusa-solved]');

  function update(){
    var cards=list.querySelectorAll('[data-saegusa-id]');
    Array.prototype.forEach.call(cards,function(card,i){
      var p=card.querySelector('[data-position]');
      if(p)p.textContent=(i+1)+' / '+cards.length;
    });
  }
  list.addEventListener('click',function(e){
    var btn=e.target.closest('button[data-move]');
    if(!btn)return;
    var card=btn.closest('[data-saegusa-id]');
    var cards=Array.prototype.slice.call(list.querySelectorAll('[data-saegusa-id]'));
    var i=cards.indexOf(card);
    var d=btn.getAttribute('data-move')==='up'?-1:1;
    var j=i+d;
    if(j<0||j>=cards.length)return;
    if(d<0)list.insertBefore(card,cards[j]);
    else list.insertBefore(cards[j],card);
    update();
    solved.hidden=true;
    status.textContent='順序を変更しました。';
    status.className='';
  });
  document.querySelector('[data-check-saegusa]').addEventListener('click',function(){
    var ids=Array.prototype.map.call(list.querySelectorAll('[data-saegusa-id]'),function(x){return x.getAttribute('data-saegusa-id')});
    if(ids.join('|')===saegusaCorrect.join('|')){
      status.textContent='保存・再整理・再発懸念・削除の時系列が一致しました。';
      status.className='good';
      solved.hidden=false;
      try{localStorage.setItem('district8-act5-saegusa','1')}catch(e){}
    }else{
      status.textContent='削除だけを見ず、保存方針と再整理の時期を含めて並べてください。';
      status.className='bad';
      solved.hidden=true;
    }
  });
  update();
}

document.addEventListener('DOMContentLoaded',function(){initMap();initCitation();initSaegusa();});
})();