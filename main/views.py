from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .forms import ContactForm
from .models import ContactMessage  # Import model if using manual save

def home(request):
    """Render homepage with optional context"""
    return render(request, 'index.html', {'title': 'Home'})

def about(request):
    """Render about page with optional context"""
    return render(request, 'about.html', {'title': 'About Us'})

def donate(request):
    """Render donation page with optional context"""
    return render(request, 'donate.html', {'title': 'Donate'})

@require_http_methods(["GET", "POST"])  # Restrict to GET/POST only
def contact(request):
    """
    Handle contact form submissions with:
    - Form validation
    - Database save
    - User feedback
    - Error handling
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                # Option 1: Using ModelForm's save()
                contact_message = form.save()
                
                # Option 2: Manual save (uncomment if needed)
                # contact_message = ContactMessage(
                #     name=form.cleaned_data['name'],
                #     email=form.cleaned_data['email'],
                #     message=form.cleaned_data['message']
                # )
                # contact_message.save()
                
                messages.success(request, 'Message sent successfully!')
                return redirect('contact_success')  # Redirect to a success page
                
            except Exception as e:
                messages.error(request, f'Error sending message: {str(e)}')
                # Consider logging the error here
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
