$(function(){
  'use strict'
  //Nice Scroll
  $("html").niceScroll({styler:"fb",cursorcolor:"#f03755 ", cursorwidth: '16px', cursorborderradius: '0px', background: '#3c3c3c', spacebarenabled:false, cursorborder: '0',  zindex: '1000'});
  //Add Active For type mael Fameal
  $('.profile .forms .users ul li').click(function(){
    $(this).addClass('active').siblings().removeClass('active');
  });

  //Add Active For type mael Fameal
  $('.header .navbar .nav-link').click(function(){
    $(this).addClass('active').siblings().removeClass('active');
  });
});

//Counter Up
const counter = document.querySelectorAll('.count');
const speed = 200;
counter.forEach(count => {
  const updateCount = () => {
    const target = +count.getAttribute('data-target');
    const countt = +count.innerText;

    const inc = target / speed;
    
    if (countt < target) {
      count.innerText = countt + inc;
      setTimeout(updateCount, 1);
    }else{
      count.innerText = target;
    }

  }
  updateCount();
});



