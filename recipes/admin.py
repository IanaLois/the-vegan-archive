from django.contrib import admin
from .models import Recipe, Profile, Like
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):    
    list_display = ('title', 'status', 'created_at', 'updated_at', 'is_approved')
    search_fields = ['title', 'description']
    list_filter = ('status', 'is_approved')
    summernote_fields = ('description', 'ingredients', 'instructions')
    actions = ['approve_recipes']

    def approve_recipes(self, request, queryset):
        queryset.update(is_approved=True)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'bio', 'created_at', 'last_login', 'is_active', 'is_admin')
    list_filter = ('is_active', 'is_admin')
    search_fields = ['user__username', 'full_name']
    readonly_fields = ('created_at', 'last_login')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'created_at')
    list_filter = ('created_at',)
    search_fields = ['user__username', 'recipe__title']
    readonly_fields = ('created_at',)

