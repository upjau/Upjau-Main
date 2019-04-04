from django.db import models
from accounts.models import *

# Farm Details
class farmer_farmLand(models.Model):
    address = models.TextField()
    state = models.CharField(max_length=25)
    district = models.CharField(max_length=50)
    subDistrict = models.CharField(max_length=50)
    pincode = models.IntegerField()
    size = models.IntegerField() # unit of measurement: acres
    soilType = models.CharField(max_length=50)
    waterSystem = models.CharField(max_length=25)
    purpose = models.CharField(max_length=8)
    server = models.ImageField(upload_to='ProfileImageWaliFile', blank=True)

    def __str__(self):
        return self.address


# Farm - Commodity Record
class farmer_commodityRecord(models.Model):
    commodity = models.CharField(max_length=20)

    def __str__(self):
        return self.commodity

# Farm - FarmerRecordProduce
class farmer_stockRecord(models.Model):
    username = models.ForeignKey(Profile)
    commodity = models.ForeignKey(farmer_commodityRecord)
    quantity = models.IntegerField()
    sellingRate = models.IntegerField()
