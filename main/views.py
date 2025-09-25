from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods

# Import your forms and models (adjust based on your app structure)
from .forms import ContactForm
from .models import ContactMessage

def home(request):
    """Render homepage"""
    return render(request, 'index.html', {'title': 'Home'})

def about(request):
    """Render about page"""
    return render(request, 'about.html', {'title': 'About Us'})

def donate(request):
    """Render donation page"""
    return render(request, 'donate.html', {'title': 'Donate'})

def autism_support(request):
    """Render autism support page"""
    return render(request, 'autism_support.html', {'title': 'Autism Support'})

def down_syndrome_support(request):
    """Render Down syndrome support page"""
    return render(request, 'down_syndrome_support.html', {'title': 'Down Syndrome Support'})

@require_http_methods(["GET", "POST"])
def contact(request):
    """
    Handle contact form submissions
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                # Save the form data to database
                contact_message = form.save()
                
                messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
                return redirect('contact_success')
                
            except Exception as e:
                # Log the error in production
                messages.error(request, 'Sorry, there was an error sending your message. Please try again.')
        else:
            messages.warning(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'title': 'Contact Us'
    })

def contact_success(request):
    """Display success page after contact submission"""
    return render(request, 'contact_success.html', {
        'title': 'Message Received'
    })

# Additional views you might need
def programs(request):
    """Render programs page"""
    return render(request, 'programs.html', {'title': 'Our Programs'})

def resources(request):
    """Render resources page"""
    return render(request, 'resources.html', {'title': 'Resources'})

def volunteer(request):
    """Render volunteer page"""
    return render(request, 'volunteer.html', {'title': 'Volunteer'})