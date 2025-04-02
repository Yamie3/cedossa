from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'truncated_message', 'submitted_at', 'is_responded', 'days_since_submission')
    list_filter = ('is_responded', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('submitted_at', 'days_since_submission')
    date_hierarchy = 'submitted_at'
    actions = ['mark_as_responded']
    list_per_page = 20

    fieldsets = (
        ('Message Details', {
            'fields': ('name', 'email', 'message')
        }),
        ('Response Status', {
            'fields': ('is_responded', 'response_notes', 'submitted_at')
        }),
    )

    def truncated_message(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    truncated_message.short_description = 'Message Preview'

    def mark_as_responded(self, request, queryset):
        updated = queryset.update(is_responded=True)
        self.message_user(request, f"{updated} messages marked as responded")
    mark_as_responded.short_description = "Mark selected as responded"

    def save_model(self, request, obj, form, change):
        if obj.is_responded and obj.response_notes:
            self.send_response_notification(obj)
        super().save_model(request, obj, form, change)

    def send_response_notification(self, message):
        subject = f"Response to your message from {message.submitted_at.strftime('%Y-%m-%d')}"
        body = f"Hello {message.name},\n\n" \
               f"We've responded to your message:\n\n" \
               f"{message.response_notes}\n\n" \
               f"Original message: {message.message[:200]}...\n\n" \
               f"Thank you,\n{settings.SITE_NAME}"
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [message.email],
            fail_silently=False,
        )