# Generated by Django 3.2.7 on 2021-10-14 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_image2_post_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='relen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Relen')),
                ('header', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='header',
        ),
        migrations.RemoveField(
            model_name='post',
            name='images',
        ),
    ]