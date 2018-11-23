# login/admin.py

from django.contrib import admin
from models import *

admin.site.register(User)
admin.site.register(PicTest)
# Register your models here.
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(GoodsInfo,GoodsInfoAdmin)
