# Generated by Django 3.2.6 on 2021-10-19 03:25

import classroom.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('bookings', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.bookings')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm_name', models.CharField(blank=True, max_length=100)),
                ('body', models.TextField(max_length=500)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='WorkingDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_days', to='classroom.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_time_slots', to='classroom.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to=classroom.models.save_subject_image, verbose_name='Subject Image')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='classroom.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='SlotSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_slots', to='classroom.classroom')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_slots_days', to='classroom.workingdays')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_slots_time', to='classroom.timeslots')),
                ('slot_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_slots_subject', to='classroom.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_body', models.TextField(max_length=500)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='classroom.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_id', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
                ('position', models.PositiveSmallIntegerField(verbose_name='Chapter no.')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to=classroom.models.save_lesson_files, verbose_name='Video')),
                ('ppt', models.FileField(blank=True, upload_to=classroom.models.save_lesson_files, verbose_name='Presentations')),
                ('Notes', models.FileField(blank=True, upload_to=classroom.models.save_lesson_files, verbose_name='Notes')),
                ('Classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.classroom')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='classroom.subject')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='lesson_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='classroom.lesson'),
        ),
    ]