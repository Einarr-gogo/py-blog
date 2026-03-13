from django.contrib import admin

from blog.models import Commentary, Post, User

from django.contrib.auth.models import Group

# Register your models here.

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner__username", "title")
    search_fields = ("owner__username", "title")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "post",
        "content",
    )
