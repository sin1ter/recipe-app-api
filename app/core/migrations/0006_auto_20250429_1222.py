# Generated by Django 3.2.25 on 2025-04-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20250429_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='core.Ingredient'),
        ),
    ]
