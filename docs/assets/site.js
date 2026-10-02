// 霞桜団HP 共通スクリプト
// ・スクロール量でヘッダーを透明/すりガラスに切替
// ・ページ内リンク(#about等)は表示中のセクションのメニューに下線
(function(){
  var n=document.querySelector('header.nav');
  var spy=[].slice.call(document.querySelectorAll('nav.links a[href^="#"]'));
  function onScroll(){
    if(n){var y=window.scrollY>10;n.classList.toggle('scrolled',y);n.classList.toggle('top',!y);}
    spy.forEach(function(a){var s=document.querySelector(a.getAttribute('href'));if(!s)return;
      var r=s.getBoundingClientRect();a.classList.toggle('active',r.top<200&&r.bottom>200);});
  }
  addEventListener('scroll',onScroll,{passive:true});onScroll();
})();
