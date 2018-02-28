# Generated by Django 2.0.2 on 2018-02-27 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('pic', models.ImageField(upload_to='static/images')),
                ('DOB', models.DateTimeField()),
                ('DOD', models.DateTimeField(blank=True, null=True)),
                ('country', models.CharField(max_length=200)),
                ('follow', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('pic', models.ImageField(upload_to='static/images')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pic', models.ImageField(upload_to='static/images')),
                ('like', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='cat_books',
            field=models.ManyToManyField(to='store.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='read',
            field=models.ManyToManyField(blank=True, related_name='read', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='wish',
            field=models.ManyToManyField(blank=True, related_name='wish', to=settings.AUTH_USER_MODEL),
        ),
    ]