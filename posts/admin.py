from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "link", "creation_date", "upvotes_ammount"]
    fields = ["title", "link", "creation_date", "upvotes_ammount", "author"]
    readonly_fields = ["upvotes_ammount", "creation_date"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["author", "post", "creation_date"]
    fields = ["author", "post", "creation_date", "content"]
    readonly_fields = ["creation_date"]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
