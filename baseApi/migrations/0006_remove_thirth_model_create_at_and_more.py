# Generated by Django 5.0.1 on 2024-02-02 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApi', '0005_alter_thirth_model_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thirth_model',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='thirth_model',
            name='user',
        ),
    ]
