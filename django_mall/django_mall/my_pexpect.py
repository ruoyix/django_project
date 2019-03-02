from django.contrib.auth.models import User


ruoyi = User.objects.exsits(name="ruoyi")
if not ruoyi:
    username = "ruoyi"
    email = "ruoyi@qq.com"
    password = "ruoyi123456"
    User.objects.create_superuser(username,  email, password)
else:
    pass
print("ruoyi")


