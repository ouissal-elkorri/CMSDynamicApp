# Generated by Django 3.2.5 on 2021-08-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_sous_menu_scraping_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='intitule',
            field=models.CharField(max_length=500),
        ),
    ]