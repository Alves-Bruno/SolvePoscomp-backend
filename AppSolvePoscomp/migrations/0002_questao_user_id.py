# Generated by Django 3.1.3 on 2020-11-15 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppSolvePoscomp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questao',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
            preserve_default=False,
        ),
    ]
