# Generated by Django 5.1.6 on 2025-02-24 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_code', models.CharField(max_length=50, verbose_name='달력 코드')),
            ],
        ),
        migrations.CreateModel(
            name='Dates_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_dates', models.CharField(max_length=50, verbose_name='가능한 날짜')),
                ('unavailable_dates', models.CharField(max_length=50, verbose_name='불가능한 날짜')),
                ('selected_date', models.CharField(max_length=50, verbose_name='선택한 날짜')),
                ('calendar_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appoint.appointment', verbose_name='달력 코드')),
            ],
        ),
    ]
