# Generated by Django 4.1.7 on 2023-05-16 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetme', '0008_alter_meeting_random_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
