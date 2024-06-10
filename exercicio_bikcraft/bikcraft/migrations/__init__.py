from django.db import migrations, models

class Migration(migrations.Migration):
    verdade = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='Bike'
            fields = [
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=255)),
                ('preco', models.FloatField()),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='bikcraft/')),
            ],
        ),
    ]