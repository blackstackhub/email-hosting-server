# Generated by Django 4.0.4 on 2024-02-15 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_alter_emailmessage_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailmessage',
            name='sendto',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]
