# Generated by Django 5.0.6 on 2024-06-15 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_postmodel_image_remove_postmodel_text_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostModel',
            new_name='TodoModel',
        ),
    ]