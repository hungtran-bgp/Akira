# Generated by Django 5.0.3 on 2024-04-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crossword', '0004_crossmapresult_wordresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordresult',
            name='row',
            field=models.IntegerField(default=1),
        ),
    ]