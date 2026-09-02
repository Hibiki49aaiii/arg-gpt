(function(){
'use strict';
function setupSearch(formSelector,resultSelector,mode){
  var form=document.querySelector(formSelector);
  var result=document.querySelector(resultSelector);
  if(!form||!result)return;
  function render(){
    var q=form.querySelector('input[name=q]').value.trim().replace(/\s+/g,' ');
    result.hidden=false;
    if(mode==='documents'){
      if(q==='防災第215号'||q==='215'){
        result.innerHTML='<p><strong>1件</strong></p><p><a href="/act2/documents/215/">防災第215号　臨時管理区分の設定について</a> <span class="status">一部公開</span></p>';
      }else if(q==='第八避難区'){
        result.innerHTML='<p><strong>3件</strong></p><ul><li>防災第214号 追補</li><li>防災第216号 改訂履歴</li><li><a href="/act2/documents/215/">防災第215号　臨時管理区分の設定について</a></li></ul>';
      }else{
        result.innerHTML='<p>一致する公開資料はありません。</p>';
      }
    }else if(mode==='school'){
      if(q==='水城 結'||q==='水城結'){
        result.innerHTML='<p><strong>2件</strong></p><ul><li><a href="/act2/school/junior-high/1997/yui-mizuki/">平成8年度 卒業台帳 — 水城 結</a></li><li><a href="/act2/school/high-school/1998/enrollment/">平成10年度 在籍確認 — 水城 結</a></li></ul>';
      }else{
        result.innerHTML='<p>該当する公開資料はありません。</p>';
      }
    }
  }
  var params=new URLSearchParams(location.search);
  if(params.get('q')){form.querySelector('input[name=q]').value=params.get('q');render();}
  form.addEventListener('submit',function(e){e.preventDefault();render();});
}
document.addEventListener('DOMContentLoaded',function(){
  setupSearch('[data-document-search]','[data-document-results]','documents');
  setupSearch('[data-school-search]','[data-school-results]','school');
});
})();