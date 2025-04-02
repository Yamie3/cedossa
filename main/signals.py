from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_admins
from django.template.loader import render_to_string
from django.conf import settings
from .models import ContactMessage

@receiver(post_save, sender=ContactMessage)
def notify_admins_on_new_message(sender, instance, created, **kwargs):
    if created:
        subject = f"New contact message from {instance.name}"
        message = render_to_string('emails/new_contact_message.txt', {
            'message': instance,
            'site_name': settings.SITE_NAME
        })
        
        mail_admins(
            subject=subject,
            message=message,
            html_message=render_to_string('emails/new_contact_message.html', {
                'message': instance,
                'site_name': settings.SITE_NAME
            })
        )