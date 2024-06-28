from django.db import models

# ----------------------------------------------------------------------------------------------------------------------

class Domain(models.Model):

    Name = models.CharField(max_length=100,blank=False,null=False)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Domain"
        verbose_name_plural = "Domain"

# ----------------------------------------------------------------------------------------------------------------------

class Resource(models.Model):

    Name = models.CharField(max_length=100,blank=False,null=False)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Resource"
        verbose_name_plural = "Resource"

# ----------------------------------------------------------------------------------------------------------------------

class Rating(models.Model):

    Rating = models.CharField(max_length=1)

    def __str__(self):
        return self.Rating

    class Meta:
        db_table = "Rating"
        verbose_name_plural = "Rating"

# ----------------------------------------------------------------------------------------------------------------------

class Assign_Job(models.Model):

    Title = models.CharField(max_length=500, blank=False, null=False)
    Domain = models.ForeignKey(to=Domain,blank=True, null=True, on_delete=models.SET_NULL)
    Resource = models.ForeignKey(to=Resource,blank=True, null=True, on_delete=models.SET_NULL)
    Status = models.CharField(max_length=50, blank=True, null=True, choices=(("Completed", "Completed"), ('In-Process', 'In-Process'), ('Created', 'Created')))
    Rating = models.ForeignKey(to=Rating,blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Title

    class Meta:
        db_table = "Assign_Job"
        verbose_name_plural = "Assign_Job"

# ----------------------------------------------------------------------------------------------------------------------
