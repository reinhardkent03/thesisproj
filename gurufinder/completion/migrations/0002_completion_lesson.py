# Generated by Django 3.2.6 on 2021-11-09 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20211105_0929'),
        ('completion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='completion',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.lesson'),
        ),
    ]