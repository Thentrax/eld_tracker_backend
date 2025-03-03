from django.db import models

class Log(models.Model):
    date = models.DateField()
    driver_name = models.CharField(max_length=255)
    truck_number = models.IntegerField()
    
    current_lat = models.FloatField()
    current_lng = models.FloatField()
    current_location_address = models.CharField(max_length=255)

    pickup_lat = models.FloatField()
    pickup_lng = models.FloatField()
    pickup_location_address = models.CharField(max_length=255)

    dropoff_lat = models.FloatField()
    dropoff_lng = models.FloatField()
    dropoff_location_address = models.CharField(max_length=255)

class CycleHours(models.Model):
    log = models.ForeignKey(Log, related_name="cycle_hours", on_delete=models.CASCADE)
    status_id = models.IntegerField()
    start_hour = models.TimeField()
    end_hour = models.TimeField()

    start_lat = models.FloatField()
    start_lng = models.FloatField()
    start_location_address = models.CharField(max_length=255)

    end_lat = models.FloatField()
    end_lng = models.FloatField()
    end_location_address = models.CharField(max_length=255)

    distance = models.FloatField()
    annotations = models.TextField(null=True, blank=True)
