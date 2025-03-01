from django.db import models

class Log(models.Model):
    date = models.DateField()
    driver_name = models.CharField(max_length=255)
    truck_number = models.IntegerField()
    
    current_lat = models.FloatField()
    current_lng = models.FloatField()
    pickup_lat = models.FloatField()
    pickup_lng = models.FloatField()
    dropoff_lat = models.FloatField()
    dropoff_lng = models.FloatField()

    def __str__(self):
        return f"Log {self.id} - {self.driver_name} ({self.date})"

class CycleHours(models.Model):
    log = models.ForeignKey(Log, related_name='cycle_hours', on_delete=models.CASCADE)
    status_id = models.IntegerField()
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    
    start_lat = models.FloatField()
    start_lng = models.FloatField()
    end_lat = models.FloatField()
    end_lng = models.FloatField()

    distance = models.FloatField()
    annotations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cycle {self.id} - Log {self.log.id}"
