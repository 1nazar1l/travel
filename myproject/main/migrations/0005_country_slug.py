# Generated by Django 5.1 on 2024-08-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_country_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='slug',
            field=models.CharField(default=None, max_length=60),
        ),
    ]
