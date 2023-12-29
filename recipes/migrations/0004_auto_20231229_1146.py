# Generated by Django 3.2.3 on 2023-12-29 11:46

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0003_auto_20230824_0903'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-updated_at']},
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='total_time',
            new_name='cooking_time',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='published_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='serves',
            new_name='servings',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='updated_on',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='like',
            name='recipe_liked',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='liked_by',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='slug',
        ),
        migrations.AddField(
            model_name='like',
            name='recipe',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='id',
            field=models.BigAutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='recipe_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='is_approved',
            field=models.BooleanField(choices=[(False, 'Pending Approval'), (True, 'Approved')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_placeholder',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL),
        ),
    ]
