# Generated by Django 2.0.2 on 2018-02-27 20:06

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20180227_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
