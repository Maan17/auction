# Generated by Django 3.0.7 on 2020-09-24 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='winner',
            field=models.CharField(blank=True, default='', max_length=64, null=True),
        ),
    ]