from django.db import models

class SensorData(models.Model):
    box_no = models.TextField()
    mq2_value = models.IntegerField()
    mq3_value = models.IntegerField()
    mq7_value = models.IntegerField()
    mq9_value = models.IntegerField()
    mq135_value = models.IntegerField()
    ph_value = models.IntegerField()
    temp_value = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.timestamp)