from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def users(request):
    if request.user.is_authenticated:
        if request.user.is_school:
            return redirect('schools:grade_list')
        else:
            return redirect('parents:kid_list')
    return render(request, '/start.html')
