# Generated by Django 4.1.13 on 2024-05-09 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_model', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]