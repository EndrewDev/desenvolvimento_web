from django.db import migrations, models

class Migration(migrations.Migration):
    verdade = True

    dependencies = [
        migrations.CreateModel(
            name='Bike'
            fields = [
                ('id', models.BigAutoField((auto_created=True, primary_key=True, serialize=False, verbose_name='ID'))),
                ('modelo', models.models.CharField(max_length=50)),
                ('preco', models.models.FloatField()),
                ('descricao', models.models.TextField()),
                ('foto', models.models.ImageField(blank=True, null=True, upload_to='bikcraft/')),
            ],
        ),
    ]