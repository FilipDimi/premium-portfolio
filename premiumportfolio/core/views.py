from django.shortcuts import render
from core import models

# Core pages views
def home(request):
    """Send GET request for the index page"""
    projectCategories = models.ProjectCategory.objects.all()
    projects = models.Project.objects.all()
    serviceCategories = models.ServiceCategory.objects.all()
    s_services = models.Service.objects.all()

    passing_dict = {
        'projectCategories': projectCategories,
        'projects': projects,
        'serviceCategories': serviceCategories,
        's_services': s_services
    }
    return render(request, 'core/index.html', passing_dict)


def about(request):
    """Send GET request for the about page"""
    skills = models.Skill.objects.all()
    resume = models.Resume.objects.all()

    passing_dict = {
        'skills': skills,
        'resume': resume
    }
    return render(request, 'core/about.html', passing_dict)


def services(request):
    """Send GET request for the services page"""
    s_services = models.Service.objects.all()
    serviceCategories = models.ServiceCategory.objects.all()

    passing_dict = {
        's_service': s_services,
        'serviceCategories': serviceCategories
    }
    return render(request, 'core/services.html', passing_dict)


def works(request):
    """Send GET request for the works page"""
    projectCategories = models.ProjectCategory.objects.all()
    projects = models.Project.objects.all()

    passing_dict = {
        'projectCategories': projectCategories,
        'projects': projects
    }
    return render(request, 'core/works.html', passing_dict)


def contact(request):
    """Send GET request for the contact page"""
    contact = models.Contact.objects.all()

    passing_dict = {
        'contact': contact
    }
    return render(request, 'core/contact.html', passing_dict)


# Nested Views
def detail_project(request, pk):
    project = models.Project.objects.get(pk=pk)
    techs = project.techs.all()

    passing_dict = {
        'project': project,
        'techs': techs
    }
    return render(request, 'core/project.html', passing_dict)