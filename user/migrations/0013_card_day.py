# Generated by Django 5.0.8 on 2024-10-09 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_food_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='day',
            field=models.CharField(default='sat', max_length=10),
        ),
    ]
