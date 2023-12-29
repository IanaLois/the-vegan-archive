from django.contrib import admin
from .models import Recipe, Like, Profile
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):    
    list_display = ('title', 'status', 'created_at', 'updated_at', 'is_approved')
    search_fields = ['title', 'description']
    list_filter = ('status', 'is_approved')
    summernote_fields = ('description', 'ingredients', 'instructions',)
    actions = ['approve_recipes']

    def approve_recipes(self, request, queryset):
        queryset.update(is_approved=True)