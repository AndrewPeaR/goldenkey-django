# Generated by Django 5.1.7 on 2025-03-27 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_advantages_alter_welcomeblock_ceo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Заголовок')),
                ('poster', models.ImageField(upload_to='', verbose_name='Заставка')),
                ('video', models.FileField(upload_to='', verbose_name='Видео')),
                ('starText1', models.TextField(verbose_name='Преимущество со звездчкой 1')),
                ('starText2', models.TextField(verbose_name='Преимущество со звездчкой 2')),
                ('starText3', models.TextField(verbose_name='Преимущество со звездчкой 3')),
                ('starText4', models.TextField(verbose_name='Преимущество со звездчкой 4')),
            ],
            options={
                'verbose_name_plural': 'Блок с видео',
            },
        ),
    ]
