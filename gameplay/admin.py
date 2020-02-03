from django.contrib import admin
from .models import Move, Game
# Register your models here.

# admin.site.register(Game)
admin.site.register(Move)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_player', 'second_player', 'status')
    list_editable = ('first_player', 'second_player', 'status')