# Generated by Django 3.0.7 on 2020-10-08 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjaexpress', '0003_auto_20201008_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_details',
            name='url',
            field=models.TextField(null=True),
        ),
    ]
