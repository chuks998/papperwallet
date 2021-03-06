# Generated by Django 3.1.5 on 2021-11-26 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import walletapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciver_name', models.CharField(max_length=100)),
                ('reciver_account', models.CharField(max_length=12)),
                ('amount', models.FloatField(default=0.0)),
                ('sending_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(blank=True, default=walletapp.models.account_genarator, max_length=11, null=True, unique=True)),
                ('account_balance', models.FloatField(default=0.0)),
                ('account_holder', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
