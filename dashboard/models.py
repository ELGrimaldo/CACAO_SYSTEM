from django.db import models

# This class is used to store each sensor reading
class SensorData(models.Model):
    reading_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    mq2 = models.IntegerField()
    mq3 = models.IntegerField()
    mq7 = models.IntegerField()
    mq9 = models.IntegerField()
    mq135 = models.IntegerField()

    def __str__(self):
        return str(self.reading_id)


class CacaoImages(models.Model):
    upload = models.ImageField(upload_to='static/media/images')
    
    def __str__(self) -> str:
        return str(self.pk)