from django.contrib import admin

from games.models import Game, GameBoard, CardFamily, Card

# Register your models here.

@admin.register(Game)
class GameFilter(admin.ModelAdmin):
    list_display = ('id', 'title')
    # list_filter = ('title', 'card_type', 'session')
    list_display_links = ('title',)
    search_fields = ('title',)
    
@admin.register(GameBoard)
class GameBoardFilter(admin.ModelAdmin):
    list_display = ('id', 'name', 'game')
    # list_filter = ('title', 'card_type', 'session')
    list_display_links = ('name',)
    search_fields = ('name',)
    
@admin.register(CardFamily)
class CardFamilyFilter(admin.ModelAdmin):
    list_display = ('id', 'title', 'game')
    # list_filter = ('title', 'card_type', 'session')
    list_display_links = ('title',)
    search_fields = ('title',)
    
@admin.register(Card)
class CardFilter(admin.ModelAdmin):
    list_display = ('id', 'slug', 'game', 'card_family')
    # list_filter = ('slug', 'card_type', 'session')
    list_display_links = ('slug',)
    search_fields = ('slug',)