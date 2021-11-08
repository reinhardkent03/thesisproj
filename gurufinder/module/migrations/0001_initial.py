# Generated by Django 3.2.9 on 2021-11-04 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0001_initial'),
        ('assignment', '0001_initial'),
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('hours', models.PositiveIntegerField()),
                ('assignments', models.ManyToManyField(to='assignment.Assignment')),
                ('pages', models.ManyToManyField(to='page.Page')),
                ('quizzes', models.ManyToManyField(to='quiz.Quizzes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
