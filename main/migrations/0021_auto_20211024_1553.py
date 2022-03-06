# Generated by Django 3.2.8 on 2021-10-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_category_relen_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='relen_product',
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('relen_product', models.ManyToManyField(to='main.relen')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='properties',
            field=models.ManyToManyField(to='main.Properties'),
        ),
    ]