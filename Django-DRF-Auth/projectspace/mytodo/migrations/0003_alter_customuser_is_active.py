# Generated by Django 5.2 on 2025-04-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0002_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
