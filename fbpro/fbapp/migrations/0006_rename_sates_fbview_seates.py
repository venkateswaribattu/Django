# Generated by Django 4.1.3 on 2022-12-23 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fbapp', '0005_fbview_sates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fbview',
            old_name='Sates',
            new_name='Seates',
        ),
    ]
