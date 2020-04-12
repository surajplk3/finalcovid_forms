# Generated by Django 3.0.3 on 2020-04-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0006_data_base'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data_base',
            old_name='data',
            new_name='age_group_data',
        ),
        migrations.AddField(
            model_name='data_base',
            name='individual_data',
            field=models.FileField(blank=True, upload_to='File'),
        ),
        migrations.AddField(
            model_name='data_base',
            name='statewise_test_details',
            field=models.FileField(blank=True, upload_to='File'),
        ),
    ]
