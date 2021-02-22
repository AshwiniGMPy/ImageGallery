from django.db import models

IMAGE_CHOICES = (
    ('Nature','Nature'),
    ('Person', 'Person'),
    ('Sculpture','Sculpture'),
    ('Monuments','Monuments'),
    ('Objects','Objects'),
    ('Paintings','Paintings'),
    ('Others','Others'),
)

# Create your models here.
class Gallery(models.Model): 
    name = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='images/') 
    category = models.CharField(max_length=50, choices=IMAGE_CHOICES, default='Others')

class CategoryTable(models.Model):
    category = models.CharField(max_length=50) 
    path = models.CharField(max_length=250) 