from django.contrib import admin
from .models import MainBlock, Questions, FAQ, Docs, News

@admin.register(MainBlock)
class MainBlockAdmin(admin.ModelAdmin):
    list_display = ("title", "undertitle", "description")

admin.site.register(Questions)
admin.site.register(FAQ)
admin.site.register(Docs)
admin.site.register(News)