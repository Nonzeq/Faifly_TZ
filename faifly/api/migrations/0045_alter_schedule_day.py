# Generated by Django 4.0.5 on 2022-06-26 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_remove_worker_time_schedule_day_schedule_person_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Thusday', 'Thusday'), ('Wendsday', 'Wendsday'), ('Thersday', 'Thersday'), ('Friday', 'Friday'), ('Seterday', 'Seterday')], default=None, max_length=8, null=True),
        ),
    ]
