from django.contrib import admin
from members.models import Member


class MemberAdmin(admin.ModelAdmin):
    fields = ['user', 'photo', 'gender']


admin.site.register(Member)
