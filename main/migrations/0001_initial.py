# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-16 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('faculty_id', models.IntegerField(primary_key=True, serialize=False)),
                ('faculty_name', models.CharField(default='XYZ', max_length=140)),
                ('faculty_total_rating', models.IntegerField()),
                ('faculty_total_raters', models.IntegerField()),
                ('faculty_contact', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('institution_id', models.IntegerField(primary_key=True, serialize=False)),
                ('institution_name', models.CharField(default='ABCD', max_length=140)),
                ('institution_type', models.IntegerField(choices=[(1, 'High School'), (2, 'Senior Secondary School'), (3, 'College')])),
                ('institution_address', models.CharField(default='ALPHA', max_length=150)),
                ('institution_total_rating', models.IntegerField()),
                ('institution_total_raters', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(default='XYZ', max_length=140)),
                ('student_total_rating', models.IntegerField()),
                ('student_total_raters', models.IntegerField()),
                ('student_contact', models.BigIntegerField()),
                ('student_institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Institution')),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='faculty_institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Institution'),
        ),
    ]
