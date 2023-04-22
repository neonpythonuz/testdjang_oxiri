from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','nomi','company_name','date','rasm1']

admin.site.register(Portfolio,AdminPortfolio)


class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi',]

admin.site.register(Type,AdminType)



class AdminService(admin.ModelAdmin):
    list_display = ['id','nomi','malumot','rasm1']

admin.site.register(Service,AdminService)


class AdminTeam(admin.ModelAdmin):
    list_display = ['id','ismi',"lavozimi",'malumot','url', 'rasm']

admin.site.register(Team,AdminTeam)



class AdminMurojaat(admin.ModelAdmin):
    list_display = ['id','name', 'mail','title','text','date']

admin.site.register(Murojaat,AdminMurojaat)


class AdminSubscribe(admin.ModelAdmin):
    list_display = ['id','mail']

admin.site.register(Subscribe,AdminSubscribe)