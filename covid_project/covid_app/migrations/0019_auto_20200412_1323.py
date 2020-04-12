# Generated by Django 3.0.3 on 2020-04-12 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0018_auto_20200412_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myreply',
            name='setfeedback',
        ),
        migrations.AddField(
            model_name='feedback_enquiry',
            name='my_reply',
            field=models.ForeignKey(blank=True, max_length=2000, null=True, on_delete=django.db.models.deletion.CASCADE, to='covid_app.MyReply'),
        ),
    ]
