# Generated by Django 3.1.7 on 2021-05-15 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0015_auto_20210515_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='phone',
            field=models.CharField(default='+79999999999', max_length=20, verbose_name='Мобильный телефон'),
        ),
    ]
