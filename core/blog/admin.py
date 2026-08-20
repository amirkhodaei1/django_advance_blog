from django.contrib import admin

from .models import Category, Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "title",
        "status",
        "category",
        "created_date",
        "category",
    ]


admin.site.register(Category)
