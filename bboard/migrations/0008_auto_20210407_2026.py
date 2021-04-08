# Generated by Django 3.1.4 on 2021-04-07 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0007_auto_20210407_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='author',
            field=models.ForeignKey(auto_created=True, blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='Автор'),
        ),
    ]
