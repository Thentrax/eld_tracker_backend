from rest_framework import serializers
from .models import Log, CycleHours

class CycleHoursSerializer(serializers.ModelSerializer):
    start_location = serializers.DictField(child=serializers.FloatField(), write_only=True)
    end_location = serializers.DictField(child=serializers.FloatField(), write_only=True)

    def create(self, validated_data):
        start_location = validated_data.pop('start_location')
        end_location = validated_data.pop('end_location')

        validated_data['start_lat'] = start_location['lat']
        validated_data['start_lng'] = start_location['lng']
        validated_data['end_lat'] = end_location['lat']
        validated_data['end_lng'] = end_location['lng']

        return super().create(validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['start_location'] = {"lat": instance.start_lat, "lng": instance.start_lng}
        data['end_location'] = {"lat": instance.end_lat, "lng": instance.end_lng}
        return data

    class Meta:
        model = CycleHours
        fields = ['id', 'log', 'status_id', 'start_hour', 'end_hour', 'start_location', 'end_location', 'distance', 'annotations']


class LogSerializer(serializers.ModelSerializer):
    current_location = serializers.DictField(child=serializers.FloatField(), write_only=True)
    pickup_location = serializers.DictField(child=serializers.FloatField(), write_only=True)
    dropoff_location = serializers.DictField(child=serializers.FloatField(), write_only=True)

    cycle_hours = CycleHoursSerializer(many=True, read_only=True)

    def create(self, validated_data):
        current_location = validated_data.pop('current_location')
        pickup_location = validated_data.pop('pickup_location')
        dropoff_location = validated_data.pop('dropoff_location')

        validated_data['current_lat'] = current_location['lat']
        validated_data['current_lng'] = current_location['lng']
        validated_data['pickup_lat'] = pickup_location['lat']
        validated_data['pickup_lng'] = pickup_location['lng']
        validated_data['dropoff_lat'] = dropoff_location['lat']
        validated_data['dropoff_lng'] = dropoff_location['lng']

        return super().create(validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['current_location'] = {"lat": instance.current_lat, "lng": instance.current_lng}
        data['pickup_location'] = {"lat": instance.pickup_lat, "lng": instance.pickup_lng}
        data['dropoff_location'] = {"lat": instance.dropoff_lat, "lng": instance.dropoff_lng}
        return data

    class Meta:
        model = Log
        fields = ['id', 'date', 'driver_name', 'truck_number', 'current_location', 'pickup_location', 'dropoff_location', 'cycle_hours']
