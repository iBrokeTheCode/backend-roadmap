from unittest.mock import patch

from django.test import TestCase

from products.models import User


class UserSignalsTest(TestCase):
    @patch('products.signals.send_mail')
    def test_welcome_email_sent_on_user_creation(self, mock_send_mail):
        """Tests that the welcome email signal sends an email when a new user is created."""
        User.objects.create_user(
            username='test', password='password', email='test@example.com'
        )

        mock_send_mail.assert_called_once_with(
            'Thank you for signing up',  # Subject
            'Welcome to the app',  # Message
            'admin@django.com',  # From Email
            ['test@example.com'],  # Recipient List
            fail_silently=False,  # Match argument in signal
        )

    @patch('products.signals.send_mail')
    def test_no_email_sent_on_user_update(self, mock_send_email):
        """Tests that the welcome email signal does not send an email when an existing user is updated."""
        user = User.objects.create_user(
            username='test', password='password', email='test@example.com'
        )

        mock_send_email.reset_mock()  # Reset the mock to clear the call from the creation step
        user.email = 'new_test@example.com'  # Update the user and save (this triggers the signal again but 'created' will be False)
        user.save()

        mock_send_email.assert_not_called()  # Assert that send_mail was NOT called after the update
