# Generated by Django 4.1.3 on 2023-01-02 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_feedbackdata_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackdata',
            name='user_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
