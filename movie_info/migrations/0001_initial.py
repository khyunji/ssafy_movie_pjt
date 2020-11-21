# Generated by Django 3.1.3 on 2020-11-21 05:34

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
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.FloatField()),
                ('vote_average', models.FloatField()),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('original_language', models.TextField()),
                ('original_title', models.TextField()),
                ('adult', models.TextField()),
                ('overview', models.TextField()),
                ('poster_path', models.TextField()),
                ('genre_ids', models.ManyToManyField(to='movie_info.Genre')),
            ],
        ),
    ]
