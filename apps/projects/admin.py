from django.contrib import admin

# Register your models here.
from apps.projects.models import Projects


class ProjectsAdmin(admin.ModelAdmin):
    '''定制后台管理站点类'''
    # 指定在修改（新增）中需要的字段
    fields = ('name', 'leader', 'tester', 'programer')
    # 指定需要列出的字段
    list_display = ['id', 'name', 'leader', 'programer']


admin.site.register(Projects, ProjectsAdmin)
