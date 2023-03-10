# Generated by Django 4.1.7 on 2023-03-03 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='news',
            name='detail',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
    ]
