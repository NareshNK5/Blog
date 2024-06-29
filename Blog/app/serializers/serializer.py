from rest_framework import serializers
from app.models import *

class Tbluserserializer(serializers.ModelSerializer):
    class Meta:
        model = Tbluser
        fields = '__all__'