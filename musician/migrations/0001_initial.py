# Generated by Django 5.0.6 on 2024-05-30 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicianModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_no', models.CharField(max_length=20)),
                ('instrument_type', models.CharField(max_length=200)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.albummodel')),
            ],
        ),
    ]