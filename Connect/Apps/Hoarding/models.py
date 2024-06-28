from django.db import models
from Apps.Media_Outlet.models import *

class Hoarding(models.Model):
    Site_Type = models.CharField(max_length=10,blank=True,null=True, choices=(("Own", "Own"), ('Rent', 'Rent')))
    Site_Location = models.CharField(max_length=100, blank=False, null=False)
    Brand_type = models.ForeignKey(to=Brand_type, null=True, blank=True, on_delete=models.SET_NULL)
    Brand_Location = models.CharField(max_length=100, blank=True, null=True)
    Width = models.IntegerField()
    Height = models.IntegerField()
    Material = models.ForeignKey(to=Material_Type, blank=True, null=True, on_delete=models.SET_NULL)
    Start_Date = models.DateField()
    Rent = models.CharField(max_length=100, blank=True, null=True)
    Asset_Image = models.FileField()
    Status = models.CharField(max_length=10,blank=True,null=True, choices=(("Enable", "Enable"), ('Disable', 'Disable')))
    Other_Comments = models.CharField(max_length=500, blank=True, null=True)
    Brand = models.ForeignKey(to=Brand, null=True, blank=True, on_delete=models.SET_NULL)
    Model_Name = models.CharField(max_length=100, blank=True, null=True)
    Vendor = models.ForeignKey(to=Vendors, null=True, blank=True, on_delete=models.SET_NULL)
    Light_Type = models.ForeignKey(to=Light_Type, null=True, blank=True, on_delete=models.SET_NULL)
    End_Date = models.DateField()
    Rent_Type = models.CharField(max_length=10,blank=True,null=True, choices=(("Month", "Month"), ('Year', 'Year')))
    AD_Image = models.FileField()
    AD_Status = models.CharField(max_length=50, blank=True, null=True,
                                 choices=(("Active", "Active"), ('Expired', 'Expired'),('Empty Space', 'Empty Space'),
                                          ('On Board Escalaton', 'On Board Escalaton'),('Approve', 'Approve'),
                                          ('BR-Waiting Action', 'BR-Waiting Action'),('Admin-Job Review', 'Admin-Job Review'),))

    def __str__(self):
        return self.Site_Location, self.Site_Type, self.Brand_Location

    class Meta:
        db_table = "Hoarding"
        verbose_name_plural = "Hoarding"