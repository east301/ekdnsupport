import os
import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from ekdnsupport import settings


class GpxData(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(null=False, unique=True, max_length=32)

    owner = models.ForeignKey(User, null=True)
    description = models.CharField(null=True, max_length=1024)
    has_timestamp = models.BooleanField(null=False)

    created = models.DateTimeField(null=False)

    def save(self, *args, **kwargs):
        if self.id is None:
            self.uid = uuid.uuid4().hex
            self.created = timezone.now()

        return super(GpxData, self).save(*args, **kwargs)

    @property
    def path(self):
        return os.path.join(settings.GPX_ROOT, self.uid + '.gpx')
