from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Render homepage template

def about(request):
    return render(request, 'about.html')  # Render the custom About page