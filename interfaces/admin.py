from django.contrib import admin

# Register your models here.
from interfaces.models import Interface
from projects.models import Projects
#
admin.site.register(Interface)
