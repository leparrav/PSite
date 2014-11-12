from django.contrib import admin
from blog.models import Quote, Post, Tag, Category, Comment

admin.site.register(Quote)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)