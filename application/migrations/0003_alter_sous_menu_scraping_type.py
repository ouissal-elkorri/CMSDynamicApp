# Generated by Django 3.2.5 on 2021-08-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20210802_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sous_menu',
            name='scraping_type',
            field=models.CharField(choices=[('youtube', 'youtube'), ('youtube_playlist', 'youtube_playlist'), ('facebook', 'facebook'), ('instagram', 'instagram')], default='youtube', max_length=20),
        ),
    ]