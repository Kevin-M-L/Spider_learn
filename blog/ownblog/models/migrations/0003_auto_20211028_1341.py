# Generated by Django 3.2.8 on 2021-10-28 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_submenu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submenu',
            old_name='display',
            new_name='subdisplay',
        ),
        migrations.RenameField(
            model_name='submenu',
            old_name='href',
            new_name='subhref',
        ),
        migrations.RenameField(
            model_name='submenu',
            old_name='name',
            new_name='subname',
        ),
        migrations.RenameField(
            model_name='submenu',
            old_name='sort',
            new_name='subsort',
        ),
    ]