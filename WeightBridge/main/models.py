from django.db import models


# Create your models here.
class VehicleType(models.Model):
    name= models.CharField(max_length=100)
    price= models.DecimalField(max_digits=6, decimal_places=2)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate= models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Reading(models.Model):
    weight1=models.DecimalField(decimal_places=3, max_digits=10, blank=True)
    weight2=models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True)
    netWeight= models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True)
    vehicleNumber= models.CharField(max_length=20)
    vehicleType= models.ForeignKey(VehicleType, related_name='vehicals', on_delete=models.PROTECT)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate= models.DateTimeField(auto_now=True)
    rate= models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)

    def save(self, *args, **kwargs):
        if self.weight1 and self.weight2:
            self.netWeight= abs(self.weight1-self.weight2)
        if not self.rate:
            self.rate = self.vehicleType.price
        super(Reading, self).save(*args, **kwargs)