(function(){
'use strict';
function initCompare(){
  var root=document.querySelector('[data-compare]');
  if(!root)return;

  var a1=document.getElementById('anchor-1');
  var a2=document.getElementById('anchor-2');
  var solve=document.getElementById('apply-alignment');
  var reset=document.getElementById('reset-alignment');
  var result=document.getElementById('alignment-result');
  var unsolved=document.getElementById('unsolved-table');
  var solved=document.getElementById('solved-table');
  var state=document.getElementById('alignment-state');

  function showUnsolved(message){
    result.hidden=true;
    solved.hidden=true;
    unsolved.hidden=false;
    state.textContent=message||'時間軸は未補正です。';
  }

  solve.addEventListener('click',function(){
    var first=a1.value;
    var second=a2.value;
    var valid=(first==='opening'&&second==='closing')||(first==='closing'&&second==='opening');
    if(valid){
      unsolved.hidden=true;
      solved.hidden=false;
      result.hidden=false;
      state.textContent='2つの通常放送Anchorで時間軸を補正しました。送信終了は27.000秒です。';
      try{localStorage.setItem('district8-act3-aligned','1')}catch(e){}
    }else{
      showUnsolved('この2点では同一の通常放送区間を安定して補正できません。別の共通音を選んでください。');
    }
  });

  reset.addEventListener('click',function(){
    a1.value='opening';
    a2.value='unknown-final';
    try{localStorage.removeItem('district8-act3-aligned')}catch(e){}
    showUnsolved('時間軸をリセットしました。');
  });

  var restored=false;
  try{restored=localStorage.getItem('district8-act3-aligned')==='1'}catch(e){}
  if(restored){
    a1.value='opening';a2.value='closing';
    unsolved.hidden=true;solved.hidden=false;result.hidden=false;
    state.textContent='保存されていた補正状態を表示しています。送信終了は27.000秒です。';
  }else{
    showUnsolved();
  }
}
document.addEventListener('DOMContentLoaded',initCompare);
})();