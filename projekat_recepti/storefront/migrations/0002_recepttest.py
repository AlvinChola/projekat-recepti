# Generated by Django 4.0.3 on 2022-03-21 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceptTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slika_jela', models.ImageField(upload_to='slike')),
                ('naziv_jela', models.CharField(max_length=30)),
                ('kuhar', models.CharField(max_length=15)),
                ('ocjena', models.IntegerField()),
            ],
        ),
    ]
