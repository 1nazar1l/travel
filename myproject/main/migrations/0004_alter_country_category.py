# Generated by Django 5.1 on 2024-08-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_another_remove_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='category',
            field=models.ManyToManyField(to='main.another'),
        ),
    ]
