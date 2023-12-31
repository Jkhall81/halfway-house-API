# Generated by Django 4.2.5 on 2023-09-24 16:30

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('total_number_of_beds', models.IntegerField()),
                ('number_of_beds_open', models.IntegerField()),
                ('parking_capacity', models.IntegerField()),
                ('house_manager', models.CharField(max_length=100)),
                ('house_manager_phone_number', models.CharField(max_length=12, validators=[app.models.validate_phone_number_format])),
                ('cost_of_rent', models.IntegerField()),
                ('rent_interval', models.CharField(max_length=100)),
                ('sober_living_house', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=12, validators=[app.models.validate_phone_number_format])),
                ('is_employed', models.BooleanField()),
                ('felony_record', models.BooleanField()),
                ('taking_psych_meds', models.BooleanField()),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residents', to='app.house')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
