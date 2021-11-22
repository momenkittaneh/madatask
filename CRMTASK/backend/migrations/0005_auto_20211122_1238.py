# Generated by Django 3.2.9 on 2021-11-22 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_remove_customers_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='customer',
        ),
        migrations.AddField(
            model_name='customers',
            name='customer',
            field=models.ManyToManyField(blank=True, related_name='customers', to='backend.service'),
        ),
    ]