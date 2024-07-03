# Generated by Django 5.0.4 on 2024-07-03 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_lecturerprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine', models.CharField(max_length=50)),
                ('brand', models.CharField(choices=[('BMW', 'BMW'), ('Mercedes', 'Mercedes'), ('Skoda', 'Skoda'), ('Mazda', 'Mazda'), ('Audi', 'Audi'), ('Seat', 'Seat')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_age', models.PositiveIntegerField()),
                ('car_made_date', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.car')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.employee')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='employee',
            field=models.ManyToManyField(through='main_app.EmployeeCar', to='main_app.employee'),
        ),
    ]