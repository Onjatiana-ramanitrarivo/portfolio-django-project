from django.db import models

class ObservationModel(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    observation = models.CharField(max_length=100)
