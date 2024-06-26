# Generated by Django 5.0.6 on 2024-06-26 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikcraft', '0006_alter_detalhebikes_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='media/bikcraft/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='detalhebikes',
            name='opcao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bikcraft.bike', verbose_name='Bikes'),
        ),
        migrations.AlterField(
            model_name='pessoas',
            name='opcao_lojas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikcraft.lojas', verbose_name='Lojas'),
        ),
    ]
