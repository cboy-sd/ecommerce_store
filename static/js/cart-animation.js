// animation for cart
var 
    buDelete = document.querySelectorAll('.backgrou .contt .courses .groupp .delate');

for(var i=0;i<buDelete.length;i++){
    buDelete[i].parentNode.style.transition = 'all 0.2s ease-in';
    buDelete[i].addEventListener('click',function(){
        this.style.background = '#FF8484';
        this.style.transition = 'all 0.2s ease-in';
        var parentDelete = this.parentNode;
        parentDelete.style.transition = 'all 0.2s ease-in';
        parentDelete.style.opacity= '0';
        parentDelete.style.transform = 'translateX(107%)scale(0.85)skew(-3deg,-5deg)';
        setTimeout(function(){
            parentDelete.style.display= 'none';
        },250);
    });
}
// animation for cart || close
var 
    cartbox = document.querySelector('.backgrou .contt'),
    tabs    = document.querySelector('.backgrou .tabb'),
    card_close = document.querySelector('.backgrou .clos'),
    card_show = document.querySelector('.web .showcart');

    card_close.style.transition = 'all 0.2s ease-in';
// hide
card_close.addEventListener('click',function(){
    card_close.style.transform = 'rotate(-71deg)translateX(52px)';
    card_close.style.opacity = '0';
    cartbox.style.transition = 'all 0.2s ease-in';
    cartbox.style.transform = 'translateY(107%)scale(0.85)skew(-3deg,-5deg)';
    cartbox.style.opacity = '0';
    setTimeout(function(){
        //cartbox.style.display= 'none';
        tabs.style.transition = 'all 0.2s ease-in';
        tabs.style.transform = 'translateY(-120%)scale(0.85)skew(-3deg,-5deg)';
        tabs.style.opacity = '0';
    },40);
});
// show
card_show.addEventListener('click',function(){
    cartbox.style.transition = 'all 0.3s ease-in';
    cartbox.style.transform = 'translateY(0)scale(1)skew(0,0)';
    cartbox.style.opacity = '1';
    setTimeout(function(){
        //cartbox.style.display= 'none';
        tabs.style.transition = 'all 0.2s ease-in';
        tabs.style.transform = 'translateY(0)scale(1)skew(0,0)';
        tabs.style.opacity = '1';
        setTimeout(function(){
            card_close.style.transform = 'rotate(0)translateX(0)';
            card_close.style.opacity = '1';
        },10);
    },20);
});