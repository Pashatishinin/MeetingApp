# Generated by Django 4.1.7 on 2023-05-16 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetme', '0010_alter_newusers_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewUsers',
        ),
    ]