from django import forms
from django.core.exceptions import ValidationError
from .models import ContactMessage
from django.utils.translation import gettext_lazy as _
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Your Name'),
                'autocomplete': 'name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('your@email.com'),
                'autocomplete': 'email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': _('Your message...'),
            }),
        }
        labels = {
            'name': _('Full Name'),
            'email': _('Email Address'),
            'message': _('Your Message')
        }
        help_texts = {
            'message': _('Minimum 10 characters, maximum 2000 characters')
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap 'is-invalid' class for error fields
        for field in self.fields:
            if self.errors.get(field):
                self.fields[field].widget.attrs.update({
                    'class': self.fields[field].widget.attrs.get('class', '') + ' is-invalid'
                })

    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.match(r'^[a-zA-Z\s\-\.\']+$', name):
            raise ValidationError(
                _('Name can only contain letters, spaces, hyphens, and apostrophes')
            )
        return name.strip()

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message.split()) < 3:
            raise ValidationError(
                _('Message should contain at least 3 words')
            )
        return message

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Capture IP address if request is available
        if self.request:
            x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                instance.ip_address = x_forwarded_for.split(',')[0]
            else:
                instance.ip_address = self.request.META.get('REMOTE_ADDR')
        
        if commit:
            instance.save()
        return instance