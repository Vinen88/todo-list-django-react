# Generated by Django 4.1.7 on 2023-03-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]