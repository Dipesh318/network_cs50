# Generated by Django 2.1.7 on 2020-07-12 13:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_auto_20200712_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user_id',
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='like',
        ),
    ]
