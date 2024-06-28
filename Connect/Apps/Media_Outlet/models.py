from django.db import models

class Showroom(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)

    def __str__(self):
        return self.name

    class Meta:

        db_table = "Showroom"
        verbose_name_plural = "Showroom"

# ----------------------------------------------------------------------------------------------------------------------

class RSM(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "RSM"
        verbose_name_plural = "RSM"

# ----------------------------------------------------------------------------------------------------------------------

class ASM(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "ASM"
        verbose_name_plural = "ASM"

# ----------------------------------------------------------------------------------------------------------------------

class Manager(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Manager"
        verbose_name_plural = "Manager"

# ----------------------------------------------------------------------------------------------------------------------

class Region(models.Model):
    Name = models.CharField(max_length=150)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Region"
        verbose_name_plural = "Region"

# ----------------------------------------------------------------------------------------------------------------------

class State(models.Model):

    Name = models.CharField(max_length=100,blank=False,null=False)

    def __str__(self):
        return self.Name

    class Meta:

        db_table = "State"
        verbose_name_plural = "State"

########################################################################################################################

class Showroom_Details(models.Model):

    Showroom = models.ForeignKey(to=Showroom,null=True,blank=True,on_delete=models.SET_NULL)
    RSM = models.ForeignKey(to=RSM,null=True,blank=True,on_delete=models.SET_NULL)
    ASM = models.ForeignKey(to=ASM,null=True,blank=True,on_delete=models.SET_NULL)
    Manager = models.ForeignKey(to=Manager,null=True,blank=True,on_delete=models.SET_NULL)
    CUG_No = models.CharField(max_length=15,blank=True,null=True)
    Landline = models.CharField(max_length=20,blank=True,null=True)
    Email = models.EmailField(blank=True,null=True)
    Region = models.ForeignKey(to=Region,null=True,blank=True,on_delete=models.SET_NULL)
    State = models.ForeignKey(to=State,null=True,blank=True,on_delete=models.SET_NULL)
    Address = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return self.Showroom.name

    class Meta:
        db_table = "Showroom_Details"
        verbose_name_plural = "Showroom Details"

########################################################################################################################

class class_Details(models.Model):

    Name = models.CharField(max_length=100)
    Status = models.CharField(max_length=10,blank=True,null=True,choices=(("Active","Active"),('Inactive','Inactive')))

    def __str__(self):

        return self.Name

    class Meta:
        db_table = "class_Details"
        verbose_name_plural = "class Management"

# ----------------------------------------------------------------------------------------------------------------------

class Brand(models.Model):

    Name = models.CharField(max_length=100)
    Status = models.CharField(max_length=10, blank=True, null=True,choices=(("Active", "Active"), ('Inactive', 'Inactive')))

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Brand"
        verbose_name_plural = "Brand"

# ----------------------------------------------------------------------------------------------------------------------

class Brand_type(models.Model):

    Name = models.CharField(max_length=100)
    Status = models.CharField(max_length=10, blank=True, null=True,choices=(("Active", "Active"), ('Inactive', 'Inactive')))

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Brand_type"
        verbose_name_plural = "Brand type"

# ----------------------------------------------------------------------------------------------------------------------

class Vendors(models.Model):
    Name = models.CharField(max_length=100)
    Status = models.CharField(max_length=10, blank=True, null=True,choices=(("Active", "Active"), ('Inactive', 'Inactive')))
    Vendor_Comments = models.CharField(max_length=1000)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Vendors"
        verbose_name_plural = "Vendors"

# ----------------------------------------------------------------------------------------------------------------------

class Brand_Location(models.Model):
    Name = models.CharField(max_length=100)
    Status = models.CharField(max_length=10,blank=True, null=True,choices=(("Active", "Active"), ('Inactive', 'Inactive')))

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Brand_Location"
        verbose_name_plural = "Brand Location"

# ----------------------------------------------------------------------------------------------------------------------

class Material_Type(models.Model):
    Name = models.CharField(max_length=100)
    Status = models.CharField(max_length=10, blank=True, null=True,choices=(("Active", "Active"), ('Inactive', 'Inactive')))

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Material_Type"
        verbose_name_plural = "Material Type"

# ----------------------------------------------------------------------------------------------------------------------

class Light_Type(models.Model):
    Name = models.CharField(max_length=100)
    Status = models.CharField(max_length=10, blank=True, null=True,choices=(("Active", "Active"), ('Inactive', 'Inactive')))

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Light_Type"
        verbose_name_plural = "Light Type"

# ----------------------------------------------------------------------------------------------------------------------

class Status(models.Model):
    Name = models.CharField(max_length=100)
    status = models.CharField(max_length=10,blank=True,null=True, choices=(("Active", "Active"), ('Inactive', 'Inactive')))
    Visiblity = models.CharField(max_length=10, blank=True, null=True,choices=(("Assets", "Assets"), ('Vendor', 'vendor')))

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Status"
        verbose_name_plural = "Status"

# ----------------------------------------------------------------------------------------------------------------------

class Floor_Diagram(models.Model):
    Showroom = models.ForeignKey(to=Showroom, blank=True, null=True, on_delete=models.SET_NULL)
    Floor_diagram = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.Showroom
    class Meta:
        db_table = "Floor_Diagram"
        verbose_name_plural = "Floor Diagram"

# ----------------------------------------------------------------------------------------------------------------------

class full_img(models.Model):
    Showroom = models.ForeignKey(to=Showroom, blank=False, null=False, on_delete=models.CASCADE)
    Url = models.URLField(blank=True,null=True)
    Grade = models.CharField(max_length=10,blank=False,null=False,choices=(("A+", "A+"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"), ("F", "F"), ("G", "G"), ("H", "H"), ("I", "I"), ("J", "J"), ("K", "K")))

    class Meta:
        verbose_name_plural = "360 Degree Image"

# ----------------------------------------------------------------------------------------------------------------------

class Ad_Status(models.Model):

    name = models.CharField(max_length=100,blank=False,null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Ad_Status"
        verbose_name_plural = "AD Status"
########################################################################################################################

class AssetManagement(models.Model):
    class_Details = models.ForeignKey(to=class_Details, blank=True, null=True, on_delete=models.SET_NULL)
    Showroom = models.ForeignKey(to=Showroom, blank=True, null=True, on_delete=models.SET_NULL)
    Brand_type = models.ForeignKey(to=Brand_type,blank=True, null=True, on_delete=models.SET_NULL)
    Brand_Location = models.ForeignKey(to=Brand_Location, blank=True, null=True, on_delete=models.SET_NULL)
    Width = models.CharField(max_length=20,blank=True,null=True)
    Height = models.CharField(max_length=20,blank=True,null=True)
    Material_Type = models.ForeignKey(to=Material_Type, blank=True,null=True, on_delete=models.SET_NULL)
    Light_Type = models.ForeignKey(to=Light_Type, blank=True, null=True, on_delete=models.SET_NULL)
    Asset_Image = models.URLField(blank=True,null=True)
    status = models.CharField(max_length=10,blank=True,null=True, choices=(("Enable", "Enable"), ('Disable', 'Disable')))
    Other_Comments = models.CharField(max_length=1000,blank=True,null=True)
    Brand = models.ForeignKey(to=Brand,blank=True,null=True,on_delete=models.SET_NULL)
    Model_Name = models.CharField(max_length=100,blank=True,null=True)
    Vendor = models.ForeignKey(to=Vendors,blank=True,null=True,on_delete=models.SET_NULL)
    Expire_On = models.DateField(null=True,blank=True)
    AD_Image = models.URLField(blank=True,null=True)
    Ad_Status = models.ForeignKey(to=Ad_Status, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Showroom.name

    class Meta:
        db_table = "AssetManagement"
        verbose_name_plural = "Asset Management"

########################################################################################################################