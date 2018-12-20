from django.db import models

class MissionalCommunity(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    leader = models.CharField(max_length=20)
    assistant = models.CharField(max_length=30, blank=True, null=True)
    church_location = models.CharField(max_length=30)
    frontier = models.CharField(max_length=30)

    def __str__(self):
        return "{0}".format(self.name)