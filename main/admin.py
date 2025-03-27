from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import MainBlock, WelcomeBlock, Questions, FAQ, Memo, News, Advantages, Performance, PerformanceItems, Reviews

@admin.register(MainBlock)
class MainBlockAdmin(admin.ModelAdmin):
    list_display = ("title", "undertitle", "description")

@admin.register(WelcomeBlock)
class WelcomeBlockAdmin(admin.ModelAdmin):
    list_display = ("title", "undertitle", "description", "preview")
    
    # Предпросмотр картинки элемента
    readonly_fields = ["preview"]
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.sign.url}" style="max-height: 100px;">')

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("name", "phoneNumber", "question", "status", "create_at", "updated_at")

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ("name", "doc")

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "preview")

    # Предпросмотр картинки элемента
    readonly_fields = ["preview"]
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;">')

@admin.register(Advantages)
class AdvantagesAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "preview")

    # Предпросмотр картинки элемента
    readonly_fields = ["preview"]
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;">')
    
@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("title", "preview")
    # Предпросмотр картинки элемента
    readonly_fields = ["preview"]
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" style="max-height: 100px;">')
    
@admin.register(PerformanceItems)
class PerformanceItemsAdmin(admin.ModelAdmin):
    list_display = ("description", )

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "review", "published")