from django.contrib.auth.forms import *
from .models import *

class RegisterCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username']