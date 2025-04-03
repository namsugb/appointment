from rest_framework import serializers

from .models import Appointment, Dates_info, Feedback, Selected_date


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class Dates_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dates_info
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'