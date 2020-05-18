# Generated by Django 3.0.5 on 2020-05-18 20:29

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataExtraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Extraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lawsuits', models.FileField(blank=True, upload_to='')),
                ('customer', models.CharField(default=None, max_length=100)),
                ('result', models.FileField(blank=True, null=True, upload_to='')),
                ('total_lawsuits', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('found', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('status', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
    ]
