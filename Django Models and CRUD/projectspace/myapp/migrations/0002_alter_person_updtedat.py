# Generated by Django 5.1.7 on 2025-03-11 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='updtedat',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
