# Generated by Django 5.0.1 on 2024-02-02 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='second_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('institute', models.CharField(max_length=50)),
                ('start_year', models.PositiveIntegerField()),
            ],
        ),
    ]
