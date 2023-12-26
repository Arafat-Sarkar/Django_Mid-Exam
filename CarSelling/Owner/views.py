from django.shortcuts import render
from .models import profileModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

def Profile(request):
    data = profileModel.objects.all()
    return render (request, 'profiles.html',  {'data':data})