# Generated by Django 2.2.7 on 2020-09-04 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bids_comments_listings'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='city',
            field=models.CharField(default='1', max_length=64),
        ),
        migrations.AddField(
            model_name='comments',
            name='code',
            field=models.CharField(default='1', max_length=3),
        ),
    ]