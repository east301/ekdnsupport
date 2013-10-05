from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from lib.models import GpxData


class RunningLog(models.Model):
    id = models.AutoField(primary_key=True)

    owner = models.ForeignKey(User)
    description = models.CharField(max_length=1024)
    gpx = models.ForeignKey(GpxData)

    created = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.id is None and self.created is None:
            self.created = timezone.now()

        return super(RunningLog, self).save(*args, **kwargs)
