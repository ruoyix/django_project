$(document).ready(function(){
    $(".tab_btn").click(function(){
        var price1 = Number($(this).siblings(".tab_h5").text());
        var price2 = Number($(".shop_h2").text());
        price3 = price1+price2;
        $(".shop_h2").text(price3);
        var number = Number($(".shop_span").text());
        number = number + 1;
        $(".shop_span").text(number);
    });
});