# Generated by Django 4.0.6 on 2022-09-08 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0003_alter_archive_hashtag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archive',
            name='image',
        ),
        migrations.AlterField(
            model_name='archiveanswer',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]