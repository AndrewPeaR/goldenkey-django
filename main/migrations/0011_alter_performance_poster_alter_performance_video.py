# Generated by Django 5.1.7 on 2025-03-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_performance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='poster',
            field=models.ImageField(upload_to='performance', verbose_name='Заставка'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='video',
            field=models.FileField(upload_to='performance', verbose_name='Видео'),
        ),
    ]
