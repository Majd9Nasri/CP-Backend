from django.db import models
import datetime
import uuid
import json
# Create your models here.


#####################################################
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True )
    customerContactPerson = models.CharField(max_length=100)
    number  = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name
    
#####################################################
class Address(models.Model):
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=100, null=True)
    zipCode = models.CharField(max_length=100, null=True)
    customer =   models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
        
    #####################################################
class Opportunity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    date = models.DateField(("Date"), default=datetime.date.today)
    link = models.CharField(max_length=200)
    description = models.TextField()
    salesfunnel = models.CharField(max_length=100)
    customerRepresentative = models.CharField(max_length=100)
    Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='opportunities')


    phases_json = models.JSONField(default='[]')

    def phases(self):
        return json.loads(self.phases_json)

    def add_phase(self, name, start, end):
        phases = self.phases()
        phases.append({'name': name, 'start': start,'end': end})
        self.phases_json = json.dumps(phases)
        self.save()
        
    def add_assignment(self, phase_index, Role, hours):
        phases = self.phases()
        if phase_index < 0 or phase_index >= len(phases):
            raise ValueError('Invalid phase index')
        phase = phases[phase_index]
        roleAssignment = phase.get('roleAssignment', [])
        roleAssignment.append({'Role': Role, 'hours': hours})
        phase['roleAssignment'] = roleAssignment
        self.phases_json = json.dumps(phases)
        self.save()    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Opportunities"
        ordering = ["date"]

#######################################################
class Role(models.Model):
    TYPE_CHOICES = (
        ("Software Engineer Senior", "SoftwareEngineerSenior"),
        ("Software Engineer Regular", "SoftwareEngineerRegular"),
        ("Requirements Engineer", "RequirementsEngineer"),
        ("Software Reliability Engineer", "SoftwareReliabilityEngineer"),
        ("Quality Engineer", "QualityEngineer"),
        ("UI_UX Designer", "UI/UXDesigner"),
        ("Technical Architect", "TechnicalArchitect"),
        ("Project Manager", "ProjectManager"),
        ("Technical Consultant", "TechnicalConsultant"),
        ("Agile Coach", "Agile Coach"),
        ("Data Scientist", "DataScientist"),
    )

    role_type = models.CharField(max_length=100,choices=TYPE_CHOICES, default=0)

    
    def __str__(self):
        return self.role_type 
#####################################################  




