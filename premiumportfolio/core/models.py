from django.db import models


# Project DB Tables
class ProjectCategory(models.Model):
    """DB table for the Project Category"""
    title = models.CharField(max_length=30)
    # image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        """string representation"""
        return self.title


class Tech(models.Model):
    """DB table that holds the techs used in projects"""
    title = models.CharField(max_length=30)

    def __str__(self):
        """string representation"""
        return self.title


class Project(models.Model):
    """DB table for the project details"""
    projectCategory = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    summary = models.TextField()
    desc = models.TextField()
    techs = models.ManyToManyField(Tech)
    codeLink = models.CharField(max_length=255)
    viewLink = models.CharField(max_length=255)

    def __str__(self):
        """string representation"""
        return f'{self.title} - {self.projectCategory.title}'


# About & Services DB Tables
class Skill(models.Model):
    """DB table for the developer's skills"""
    title = models.CharField(max_length=30)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        """string representation"""
        return str(self.percentage)


class Resume(models.Model):
    """DB table to hold the resume .pdf file"""
    developer = models.CharField(max_length=50)
    resume = models.FileField(upload_to='uploads/')

    def __str__(self):
        """string representation"""
        return f'{self.developer} Resume'


class Service(models.Model):
    """DB table to hold developer's services"""
    title = models.CharField(max_length=30)

    def __str__(self):
        """string representation"""
        return self.title


class ServiceCategory(models.Model):
    """DB table for the Service Category"""
    title = models.CharField(max_length=30)
    desc = models.TextField()
    icon = models.CharField(max_length=30)
    services = models.ManyToManyField(Service)

    def __str__(self):
        """string representation"""
        return self.title
    

class Contact(models.Model):
    """DB table to hold the developer's contact info"""
    summary = models.TextField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        """string representation"""
        return self.email
