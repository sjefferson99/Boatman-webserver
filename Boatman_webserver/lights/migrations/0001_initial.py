# Generated by Django 4.0.2 on 2022-02-19 12:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='light',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(15)])),
                ('state', models.BooleanField(verbose_name=False)),
                ('duty', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255)])),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(15)])),
                ('name', models.CharField(max_length=16)),
                ('state', models.BooleanField(verbose_name=False)),
                ('duty', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255)])),
                ('lights', models.ManyToManyField(to='lights.light')),
            ],
        ),
    ]
