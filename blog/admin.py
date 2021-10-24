from django.contrib import admin
from .models import job, contactStuff
# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    search_fields = ['title',]
admin.site.register(job, PhotoAdmin)
class con(admin.ModelAdmin):
    search_fields = ['email']
admin.site.register(contactStuff, con)
