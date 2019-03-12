from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def menu(request):
    context = {'items': ["item"]*10}
    return render(request, "menu.html", context)


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def account(request):
    return render(request, "account.html")


def order(request):
    context = {"info_items": [
            ["0", "/static/img/lemon.jpg"],
            ["1", "/static/img/strawberry2.jpg"],
            ["2", "/static/img/apple.jpg"]
            ]}
    return render(request, "order.html", context)


