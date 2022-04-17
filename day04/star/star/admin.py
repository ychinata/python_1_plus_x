from django.contrib import admin
from .models import Star, UserPro


# Register your models here.
class StarAdmin(admin.ModelAdmin):
    list_display = ["name", "sex", "age", "profession", "avatar"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "nickname", "email", "gender", "image", "is_staff"]


# 注册模型
admin.site.register(Star, StarAdmin)
admin.site.register(UserPro, UserAdmin)

# 修改后台管理登录的标题
admin.site.site_tile = "star_library"
# admin.site.site_header = "star_library"

