# Generated by Django 5.0.3 on 2024-03-12 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customuser_delete_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='data_nascimento',
        ),
    ]
