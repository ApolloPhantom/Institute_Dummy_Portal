from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()
    bio = models.TextField()
    image = models.ImageField(upload_to='faculty_images/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.department}"
    
    class Meta:
        verbose_name_plural = "Faculty Members"

class Alumni(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    graduation_year = models.IntegerField()
    degree = models.CharField(max_length=100)
    current_company = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    linkedin_profile = models.URLField(blank=True)
    image = models.ImageField(upload_to='alumni_images/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.graduation_year}"
    
    class Meta:
        verbose_name_plural = "Alumni"