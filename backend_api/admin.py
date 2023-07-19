from django.contrib import admin
from .models import Address,Customer,Opportunity,Role

# Register your models here.

admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Opportunity)
admin.site.register(Role)


