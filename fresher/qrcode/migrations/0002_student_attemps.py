# Generated by Django 4.1.4 on 2023-08-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='attemps',
            field=models.IntegerField(default=0),
        ),
    ]