# Generated by Django 4.0.5 on 2022-06-26 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0049_alter_schedule_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.worker', verbose_name='Worker'),
        ),
    ]
