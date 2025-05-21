from django.contrib import admin

from .models import Post, Author, Tag, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    """To give different setting to Post models.
    """
    list_filter = ("author", "tag", "date",)  # to get datas by filter
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    """To handle comment model.
    """
    list_display = ("user_name", "post")

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
