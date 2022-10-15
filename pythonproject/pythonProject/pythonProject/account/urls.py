from django.urls import path
from account.views import Register, login_page, activate_email

urlpatterns = [
    path('login', login_page),
    path('register', Register),
    path('activate/<email_token>', activate_email),
]
