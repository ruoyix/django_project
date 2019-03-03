from django.contrib import admin
from . import models as m


# 管理页面模型注册
admin.site.register(m.Fruit)
admin.site.register(m.Drink)
admin.site.register(m.Snack)
admin.site.register(m.Dayly)
admin.site.register(m.Electron)

