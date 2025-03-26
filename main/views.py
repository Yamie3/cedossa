from django.shortcuts import render
from .forms import ContactForm

def home(request):
    return render(request, 'index.html')  # Render homepage template

def about(request):
    return render(request, 'about.html')  # Render the custom About page

def contact(request):
    return render(request, 'contact.html')  # Render the Contact page

def donate(request):
    return render(request, 'donate.html')  # Render the Donate page

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form (save to database, send email, etc.)
            return render(request, 'contact_success.html')  # Success page after form submission
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})