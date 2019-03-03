from django.contrib.auth.models import User


if User.objects.filter(username="ruoyi"):
    pass
else:
    username = "ruoyi"
    email = "ruoyi@qq.com"
    password = "ruoyi123456"
    User.objects.create_superuser(username,  email, password)

