from django.urls import reverse_lazy
from django.views import generic
from first_app.views import product_list
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
