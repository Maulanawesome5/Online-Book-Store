from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from typing import Any
from .forms import CustomUserCreationForm
from .models import CustomUser


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserProfileView(DetailView):
    template_name = "accounts/profile.html"
    model = CustomUser
    extra_context = {}

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.method == "GET":
            self.extra_context.update({
                "page_title": CustomUser.objects.get(id=kwargs.get("pk")).username,
            })

        return super().get(request, *args, **kwargs)
