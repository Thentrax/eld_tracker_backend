from django.db import models

class Trip(models.Model):
    current_location = models.CharField(max_length=255)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    cycle_hours = models.DecimalField(max_digits=5, decimal_places=2)
    route_details = models.TextField()
    log_sheets = models.TextField()

    def __str__(self):
        return f"Trip from {self.pickup_location} to {self.dropoff_location}"
