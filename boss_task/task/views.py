from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.views.generic.list import ListView
from .models import User
from .forms import  UserCreationForm

# Create your views here.
class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)
        return success_url


class ProfileView(UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'profile_picture', 'address',]
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse('profile')

    def get_object(self):
        return self.request.user

class HomeView(ListView):
    template_name = 'home.html'
    queryset = User.objects.all()
    context_object_name = 'Users'
    paginate_by = 30