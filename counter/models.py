from django.db import models

# Create your models here.

class FileLog(models.Model):
    ip_address=models.GenericIPAddressField(default='0.0.0.0') #default 추가
    timestamp=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.ip_address} - {self.status} at {self.timestamp}"
