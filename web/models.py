import uuid
from django.db import models

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio con dos decimales
    stock = models.IntegerField(default=0)
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
    def __str__(self):
        return self.customer_name
    
class Testimonio(models.Model):
    name = models.CharField(max_length=100)
    mensaje = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name