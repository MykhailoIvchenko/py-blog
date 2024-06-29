from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary


@admin.register(User)
class AuthorAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("created_time",)


admin.site.unregister(Group)