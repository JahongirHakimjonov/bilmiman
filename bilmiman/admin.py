from django.contrib import admin

from .models import Work, About, Contact


# Register your models here.


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['address', 'email', 'phone']
