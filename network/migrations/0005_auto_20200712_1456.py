# Generated by Django 2.1.7 on 2020-07-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20200712_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('user', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
    ]