from django.db import models

# Create your models here.
class contactdata(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    portfolio = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    image = models.ImageField(upload_to='image')
  
    
   



    
    def __str__(self):
        return self.name


     



