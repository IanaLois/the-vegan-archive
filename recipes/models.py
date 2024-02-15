from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

RECIPE_STATUS = ((0, "Draft"), (1, "Published"))

APPROVAL_STATUS = ((False, "Pending Approval"), (True, "Approved"))


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe')
    title = models.CharField(max_length=200, unique=True, blank=False)
    image = CloudinaryField('image', null=True)
    description = models.TextField(blank=False)
    servings = models.PositiveIntegerField(blank=False)
    calories = models.PositiveIntegerField(blank=False)
    cooking_time = models.PositiveIntegerField(blank=False)
    ingredients = models.TextField(blank=False)
    instructions = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=RECIPE_STATUS, default=0)
    is_approved = models.BooleanField(choices=APPROVAL_STATUS, default=False, null=True)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} liked {self.recipe.title}"


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, blank=False)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s profile"
