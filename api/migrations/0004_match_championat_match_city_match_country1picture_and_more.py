# Generated by Django 5.0.2 on 2024-02-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_guider'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='Championat',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='City',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='Country1Picture',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='Country2Picture',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='StadiumName',
            field=models.CharField(default='none', max_length=100),
        ),
    ]