from celery import Celery

# Celery configuration
celery_app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',  # Using Redis as the message broker
    backend='redis://localhost:6379/0'  # Redis for result backend as well
)

celery_app.conf.task_routes = {'send_email': 'emails'}

@celery_app.task(name="send_email")
def send_email(email: str, subject: str, body: str):
    # Mock implementation of email sending
    print(f"Sending email to {email}: {subject}\n{body}")
    return "Email sent successfully"
