from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	change_list_template = "admin/news_change_list.html"
	list_display = ('id', 'tag', 'title', 'detail')
	list_display_links = ('id', 'tag', 'title')
