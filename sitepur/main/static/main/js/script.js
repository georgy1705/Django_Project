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
        var el=document.getElementById("size");
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






