# Generated by Django 3.1.5 on 2021-11-26 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('walletapp', '0004_auto_20211126_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='sending_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
