// animation for login
var 
    buDelete_login = document.querySelector('.backAccount .clos'),
    headup         = document.querySelector('.backAccount .content .hedTop'),
    bxcontent      = document.querySelector('.backAccount .content'),
    s_facebook     = document.querySelectorAll('.backAccount .content .login .logBy .social')[0],
    s_google       = document.querySelectorAll('.backAccount .content .login .logBy .social')[1],
    inp_email      = document.querySelectorAll('.backAccount .content .login form .inp')[0],
    inp_pass       = document.querySelectorAll('.backAccount .content .login form .inp')[1],
    forget         = document.querySelector('.backAccount .content .login form .forget'),
    buNext         = document.querySelector('.backAccount .content .login form .next'),
    bu_or          = document.querySelector('.backAccount .content .login .creat .orr'),
    bu_loginUp     = document.querySelector('.backAccount .content .login .creat a h3');
buDelete_login.addEventListener('click',function(){
    //bu_loginUp
    bu_loginUp.style.transition = 'all 0.2s ease';
    bu_loginUp.style.transform = 'translateX(62px)';
    bu_loginUp.style.opacity = '0';
    //bu_or
    bu_or.style.transition = 'all 0.2s ease';
    bu_or.style.transform = 'rotate(-70deg)';
    bu_or.style.opacity = '0';
    setTimeout(function(){
        //inp_pass
        inp_pass.style.transition = 'all 0.2s ease';
        inp_pass.style.transform = 'translateX(123px)skew(-15deg)scale(0.8)';
        inp_pass.style.opacity = '0';
        //buNext
        buNext.style.transition = 'all 0.2s ease';
        buNext.style.transform = 'translateX(123px)skew(-15deg)scale(0.8)';
        buNext.style.opacity = '0';
        setTimeout(function(){
            //inp_email
            inp_email.style.transition = 'all 0.2s ease';
            inp_email.style.transform = 'translateX(123px)skew(-15deg)scale(0.8)';
            inp_email.style.opacity = '0';
        },100);
    },40);

});