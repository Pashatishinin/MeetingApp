# Generated by Django 4.1.7 on 2023-06-09 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetme', '0012_remove_meeting_random_code_meeting_number_of_quests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='number_of_quests',
            field=models.IntegerField(default=False, null=True),
        ),
    ]
