# Generated by Django 3.1.8 on 2021-04-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopee', '0004_auto_20210407_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='md5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]