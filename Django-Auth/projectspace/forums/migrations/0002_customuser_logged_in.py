# Generated by Django 5.1.7 on 2025-03-20 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='logged_in',
            field=models.BooleanField(default=False),
        ),
    ]
