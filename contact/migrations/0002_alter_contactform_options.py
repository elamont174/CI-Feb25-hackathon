# Generated by Django 4.2 on 2025-02-14 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactform',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
    ]
