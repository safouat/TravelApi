# Generated by Django 5.0.2 on 2024-02-28 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_match_championat_match_city_match_country1picture_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='Country1',
            new_name='country1',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='Country2',
            new_name='country2',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='Championat',
            new_name='flag1',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='Country1Picture',
            new_name='flag2',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='Country2Picture',
            new_name='stadium',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='StadiumName',
            new_name='title',
        ),
    ]
