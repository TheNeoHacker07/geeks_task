# Generated by Django 5.0.6 on 2024-06-15 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_rename_postmodel_todomodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoModel',
            new_name='Task',
        ),
    ]
