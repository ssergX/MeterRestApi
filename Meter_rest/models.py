from django.db import models

class Data(models.Model):
    meter = models.CharField(max_length=255)
    qr = models.CharField(max_length=255, null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __repr__(self):
        return f"{self.meter} - счетчик. {self.qr} - QR-код"