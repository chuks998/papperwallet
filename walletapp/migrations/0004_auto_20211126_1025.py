# Generated by Django 3.1.5 on 2021-11-26 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('walletapp', '0003_auto_20211126_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='sending_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='walletapp.accountdetail'),
        ),
    ]
