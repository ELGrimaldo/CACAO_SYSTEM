from django.db import models

class BoxOne(models.Model):
    reading_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    mq2 = models.IntegerField()
    mq3 = models.IntegerField()
    mq7 = models.IntegerField()
    mq9 = models.IntegerField()
    mq135 = models.IntegerField()

    def __str__(self):
        return str(self.reading_id)

class BoxTwo(models.Model):
    reading_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    mq2 = models.IntegerField()
    mq3 = models.IntegerField()
    mq7 = models.IntegerField()
    mq9 = models.IntegerField()
    mq135 = models.IntegerField()

    def __str__(self):
        return str(self.reading_id)
    
class BoxThree(models.Model):
    reading_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    mq2 = models.IntegerField()
    mq3 = models.IntegerField()
    mq7 = models.IntegerField()
    mq9 = models.IntegerField()
    mq135 = models.IntegerField()

    def __str__(self):
        return str(self.reading_id)
    
class BoxFour(models.Model):
    reading_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    mq2 = models.IntegerField()
    mq3 = models.IntegerField()
    mq7 = models.IntegerField()
    mq9 = models.IntegerField()
    mq135 = models.IntegerField()

    def __str__(self):
        return str(self.reading_id)
