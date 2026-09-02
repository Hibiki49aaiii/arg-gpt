(function(){
'use strict';

var correctDiary=['D-01','D-02','D-03','D-04','D-05','D-06','D-07','D-08','D-09','D-10'];

function initDiary(){
  var list=document.querySelector('[data-diary-list]');
  if(!list)return;
  var status=document.querySelector('[data-diary-status]');
  var solved=document.querySelector('[data-diary-solved]');

  function ids(){
    return Array.prototype.map.call(list.querySelectorAll('[data-diary-id]'),function(x){return x.getAttribute('data-diary-id')});
  }
  function updatePosition(card){
    var cards=Array.prototype.slice.call(list.querySelectorAll('[data-diary-id]'));
    cards.forEach(function(x,i){
      var pos=x.querySelector('[data-position]');
      if(pos)pos.textContent=(i+1)+' / '+cards.length;
    });
  }
  function move(card,delta){
    var cards=Array.prototype.slice.call(list.querySelectorAll('[data-diary-id]'));
    var i=cards.indexOf(card);
    var j=i+delta;
    if(j<0||j>=cards.length)return;
    if(delta<0)list.insertBefore(card,cards[j]);
    else list.insertBefore(cards[j],card);
    updatePosition();
    status.textContent='順序を変更しました。';
    solved.hidden=true;
  }
  list.addEventListener('click',function(e){
    var b=e.target.closest('button[data-move]');
    if(!b)return;
    var card=b.closest('[data-diary-id]');
    move(card,b.getAttribute('data-move')==='up'?-1:1);
  });

  var check=document.querySelector('[data-check-diary]');
  if(check)check.addEventListener('click',function(){
    var current=ids();
    var ok=current.join('|')===correctDiary.join('|');
    if(ok){
      status.textContent='資料の時系列が一致しました。';
      status.className='good';
      solved.hidden=false;
      try{localStorage.setItem('district8-act4-diary','1')}catch(e){}
    }else{
      status.textContent='まだ時系列が一致しません。日付ではなく、部活・返却期限・祭り・買い物・試験放送の関係も確認してください。';
      status.className='bad';
      solved.hidden=true;
    }
  });

  var reset=document.querySelector('[data-reset-diary]');
  if(reset)reset.addEventListener('click',function(){
    var initial=['D-08','D-02','D-10','D-04','D-01','D-06','D-09','D-03','D-05','D-07'];
    initial.forEach(function(id){var el=list.querySelector('[data-diary-id="'+id+'"]');if(el)list.appendChild(el)});
    updatePosition();
    status.textContent='初期順序へ戻しました。';
    status.className='';
    solved.hidden=true;
    try{localStorage.removeItem('district8-act4-diary')}catch(e){}
  });

  updatePosition();
}

function initTopology(){
  var root=document.querySelector('[data-topology]');
  if(!root)return;
  var status=document.querySelector('[data-topology-status]');
  var solved=document.querySelector('[data-topology-solved]');
  var check=document.querySelector('[data-check-topology]');

  check.addEventListener('click',function(){
    var vals=['slot1','slot2','slot3','slot4'].map(function(id){return document.getElementById(id).value});
    var foundation=document.getElementById('foundation-location').value;
    var unique=(new Set(vals)).size===4;
    var ok=unique &&
      vals.join('|')==='PARK|VENDING_MACHINE|BLUE_FENCE|TRIANGULAR_ROOF_HALL' &&
      foundation==='PARK';
    if(ok){
      status.textContent='3資料と作文の位置関係が両立します。';
      status.className='good';
      solved.hidden=false;
      try{localStorage.setItem('district8-act4-topology','1')}catch(e){}
    }else{
      status.textContent='この配置では複数資料の視点が同時に成立しません。近い／遠い、坂の上／下の関係を見直してください。';
      status.className='bad';
      solved.hidden=true;
    }
  });
}

document.addEventListener('DOMContentLoaded',function(){initDiary();initTopology();});
})();