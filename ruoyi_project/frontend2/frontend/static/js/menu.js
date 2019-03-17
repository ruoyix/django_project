$(document).ready(function(){
    $(".tab_btn").click(function(){
        var price1 = Number($(this).siblings(".tab_h4").text().split("￥")[1]);
        var price2 = Number($(".shop_h1").text().split("￥")[1]);
        price3 = price1+price2;
        $(".shop_h1").text("￥"+String(price3));
        var number = Number($(".shop_span").text());
        number = number + 1;
        $(".shop_span").text(number);
        var name = $(this).siblings(".tab_h3").text();
        var item0 = "<hr class='m-0'>"
        var item1 = "<nav class='navbar'>\n"
        var item2 = "   <a class='navbar-item'>"+name+"</a>\n"
        var item3 = "   <a class='navbar-item shopcar_a2'>￥"+String(price1)+"</a>\n"
        var item4 = "   <button type='button' class='btn btn-primary shopcar_btn'><h6>-</h6></button></nav>\n"
        var item = item1+item2+item3+item4+item0
        $("#shopcar").append(item);
    });
    $("#shopcar").on("mouseenter", function(){
        $(".shopcar_btn").unbind("click").click(function(){
            var price4 = Number($(this).siblings(".shopcar_a2").text().split("￥")[1]);
            var price5 = Number($(".shop_h1").text().split("￥")[1]);
            price6 = price5-price4;
            $(".shop_h1").text("￥"+String(price6));
            var number = Number($(".shop_span").text());
            number = number - 1;
            $(".shop_span").text(number);
            $(this).parent().remove();
            $(this).parent().next().remove();
        });

    })
});