# Generated by Django 5.0.3 on 2024-03-17 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='fullname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='school',
        ),
    ]
