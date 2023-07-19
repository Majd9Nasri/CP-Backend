# Generated by Django 4.1.7 on 2023-06-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0007_remove_roleassignment_phase_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Costumer',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='costumer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='opportunity',
            old_name='Costumer_id',
            new_name='Customer_id',
        ),
        migrations.AlterField(
            model_name='role',
            name='role_type',
            field=models.CharField(choices=[('Software Engineer Senior', 'SoftwareEngineerSenior'), ('Software Engineer Regular', 'SoftwareEngineerRegular'), ('Requirements Engineer', 'RequirementsEngineer'), ('Software Reliability Engineer', 'SoftwareReliabilityEngineer'), ('Quality Engineer', 'QualityEngineer'), ('UI_UX Designer', 'UI/UXDesigner'), ('Technical Architect', 'TechnicalArchitect'), ('Project Manager', 'ProjectManager'), ('Technical Consultant', 'TechnicalConsultant'), ('Agile Coach', 'Agile Coach'), ('Data Scientist', 'DataScientist')], default=0, max_length=100),
        ),
    ]
