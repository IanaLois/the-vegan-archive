from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe, Like
from django.views.generic import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from recipes.mixins.is_owner import UserIsObjectOwnerMixin

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-created_at")
    template_name = 'index.html'
    paginate_by = 3

class RecipeDirectoryView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1, is_approved=True).order_by("-created_at")
    template_name = 'recipe_directory.html'
    paginate_by = 3

class RecipeDetail(View):

    def get(self, request, id, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=id)
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "liked": liked
            },
        )

class RecipeLike(View):
    def post(self, request, id, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=id)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        return HttpResponseRedirect(reverse('recipe_detail', args=[id]))

class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['field1', 'field2']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin, UserIsObjectOwnerMixin, UpdateView):
    model = Recipe
    fields = ['field1', 'field2']

class RecipeDelete(LoginRequiredMixin, UserIsObjectOwnerMixin, DeleteView):
    model = Recipe