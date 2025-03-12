from rest_framework import serializers

from .models import Appointment, Dates_info


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class Dates_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dates_info
        fields = '__all__'