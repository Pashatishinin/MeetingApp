# Generated by Django 4.1.7 on 2023-05-03 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetme', '0002_alter_meeting_end_date_alter_meeting_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
