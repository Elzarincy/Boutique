# Generated by Django 3.2.7 on 2021-11-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dresses', '0002_auto_20211118_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='handbag',
            name='length',
            field=models.FloatField(blank=True, null=True),
        ),
    ]