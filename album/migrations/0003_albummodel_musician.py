# Generated by Django 5.0.6 on 2024-05-30 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_alter_albummodel_release_date'),
        ('musician', '0002_remove_musicianmodel_album_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='albummodel',
            name='musician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musician.musicianmodel'),
        ),
    ]
