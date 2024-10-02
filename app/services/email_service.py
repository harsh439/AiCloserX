from core.tasks import send_email

class EmailService:
    @staticmethod
    def send_alert_email(to_email: str, subject: str, message: str):
        """
        Enqueues an email to be sent to the specified recipient.
        """
        send_email.delay(to_email, subject, message)

    @staticmethod
    def send_welcome_email(to_email: str):
        """
        Sends a welcome email to the user.
        """
        subject = "Welcome to Our Service!"
        message = "Thank you for registering. We're glad to have you."
        send_email.delay(to_email, subject, message)
