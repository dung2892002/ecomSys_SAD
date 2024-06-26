# Generated by Django 4.1.13 on 2024-05-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=10)),
                ('order_id', models.CharField(max_length=10)),
                ('mode_of_payment', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'payments',
            },
        ),
    ]
