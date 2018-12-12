from django.contrib import admin
from .models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "published",]
    list_filter = ["last_modified", "published"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post
    

admin.site.register(Post, PostModelAdmin)