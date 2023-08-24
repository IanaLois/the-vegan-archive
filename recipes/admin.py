from django.contrib import admin
from .models import Recipe, Like, Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'status', 'published_on', 'updated_on', 'is_approved')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'published_on', 'is_approved')
    summernote_fields = ('description', 'ingredients', 'instructions',)
    actions = ['approve_recipes']

    def approve_recipes(self, request, queryset):
        queryset.update(is_approved=True)