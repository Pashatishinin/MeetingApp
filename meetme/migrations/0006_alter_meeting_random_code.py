# Generated by Django 4.1.7 on 2023-05-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetme', '0005_alter_meeting_end_date_alter_meeting_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='random_code',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
