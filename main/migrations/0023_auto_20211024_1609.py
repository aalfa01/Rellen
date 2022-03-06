# Generated by Django 3.2.8 on 2021-10-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_properties_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Posts')),
            ],
        ),
        migrations.RenameField(
            model_name='properties',
            old_name='content',
            new_name='content_ru',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image4',
        ),
        migrations.AddField(
            model_name='properties',
            name='content_uz',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ManyToManyField(to='main.Image'),
        ),
    ]