# Generated by Django 3.0.6 on 2020-08-04 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Melon_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('artist_name', models.CharField(max_length=100)),
                ('rank', models.IntegerField(default=0)),
                ('img_src', models.TextField(blank=True)),
            ],
        ),
    ]
