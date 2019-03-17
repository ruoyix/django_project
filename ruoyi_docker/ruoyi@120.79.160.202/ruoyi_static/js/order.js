$(document).ready(function(){

    var price1 = Number($('.info_value3').text());
    var price2 = Number($('.info_value5').text());
    var price3 = 0;
    t = 0;
    for ( i in $(".info_media").children(".info_h3") ){
        if ( 0<=i && i<100 ){
            price3 = price3 + Number($("#"+String(t)).text())
        }
        else {
            break;
        }
    }
    price = price3 + price1 - price2
    $(".shop_h2").text(price)
});