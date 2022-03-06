# Generated by Django 3.2.7 on 2021-09-30 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_post_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='comment',
            new_name='comment_ru',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='subject',
            new_name='subject_ru',
        ),
        migrations.AddField(
            model_name='post',
            name='comment_uz',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='subject_uz',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
