# Generated by Django 5.0.4 on 2024-07-17 13:43

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(120)])),
                ('birth_date', models.DateField(default='1900-01-01')),
                ('nationality', models.CharField(default='Unknown', max_length=50, validators=[django.core.validators.MaxLengthValidator(50)])),
                ('is_awarded', models.BooleanField(default=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(120)])),
                ('birth_date', models.DateField(default='1900-01-01')),
                ('nationality', models.CharField(default='Unknown', max_length=50, validators=[django.core.validators.MaxLengthValidator(50)])),
                ('years_of_experience', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(150)])),
                ('release_date', models.DateField()),
                ('storyline', models.TextField(blank=True, null=True)),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Other', 'Other')], default='Other', max_length=6)),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('is_classic', models.BooleanField(default=False)),
                ('is_awarded', models.BooleanField(default=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.director')),
                ('starring_actor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.actor')),
            ],
        ),
    ]