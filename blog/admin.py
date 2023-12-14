from django.contrib import admin
from blog.models import Article, Like, Favorites
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ['title', 'author', 'id']
    list_display_links = ['title', 'author', 'id']
    ordering = ['id', '-title']
    list_filter = ['author']
    summernote_fields = '__all__'



admin.site.register(Like)
admin.site.register(Favorites)