
from django.db import models






class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)




