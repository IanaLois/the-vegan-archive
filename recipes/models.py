from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

RECIPE_STATUS = ((0, "Draft"), (1, "Published"))

APPROVAL_STATUS = ((False, "Pending Approval"), (True, "Approved"))


class Recipe(models.Model):
    recipe = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=False)
    image = CloudinaryField('image', 'recipe_placeholder', blank=False)
    description = models.TextField(blank=False)
    serves = models.PositiveIntegerField(blank=False)
    calories = models.PositiveIntegerField(blank=False)
    total_time = models.PositiveIntegerField(blank=False)
    ingredients = models.TextField(blank=False)
    instructions = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField(
        User, blank=True, related_name='liked_recipes')
    status = models.IntegerField(choices=RECIPE_STATUS, default=0)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.liked_by.count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_liked = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    liked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.recipe_liked.title}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
