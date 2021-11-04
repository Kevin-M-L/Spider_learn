# Generated by Django 3.2.8 on 2021-11-01 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='bannericon',
            field=models.ImageField(blank=True, db_index=True, null=True, upload_to='static/images/icon', verbose_name='轮播图标'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, db_index=True, null=True, upload_to='static/images/', verbose_name='封面'),
        ),
    ]
