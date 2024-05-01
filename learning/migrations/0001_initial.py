# Generated by Django 5.0.3 on 2024-04-24 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(default=0)),
                ('number', models.IntegerField()),
                ('vietnam_name', models.CharField(max_length=50)),
                ('japan_name', models.CharField(max_length=50)),
                ('note1', models.CharField(max_length=50, null=True)),
                ('note2', models.CharField(max_length=50, null=True)),
                ('section', models.PositiveIntegerField()),
                ('section_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LessonImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='lesson_pictures')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.lesson')),
            ],
        ),
    ]