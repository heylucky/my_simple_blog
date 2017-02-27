from django.contrib import admin
from models import Article,UserProfile


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',
                    "date_time",
                    "category",
                    )


class UserAdmin(admin.ModelAdmin):
    list_display = ('username',
                    "email",
                    "password",
                    )


admin.site.register(Article,ArticleAdmin)
admin.site.register(UserProfile,UserAdmin)
