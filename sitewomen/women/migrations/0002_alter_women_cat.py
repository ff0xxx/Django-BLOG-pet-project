# Generated by Django 5.0.6 on 2024-07-08 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='cat',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='women.category', verbose_name='Категории'),
        ),
    ]
