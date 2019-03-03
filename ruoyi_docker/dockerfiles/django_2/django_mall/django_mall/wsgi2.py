"""
WSGI config for django_mall project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
# 创建超级用户
from django.contrib.auth.models import User

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_mall.settings")

application = get_wsgi_application()

# 个人添加代码
if User.objects.filter(username="ruoyi"):
    pass
else:
    username = "ruoyi"
    email = "ruoyi@qq.com"
    password = "ruoyi123456"
    User.objects.create_superuser(username,  email, password)

