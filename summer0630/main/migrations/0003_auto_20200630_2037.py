# Generated by Django 3.0.6 on 2020-06-30 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_goods_sheets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goodsPrice',
            field=models.IntegerField(max_length=30),
        ),
    ]
