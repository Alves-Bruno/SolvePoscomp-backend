# Generated by Django 3.1.3 on 2020-11-22 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSolvePoscomp', '0005_auto_20201120_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='nome',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
