# Generated by Django 2.2.3 on 2020-03-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate_my_agency', '0005_auto_20200330_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
