# Generated by Django 4.0.6 on 2022-08-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0002_alter_archive_image_alter_archiveanswer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='hashtag',
            field=models.TextField(null=True, verbose_name='해시태그'),
        ),
    ]