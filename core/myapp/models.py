from django.db import models
from django.utils import timezone   
# Create your models here.

class Application(models.Model):
    full_name = models.CharField(max_length=255)
    linkedin_url = models.URLField(verbose_name="Linkedin_URL", blank=True, null=False)
    location = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField(unique=True)
    experience = models.IntegerField()    
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
