from django.db import models

# Create your models here.
class Basic(models.Model):
    lng_lat = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=60, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    img_url = models.CharField(max_length=30,blank=True)
    price = models.CharField(max_length=10, blank=True)
    uid = models.CharField(db_index=True, max_length=200)
    # objects=Manager()
    # objects = models.Manager()
    class Meta:
        db_table="basic"
