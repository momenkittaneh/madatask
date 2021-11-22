# Generated by Django 3.2.9 on 2021-11-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_remove_service_common'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='common',
        ),
        migrations.AddField(
            model_name='customers',
            name='service',
            field=models.ManyToManyField(blank=True, related_name='service', to='backend.service'),
        ),
        migrations.AddField(
            model_name='service',
            name='customer',
            field=models.ManyToManyField(blank=True, related_name='customer', to='backend.customers'),
        ),
    ]