from django.db import models

# Create your models here.

# About Model
class About(models.Model):
    description = models.TextField()

    class Meta():
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"
    
# Service Model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    description = models.TextField(verbose_name="About service")

    def __str__(self):
        return self.name
    

# Works Model
class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Project title")
    project_badge = models.CharField(max_length=100)
    image = models.ImageField(upload_to="projects")

    def __str__(self):
        return self.title
    

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  


    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.name