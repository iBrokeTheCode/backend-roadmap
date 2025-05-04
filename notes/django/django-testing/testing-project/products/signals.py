from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import User


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        # print('Signal fired!')
        subject = 'Thank you for signing up'
        message = 'Welcome to the app'
        from_email = 'admin@django.com'
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
