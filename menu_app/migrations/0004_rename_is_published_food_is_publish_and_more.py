# Generated by Django 4.0.8 on 2023-01-11 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0003_rename_category_id_food_category_alter_food_toppings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='is_published',
            new_name='is_publish',
        ),
        migrations.RenameField(
            model_name='foodcategory',
            old_name='is_published',
            new_name='is_publish',
        ),
    ]
