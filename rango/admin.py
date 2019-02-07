# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rango.models import UserProfile
from django.contrib import admin
from rango.models import Category
from rango.models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name' ,)}



admin.site.register(UserProfile)                    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
