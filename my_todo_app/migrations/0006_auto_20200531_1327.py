# Generated by Django 2.1 on 2020-05-31 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_todo_app', '0005_auto_20200531_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='firstname',
            new_name='content',
        ),
    ]
