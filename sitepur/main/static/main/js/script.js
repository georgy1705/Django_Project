$(document).ready(function(){
    $('.single-item').slick({
        draggable: false,
        arrows: true,
        dots: true,
        infinite: true,
        speed: 500,
        fade: true,
        cssEase: 'linear'
    });
    $('[id^="option"]').on('click', function (){
        const el=document.getElementById("size");
        el.placeholder = "Выбранный размер: " + $('input[name=options]:checked').val()
    });



    $('.type_1 .headingElem').on('click', function (){
    /*записываем в переменную блок с контентом*/
    let thisContentBlock = $(this).parent().find('.descElem');
    /*проверяем есть ли у блока с контентом класс active
      если есть то удаляем, если нет то добавляем */
    if(thisContentBlock.hasClass('active')) {
        thisContentBlock.removeClass('active')
    }
    else {
        thisContentBlock.addClass('active')
    }
    });
});
$(function() {
    $('.topmenu-open').click(function(){
        if($('.topmenu').hasClass("show-topmenu"))
        {
         $('.topmenu').slideToggle(400, function() {
           $('topmenu').removeClass('show-topmenu');
        });

        } else {
        $('.topmenu').slideToggle(400, function() {
           $('.topmenu').addClass('show-topmenu');
        });
        }
        $('body').toggleClass('fixed-page');
    });
});

$(function() {
 let header = $('.header');
 let hederHeight = header.height(); // вычисляем высоту шапки

 $(window).scroll(function() {
   if($(this).scrollTop() > 1) {
    header.addClass('header_fixed');
    $('body').css({
       'paddingTop': hederHeight+'px' // делаем отступ у body, равный высоте шапки
    });
   } else {
    header.removeClass('header_fixed');
    $('body').css({
     'paddingTop': 0 // удаляю отступ у body, равный высоте шапки
    })
   }
 });
});

$(function() {
    var el = document.getElementsByClassName('menu-item');
    for(var i=0; i<el.length; i++) {
        el[i].addEventListener("mouseenter", showSub, false);
        el[i].addEventListener("mouseleave", hideSub, false);
    }

    function showSub(e) {
        if(this.children.length>1) {
          this.children[1].style.height = "auto";
          this.children[1].style.overflow = "visible";
          this.children[1].style.opacity = "1";
        } else {
          return false;
    }
    }

    function hideSub(e) {
        if(this.children.length>1) {
          this.children[1].style.height = "0px";
           this.children[1].style.overflow = "hidden";
           this.children[1].style.opacity = "0";
        } else {
           return false;
    }
}
});






