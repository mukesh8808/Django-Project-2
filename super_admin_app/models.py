from django.db import models

# Create your models here.

class Module(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    created_by = models.CharField(max_length=50, default="super admin")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name