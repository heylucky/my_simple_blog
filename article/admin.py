from django.contrib import admin
from models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',
                    "date_time",
                    "category",
                    )

admin.site.register(Article,ArticleAdmin)

