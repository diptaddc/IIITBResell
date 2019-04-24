from django.urls import reverse_lazy
from django.views import generic
from first_app.views import product_list
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomUserChangeForm
from .forms import CustomUserCreationForm
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('edit_profile'))
    else:
        form = CustomUserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)
