# Generated by Django 4.1.7 on 2023-06-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0008_rename_costumer_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_type',
            field=models.CharField(choices=[('Software Engineer Senior', 'SoftwareEngineerSenior'), ('Software Engineer Regular', 'SoftwareEngineerRegular'), ('Requirements Engineer', 'Requirements Engineer'), ('Software Reliability Engineer', 'SoftwareReliabilityEngineer'), ('Quality Engineer', 'QualityEngineer'), ('UI_UX Designer', 'UI/UXDesigner'), ('Technical Architect', 'TechnicalArchitect'), ('Project Manager', 'ProjectManager'), ('Technical Consultant', 'TechnicalConsultant'), ('Agile Coach', 'Agile Coach'), ('Data Scientist', 'DataScientist')], default=0, max_length=100),
        ),
    ]
