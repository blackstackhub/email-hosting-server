# Generated by Django 4.0.4 on 2024-02-13 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_alter_emailmessage_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmessage',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.domain'),
        ),
    ]
