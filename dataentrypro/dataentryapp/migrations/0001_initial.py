# Generated by Django 4.1.3 on 2022-12-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('course', models.CharField(max_length=100)),
                ('fee', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('institute', models.CharField(max_length=100)),
            ],
        ),
    ]