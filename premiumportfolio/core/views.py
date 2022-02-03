from django.shortcuts import render

# Core pages views
def home(request):
    """Send GET request for the index page"""

    passing_dict = {}
    return render(request, 'core/index.html', passing_dict)


def about(request):
    """Send GET request for the about page"""

    passing_dict = {}
    return render(request, 'core/about.html', passing_dict)


def services(request):
    """Send GET request for the services page"""

    passing_dict = {}
    return render(request, 'core/services.html', passing_dict)


def works(request):
    """Send GET request for the works page"""

    passing_dict = {}
    return render(request, 'core/works.html', passing_dict)


def contact(request):
    """Send GET request for the contact page"""

    passing_dict = {}
    return render(request, 'core/contact.html', passing_dict)