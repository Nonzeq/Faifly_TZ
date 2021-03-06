# Generated by Django 4.0.5 on 2022-06-26 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField(verbose_name='start')),
                ('time_end', models.DateTimeField(verbose_name='end')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.location', verbose_name='location')),
            ],
        ),
        migrations.DeleteModel(
            name='Apoitment',
        ),
        migrations.AddField(
            model_name='worker',
            name='time_of_work',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.schedule', verbose_name='time of work'),
        ),
        migrations.AddField(
            model_name='apointment',
            name='worker',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='api.worker', verbose_name='Worker'),
        ),
    ]
