from django.contrib import admin

from player_site.models import Card, CardSession
# Register your models here.

admin.site.register(CardSession)


@admin.register(Card)
class CardFilter(admin.ModelAdmin):
    list_display = ('id', "slug", "session", "is_active")
    list_filter = ("is_active",)
    list_editable = ("is_active",)
    list_display_links = ("slug",)
    search_fields = ("slug",)
