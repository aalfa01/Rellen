# Generated by Django 3.2.8 on 2021-10-24 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20211024_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='products',
            field=models.ManyToManyField(to='main.Post'),
        ),
    ]
