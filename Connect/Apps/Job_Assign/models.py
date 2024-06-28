from django.db import models
from Apps.Media_Outlet.models import Showroom


class Job_For(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    Status = models.CharField(max_length=20, blank=False, null=False,choices=(("Active", "Active"), ('Deactive', 'Deactive')))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Job_For"
        verbose_name_plural = "Job_For"

# ----------------------------------------------------------------------------------------------------------------------

class Job_Type(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    Status = models.CharField(max_length=20, blank=False, null=False,choices=(("Active", "Active"), ('Deactive', 'Deactive')))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Job_Type"
        verbose_name_plural = "Job_Type"

# ----------------------------------------------------------------------------------------------------------------------

class Design_Type(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    Status = models.CharField(max_length=20, blank=False, null=False,choices=(("Active", "Active"), ('Deactive', 'Deactive')))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Design_Type"
        verbose_name_plural = "Design_Type"

# ----------------------------------------------------------------------------------------------------------------------

class Assign_To(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Assign_To"
        verbose_name_plural = "Assign_To"

# ----------------------------------------------------------------------------------------------------------------------

class Assign_By(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Assign_By"
        verbose_name_plural = "Assign_By"

# ----------------------------------------------------------------------------------------------------------------------

class Job_Form(models.Model):

    Job_Type = models.ForeignKey(to=Job_Type, blank=True, null=True, on_delete=models.SET_NULL)
    Job_For = models.ForeignKey(to=Job_For, blank=True, null=True, on_delete=models.SET_NULL)
    Design_Type = models.ForeignKey(to=Design_Type, blank=True, null=True, on_delete=models.SET_NULL)
    Showroom = models.ForeignKey(to=Showroom, blank=True, null=True, on_delete=models.SET_NULL)
    Priority = models.CharField(max_length=20, blank=False, null=False,choices=(("Medium", "Medium"), ('Top', 'Top'), ('Urgent', 'Urgent')))
    Assign_To = models.ForeignKey(to=Assign_To, blank=True, null=True, on_delete=models.SET_NULL)
    Status = models.CharField(max_length=20, blank=False, null=False,choices=(("Pending", "Pending"), ('Follow Up', 'Follow Up'), ('Completed', 'Completed')))
    Dead_Line = models.DateTimeField(blank=True,null=True)
    Comments = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.Job_Type

    class Meta:
        db_table = "Job_Form"
        verbose_name_plural = "Job_Form"

# ----------------------------------------------------------------------------------------------------------------------