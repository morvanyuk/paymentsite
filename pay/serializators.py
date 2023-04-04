from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from pay.models import ContactData, Paidusers

def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')

class ContactSerialization(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ContactData

class PaidusersSerialization(ModelSerializer):
    total_sum = serializers.FloatField(validators=[required])

    class Meta:
        fields = ('user', 'total_sum', 'discord_name')
        model = Paidusers