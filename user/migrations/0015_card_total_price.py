# Generated by Django 5.0.8 on 2024-10-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_card_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
