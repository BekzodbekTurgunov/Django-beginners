# Generated by Django 3.1.6 on 2021-02-13 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20210213_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(),
        ),
    ]
