from django.contrib import admin
from .models import Activitytype, Menumaster,Submenu,Pagemaster,Coursemaster
# Register your models here.
admin.site.register(Menumaster)
admin.site.register(Pagemaster)
admin.site.register(Coursemaster)
admin.site.register(Submenu)
admin.site.register(Activitytype)