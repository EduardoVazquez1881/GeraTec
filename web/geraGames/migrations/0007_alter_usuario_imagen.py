# Generated by Django 5.1.4 on 2024-12-11 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geraGames', '0006_usuario_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, default='usr/default.jpg', null=True, upload_to='usr/'),
        ),
    ]