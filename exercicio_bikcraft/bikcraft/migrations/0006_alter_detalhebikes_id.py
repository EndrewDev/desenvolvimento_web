# Generated by Django 5.0.6 on 2024-06-22 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikcraft', '0005_detalhebikes_id_pessoas_id_alter_detalhebikes_opcao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalhebikes',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
