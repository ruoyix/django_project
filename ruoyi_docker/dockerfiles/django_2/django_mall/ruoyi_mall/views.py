from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
# request属性引用某些要大写如GET,POST
# 提示有局限性,可能可以的没有提示
# 传参注意顺位问题
# 局部修改模型数据之后要save(),然后重新获取数据才能用,因为可能save()失败


# 注册
def register_view(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        User.objects.create_user(username=username, password=password)
        to = redirect(reverse("ruoyi_mall:login"))
        return redirect(to)
    else:
        template_name = "ruoyi_mall/register.html"
        return render(request, template_name)


# 创建超级用户
def createsuperuser_view(request):
    if User.objects.filter(username="ruoyi"):
        to = redirect(reverse("ruoyi_mall:login"))
        return HttpResponse("fail")
    else:
        username = "ruoyi"
        email = "ruoyi@qq.com"
        password = "ruoyi123456"
        User.objects.create_superuser(username, email, password)
        to = redirect(reverse("ruoyi_mall:login"))
        return HttpResponse("success")


# 重写 LoginView, LogoutView, PasswordChangeView视图类
# 登录
class MyLoginView(LoginView):
    template_name = "ruoyi_mall/login.html"


# 注销
class MyLogoutView(LogoutView):
    next_page = "/mall/login"


# 更改密码
class MyPasswordChangeView(PasswordChangeView):
    template_name = "ruoyi_mall/passwd_change.html"
    success_url = "/mall/login",


# 主页
def index_view(request):
    if request.user.is_authenticated:
        # session中初始化购物车信息
        # session属性是Session模型中的session_key字段内容
        # session_key是TextField类型
        if "shopcar" not in request.session.keys():
            request.session["shopcar"] = []
        print(request.user)
        # 自定义物品展示算法
        items = {"Fruit": Fruit, "Drink": Drink, "Snack": Snack, "Dayly": Dayly, "Electron": Electron}
        context = {}
        for key in items:
            for card_id in range(1, 11):
                context[key+"_name_"+str(card_id)] = items[key].objects.get(id=card_id).name
                context[key+"_price_" + str(card_id)] = items[key].objects.get(id=card_id).price
                context[key+"_link_" + str(card_id)] = items[key].objects.get(id=card_id).link
        template_name = 'ruoyi_mall/index.html'
        return render(request, template_name, context)
    else:
        to = reverse("ruoyi_mall:login")
        return redirect(to)


# 物品详情页面
def detail_view(request):
    if request.user.is_authenticated:
        if request.POST:
            context = {
                "img": request.POST["img"],
                "goods_info": request.POST["goods_info"],
                "price": request.POST["price"]
            }
            print(context)
            template_name = 'ruoyi_mall/detail.html'
            return render(request, template_name, context)
        else:
            to = reverse("ruoyi_mall:index")
            return redirect(to)
    else:
        to = reverse("ruoyi_mall:login")
        return redirect(to)


# 添加购物车
def shopcar_add_view(request):
    if request.user.is_authenticated:
        request.session["shopcar"] += [{
            "img": request.POST["img"],
            "goods_info": request.POST["goods_info"],
            "price": request.POST["price"]
        }]
        print(request.session["shopcar"])
        return HttpResponse("ruoyi")
    else:
        to = reverse("ruoyi_mall:login")
        return redirect(to)


# 购物车页面
def shopcar_view(request):
    if request.user.is_authenticated:
        context = {
            "info": [i for i in request.session["shopcar"]]
        }
        template_name = 'ruoyi_mall/shopcar.html'
        return render(request, template_name, context)
    else:
        to = reverse("ruoyi_mall:login")
        return redirect(to)
