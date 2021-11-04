# Generated by Django 3.2.6 on 2021-10-23 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_bookings_on_session'),
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='bookings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.bookings'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='Classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.classroom'),
        ),
        migrations.AlterField(
            model_name='slotsubject',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classroom_slots', to='classroom.classroom'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='classroom.classroom'),
        ),
        migrations.AlterField(
            model_name='timeslots',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classroom_time_slots', to='classroom.classroom'),
        ),
        migrations.AlterField(
            model_name='workingdays',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classroom_days', to='classroom.classroom'),
        ),
    ]
