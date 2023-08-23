# Generated by Django 3.2.20 on 2023-08-23 22:07

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('total_time', models.PositiveIntegerField()),
                ('serves', models.PositiveIntegerField()),
                ('recipe_placeholder', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('published_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('featured_image', cloudinary.models.CloudinaryField(default='landing_page_placeholder', max_length=255, verbose_name='image')),
                ('featured_description', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('calories', models.PositiveIntegerField()),
                ('is_approved', models.BooleanField(default=False)),
                ('liked_by', models.ManyToManyField(blank=True, related_name='liked_recipes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-published_on'],
            },
        ),
    ]
