# Generated by Django 5.1.7 on 2025-03-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_welcomeblock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welcomeblock',
            name='sign',
            field=models.ImageField(upload_to='static/img/sign'),
        ),
    ]
