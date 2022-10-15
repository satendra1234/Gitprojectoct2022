# from accounts.models import send_email_token
from django.conf import settings
from django.core.mail import send_mail

def send_account_activation_email(email,email_token):
    subject = 'Your Account needs to be verified'
    email_from = settings.EMAIL_HOST_USER
    massage = f'Hi, click on the ling activate your land http://127.0.0.1:8000/account/activate/{email_token}'
    send_mail(subject,massage,email_from,[email])