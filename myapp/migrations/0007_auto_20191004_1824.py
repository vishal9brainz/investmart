# Generated by Django 2.2.5 on 2019-10-04 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20190925_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='myapp',
            name='placetitle',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='myapp',
            name='placevalue',
            field=models.CharField(default=' ', max_length=1000),
        ),
    ]
