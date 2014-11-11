from django.contrib import admin
from blog.models import Quote, Post, Tag, Category

admin.site.register(Quote)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)