from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'get_name', 'email', 'is_staff')

    # 사용자 이름을 'first_name'에서 가져오도록 설정
    def get_name(self, obj):
        return f"{obj.first_name}"  # 전체 이름이 first_name에 저장
    get_name.short_description = '이름'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
