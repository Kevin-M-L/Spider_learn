# Generated by Django 3.2.8 on 2021-10-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_auto_20211028_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='hassub',
            field=models.BooleanField(db_index=True, default=True, verbose_name='是否有子菜单'),
        ),
    ]
