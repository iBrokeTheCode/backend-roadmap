import os

from django.core.mail import send_mail
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from core.models import User


@receiver(post_save, sender=User, dispatch_uid="send_welcome_email")
def send_welcome_email(sender, instance, created, **kwargs):
    """Sends a welcome email to a user after they are created."""

    print("> Signal fired...")

    if created:
        subject = "Welcome"
        message = "Thank you for signing up"
        from_email = "admin@django.com"
        recipient_list = [instance.email]

        send_mail(subject, message, from_email, recipient_list)


@receiver(post_delete, sender=User, dispatch_uid="delete_associated_file")
def delete_associated_file(sender, instance, **kwargs):
    """Deletes the associated file from the filesystem when a User instance is deleted."""

    if instance.cv:
        if os.path.isfile(instance.cv.path):
            os.remove(instance.cv.path)
            print(f"> Deleted file: {instance.cv.path}")
