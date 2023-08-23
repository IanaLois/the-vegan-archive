from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

RECIPE_STATUS = ((0, "Draft"), (1, "Published"))

APPROVAL_STATUS = ((False, "Pending Approval"), (True, "Approved"))


class Recipe(models.Model):
    recipe = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    ingredients = models.TextField(blank=False)
    instructions = models.TextField(blank=False)
    total_time = models.PositiveIntegerField(blank=False)
    serves = models.PositiveIntegerField(blank=False)
    image = CloudinaryField('image', 'recipe_placeholder', blank=False)
    published_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    featured_image = CloudinaryField(
        'image', default='landing_page_placeholder', blank=False)
    featured_description = models.TextField(blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    liked_by = models.ManyToManyField(
        User, blank=True, related_name='liked_recipes')
    calories = models.PositiveIntegerField(blank=False)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
