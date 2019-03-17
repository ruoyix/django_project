from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def menu(request):
    context = {
        "items1": [
            ["0", "/static/img/apple0.jpg"],
            ["1", "/static/img/apple1.jpg"],
            ["2", "/static/img/apple2.jpg"],
            ["3", "/static/img/apple3.jpg"],
            ["4", "/static/img/apple4.jpg"],
            ["5", "/static/img/apple5.jpg"],
            ["6", "/static/img/apple6.jpg"],
            ["7", "/static/img/apple7.jpg"],
            ["8", "/static/img/apple8.jpg"],
            ["9", "/static/img/apple9.jpg"],
        ],
        "items5": [
            ["0", "/static/img/lemon0.jpg"],
            ["1", "/static/img/lemon1.jpg"],
            ["2", "/static/img/lemon2.jpg"],
            ["3", "/static/img/lemon3.jpg"],
            ["4", "/static/img/lemon4.jpg"],
            ["5", "/static/img/lemon5.jpg"],
            ["6", "/static/img/lemon6.jpg"],
            ["7", "/static/img/lemon7.jpg"],
            ["8", "/static/img/lemon8.jpg"],
            ["9", "/static/img/lemon9.jpg"],
        ],
        "items2": [
            ["0", "/static/img/banana0.jpg"],
            ["1", "/static/img/banana1.jpg"],
            ["2", "/static/img/banana2.jpg"],
            ["3", "/static/img/banana3.jpg"],
            ["4", "/static/img/banana4.jpg"],
            ["5", "/static/img/banana5.jpg"],
            ["6", "/static/img/banana6.jpg"],
            ["7", "/static/img/banana7.jpg"],
            ["8", "/static/img/banana8.jpg"],
            ["9", "/static/img/banana9.jpg"],
        ],
        "items4": [
            ["0", "/static/img/strawberry0.jpg"],
            ["1", "/static/img/strawberry1.jpg"],
            ["2", "/static/img/strawberry2.jpg"],
            ["3", "/static/img/strawberry3.jpg"],
            ["4", "/static/img/strawberry4.jpg"],
            ["5", "/static/img/strawberry5.jpg"],
            ["6", "/static/img/strawberry6.jpg"],
            ["7", "/static/img/strawberry7.jpg"],
            ["8", "/static/img/strawberry8.jpg"],
            ["9", "/static/img/strawberry9.jpg"],
        ],
        "items3": [
            ["0", "/static/img/watermelon0.jpg"],
            ["1", "/static/img/watermelon01.jpg"],
            ["2", "/static/img/watermelon02.jpg"],
            ["3", "/static/img/watermelon03.jpg"],
            ["4", "/static/img/watermelon04.jpg"],
            ["5", "/static/img/watermelon05.jpg"],
            ["6", "/static/img/watermelon06.jpg"],
            ["7", "/static/img/watermelon07.jpg"],
            ["8", "/static/img/watermelon08.jpg"],
            ["9", "/static/img/watermelon09.jpg"],
        ],
    }
    return render(request, "menu.html", context)


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def account(request):
    return render(request, "account.html")


def order(request):
    context = {"info_items": [
            ["0", "/static/img/lemon0.jpg"],
            ["1", "/static/img/strawberry0.jpg"],
            ["2", "/static/img/apple0.jpg"]
            ]}
    return render(request, "order.html", context)


