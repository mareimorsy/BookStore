# Generated by Django 2.0.2 on 2018-02-27 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='country',
            new_name='author_country',
        ),
    ]