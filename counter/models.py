from django.db import models

# Create your models here.

class FileLog(models.Model):
    ip_address=models.GenericIPAddressField(default='0.0.0.0',null=True, blank=True) #default 추가
    timestamp=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    status=models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return f"{self.ip_address} - {self.status} at {self.timestamp}"
