from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import Event
from django.utils.timezone import now
# Import your forms and models
from .forms import ContactForm
from .models import ContactMessage

# -------------------------
# Homepage
# -------------------------
def home(request):
    """Render homepage with programs preview"""
    programs_list = [
        {
            'title': 'Autism Support',
            'description': 'Early intervention, sensory activities, speech therapy, and inclusive education programs for children with autism.',
            'color': 'blue-600',
            'url_name': 'autism_support'
        },
        {
            'title': 'Down Syndrome Support',
            'description': 'Specialized healthcare, developmental learning, and advocacy programs for children with Down Syndrome and their families.',
            'color': 'yellow-600',
            'url_name': 'down_syndrome_support'
        },
        {
            'title': 'Inclusive Education Training',
            'description': 'Training schools and teachers on inclusive education practices to accommodate children with special needs.',
            'color': 'green-600',
            'url_name': '#'
        },
        {
            'title': 'Community Outreach',
            'description': 'Awareness campaigns and family counseling programs to support children with disabilities and their communities.',
            'color': 'purple-600',
            'url_name': '#'
        }
    ]

    return render(request, 'index.html', {
        'title': 'Home',
        'programs': programs_list
    })

# -------------------------
# Static Pages
# -------------------------
def about(request):
    return render(request, 'about.html', {'title': 'About Us'})

def donate(request):
    return render(request, 'donate.html', {'title': 'Donate'})

def autism_support(request):
    return render(request, 'autism_support.html', {'title': 'Autism Support'})

def down_syndrome_support(request):
    return render(request, 'down_syndrome_support.html', {'title': 'Down Syndrome Support'})

def resources(request):
    return render(request, 'resources.html', {'title': 'Resources'})

def volunteer(request):
    return render(request, 'volunteer.html', {'title': 'Volunteer'})

# -------------------------
# Contact
# -------------------------
@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
                return redirect('main:contact_success')
            except Exception:
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
    return render(request, 'contact_success.html', {'title': 'Message Received'})

# -------------------------
# Programs Page
# -------------------------
def programs(request):
    """Render programs page with dynamic program list"""
    programs_list = [
        {
            'title': 'Autism Support',
            'description': 'Early intervention, sensory activities, speech therapy, and inclusive education programs for children with autism.',
            'color': 'blue-600',
            'url_name': 'autism_support'
        },
        {
            'title': 'Down Syndrome Support',
            'description': 'Specialized healthcare, developmental learning, and advocacy programs for children with Down Syndrome and their families.',
            'color': 'yellow-600',
            'url_name': 'down_syndrome_support'
        },
        {
            'title': 'Inclusive Education Training',
            'description': 'Training schools and teachers on inclusive education practices to accommodate children with special needs.',
            'color': 'green-600',
            'url_name': '#'
        },
        {
            'title': 'Community Outreach',
            'description': 'Awareness campaigns and family counseling programs to support children with disabilities and their communities.',
            'color': 'purple-600',
            'url_name': '#'
        }
    ]

    return render(request, 'our_programs.html', {
        'title': 'Our Programs',
        'programs': programs_list
    })
def events(request):
    upcoming_events = Event.objects.filter(
        is_published=True,
        date__gte=now().date()
    )

    past_events = Event.objects.filter(
        is_published=True,
        date__lt=now().date()
    )

    context = {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'title': 'Events'
    }
    return render(request, 'events.html', context)
def sickle_cell_support(request):
    return render(request, 'main/sickle_cell_support.html', {
        'title': 'Sickle Cell Support'
    })
