from django.contrib import admin
from .models import Fcuser


class FcuserAdmin(admin.ModelAdmin):
    # model class 안에 있는 field가 list up
    list_display = ('username', 'password')


admin.site.register(Fcuser, FcuserAdmin)
