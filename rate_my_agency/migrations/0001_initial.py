# Generated by Django 2.2.3 on 2020-04-03 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencyName', models.CharField(max_length=30)),
                ('website', models.URLField(null=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Agencies',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField()),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rate_my_agency.Agency')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rate_my_agency.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='agency_images/')),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rate_my_agency.Agency')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentText', models.CharField(max_length=300)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rate_my_agency.Agency')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rate_my_agency.Tenant')),
            ],
        ),
        migrations.AddField(
            model_name='agency',
            name='cities',
            field=models.ManyToManyField(to='rate_my_agency.City'),
        ),
        migrations.AddField(
            model_name='agency',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
