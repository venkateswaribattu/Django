# Generated by Django 4.1.3 on 2022-12-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbapp', '0002_remove_fbview_sates'),
    ]

    operations = [
        migrations.AddField(
            model_name='fbview',
            name='Sates',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
