# Generated by Django 5.0.4 on 2024-06-19 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('employee_count', models.PositiveIntegerField(default=1, verbose_name='Employees Count')),
                ('location', models.CharField(blank=True, choices=[('Sofia', 'Sofia'), ('Plovdiv', 'Plovdiv'), ('Burgas', 'Burgas'), ('Varna', 'Varna')], max_length=20, null=True)),
                ('last_edited_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
