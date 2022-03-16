from asyncore import read
from django.contrib import admin
from .models import Article, Category

# Register your models here.

#this class is to show  those propierties, just to be read it
# and not modified
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at' , 'updated_at')

admin.site.register (Article, ArticleAdmin)
admin.site.register (Category)
