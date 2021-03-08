# Generated by Django 3.1.4 on 2021-02-18 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='author',
            field=models.TextField(blank=True, null=True, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Онлайн'),
        ),
    ]
