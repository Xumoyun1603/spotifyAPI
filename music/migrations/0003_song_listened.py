# Generated by Django 3.1.14 on 2022-03-28 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20220328_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='listened',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
