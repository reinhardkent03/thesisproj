# Generated by Django 3.2.6 on 2021-10-25 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_tutorprofile_book_counter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorprofile',
            name='book_counter',
        ),
    ]
