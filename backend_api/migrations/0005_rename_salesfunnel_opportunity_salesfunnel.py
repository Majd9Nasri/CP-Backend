# Generated by Django 4.1.7 on 2023-04-26 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0004_alter_opportunity_id_alter_phase_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opportunity',
            old_name='Salesfunnel',
            new_name='salesfunnel',
        ),
    ]
