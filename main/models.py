from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class ContactMessage(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100,
        validators=[MinLengthValidator(2, _('Name must be at least 2 characters'))],
        help_text=_("Your full name")
    )
    email = models.EmailField(
        _('Email'),
        validators=[EmailValidator(message=_('Enter a valid email address'))],
        help_text=_("A valid email address")
    )
    message = models.TextField(
        _('Message'),
        max_length=2000,
        validators=[MinLengthValidator(10, _('Message must be at least 10 characters'))],
        help_text=_("Your message (10-2000 characters)")
    )
    submitted_at = models.DateTimeField(
        _('Submission Date'),
        auto_now_add=True,
        db_index=True  # Added for better query performance
    )
    is_responded = models.BooleanField(
        _('Responded Status'),
        default=False
    )
    response_notes = models.TextField(
        _('Admin Response'),
        blank=True,
        null=True
    )
    ip_address = models.GenericIPAddressField(
        _('IP Address'),
        blank=True,
        null=True,
        editable=False
    )

    class Meta:
        verbose_name = _('Contact Message')
        verbose_name_plural = _('Contact Messages')
        ordering = ['-submitted_at']
        db_table = 'contact_messages'
        permissions = [
            ('can_export_messages', _('Can export contact messages')),
        ]

    def __str__(self):
        return _("Message from %(name)s (%(email)s)") % {
            'name': self.name,
            'email': self.email
        }

    def mark_as_responded(self, notes="", commit=True):
        """Mark message as responded with optional notes"""
        self.is_responded = True
        self.response_notes = notes
        if commit:
            self.save()
        return self

    @property
    def days_since_submission(self):
        """Calculate days since message was submitted"""
        return (timezone.now() - self.submitted_at).days

    @classmethod
    def get_unresponded_messages(cls):
        """Get all unresponded messages"""
        return cls.objects.filter(is_responded=False)

    def clean(self):
        """Additional model-wide validation"""
        super().clean()
        if len(self.message.split()) < 3:  # At least 3 words
            raise models.ValidationError(
                _('Message should contain at least 3 words')
            )
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title