from rest_framework import serializers
from .models import Address, Customer, Opportunity, Role

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("__all__")

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ("__all__")

class OpportunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Opportunity
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'

class AddressDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('country', 'city', 'street', 'zipCode')


class OpportunityDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ('id', 'name', 'date', 'link', 'description', 'salesfunnel', 'customerRepresentative',"phases_json")


class CustomerDetailsSerializer(serializers.ModelSerializer):
    opportunities = OpportunityDetailsSerializer(many=True)
    address = AddressDetailsSerializer()
    class Meta:
        model = Customer
        fields = ('id', 'name', 'customerContactPerson', 'number', 'email','address', 'opportunities')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        opportunity_data = validated_data.pop('opportunities')
       
        customer = Customer.objects.create(**validated_data)
        address_data['customer'] = customer
        address = Address.objects.create(**address_data)
        for opp_data in opportunity_data:
            Opportunity.objects.create(Customer_id = customer, **opp_data)

        return customer
