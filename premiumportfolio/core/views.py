from django.shortcuts import render
from django.core.mail import send_mail
from core import models

# Core pages views
def home(request):
    """Send GET request for the index page"""
    projectCategories = models.ProjectCategory.objects.all()
    projects = models.FeaturedProject.objects.all()
    serviceCategories = models.ServiceCategory.objects.all()
    s_services = models.Service.objects.all()
    techLogos = models.TechLogo.objects.all()

    passing_dict = {
        'projectCategories': projectCategories,
        'projects': projects,
        'serviceCategories': serviceCategories,
        's_services': s_services,
        'techLogos': techLogos
    }
    return render(request, 'core/index.html', passing_dict)


def about(request):
    """Send GET request for the about page"""
    skills = models.Skill.objects.all()
    resume = models.Resume.objects.all()
    developer = models.Contact.objects.all()

    passing_dict = {
        'skills': skills,
        'resume': resume,
        'developer': developer[0]
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
    developer = models.Contact.objects.all()

    passing_dict = {
        'developer': developer[0]
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


# Services Views
def send_email(request):
    """Send email to the developer - POST request"""
    developerEmail = models.Contact.objects.all()[0]
    message = ""

    if request.method == 'POST':
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message", "")

        if name and email and subject and message:
            send_mail(subject, message, 'f_dimitrievski@outlook.com', [developerEmail])
            message = {"id": 0, "msg": "Your message has been sent. Thank you!"}
        else:
            message = {"id": 1, "msg": "All fields are required"}

    passing_dict = {
        'message': message
    }
    return render(request, 'core/contact.html', passing_dict)

