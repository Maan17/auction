# Generated by Django 3.0.7 on 2020-09-07 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200905_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(default='none', max_length=50),
        ),
    ]