# Generated by Django 2.2.6 on 2020-05-10 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_auto_20200510_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='productname',
            new_name='equipmentname',
        ),
    ]
