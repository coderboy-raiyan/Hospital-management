# Generated by Django 4.2.7 on 2024-01-08 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='available_time',
        ),
        migrations.AddField(
            model_name='doctor',
            name='available_time',
            field=models.ManyToManyField(to='doctor.availabletime'),
        ),
    ]
