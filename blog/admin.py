from django.contrib import admin

from .models import Post, Author, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    """To give different setting to Post models.
    """
    list_filter = ("author", "tag", "date",)  # to get datas by filter
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
