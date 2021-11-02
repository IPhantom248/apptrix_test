from django.shortcuts import render
from django.views.generic import CreateView

from members.models import Member


def home_view(request):
    return render(request, 'home_page.html')


