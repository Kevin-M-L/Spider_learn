# Generated by Django 3.2.8 on 2021-10-29 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, db_index=True, null=True, upload_to='upload/static/images/', verbose_name='封面'),
        ),
    ]
