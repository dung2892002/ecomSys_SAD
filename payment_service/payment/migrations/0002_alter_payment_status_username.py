# Generated by Django 4.1.13 on 2024-05-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_status',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
