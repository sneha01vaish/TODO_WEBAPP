from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TODO(models.Model):
    status_choices = [
        ('C', 'COMPLETED'),
        ('P', 'PENDING'),
    ]
    priority_choices =[
        ('1', '1️⃣'),
        ('2', '2️⃣'),
        ('3', '3️⃣'),
        ('4', '4️⃣'),
        ('5', '5️⃣'),
        ('6', '6️⃣'),
        ('7', '7️⃣'),
        ('8', '8️⃣'),
        ('9', '9️⃣'),
        ('10', '1️⃣0️⃣'),
    
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    priority= models.CharField(max_length=2, choices=priority_choices)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)