from email import message
from email.policy import default
from django.db import models
from django.forms import BooleanField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="email", max_length=60)
    contact_no = PhoneNumberField(null=False, blank=False)
    subject = models.CharField(max_length=500)
    message = models.TextField()
    is_replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        # self.updated_at = timezone.now()
        return super(Contact, self).save(*args, **kwargs)
