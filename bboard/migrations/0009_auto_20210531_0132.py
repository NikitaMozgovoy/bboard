# Generated by Django 3.1.7 on 2021-05-30 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0008_auto_20210531_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateField(default='2021-01-01', verbose_name='Дата регистрации'),
        ),
    ]
