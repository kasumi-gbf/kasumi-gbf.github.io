// 霞桜団HP 共通スクリプト
// ・TOP絵(.hero)に舞う花びらを生成(位置・速さ・揺れ幅を1枚ずつばらす)
// ・スクロール量でヘッダーを透明/すりガラスに切替
// ・ページ内リンク(#about等)は表示中のセクションのメニューに下線
(function(){
  var h=document.querySelector('.hero');
  if(h){
    var f=document.createElement('div');f.className='hero-fall';f.setAttribute('aria-hidden','true');
    for(var i=0;i<14;i++){
      var p=document.createElement('i'),d=16+Math.random()*12;
      p.style.cssText='left:'+(Math.random()*100)+'%;--dur:'+d+'s;--delay:'+(-Math.random()*d)+'s;--sway:'
        +(30+Math.random()*70)*(Math.random()<.5?-1:1)+'px;--op:'+(.45+Math.random()*.4)+';scale:'+(.6+Math.random()*.7);
      f.appendChild(p);
    }
    h.insertBefore(f,h.querySelector('.heroin'));
  }
  var n=document.querySelector('header.nav');
  var spy=[].slice.call(document.querySelectorAll('nav.links a[href^="#"]'));
  function onScroll(){
    if(n){var y=window.scrollY>10;n.classList.toggle('scrolled',y);n.classList.toggle('top',!y);}
    spy.forEach(function(a){var s=document.querySelector(a.getAttribute('href'));if(!s)return;
      var r=s.getBoundingClientRect();a.classList.toggle('active',r.top<200&&r.bottom>200);});
  }
  addEventListener('scroll',onScroll,{passive:true});onScroll();
})();
