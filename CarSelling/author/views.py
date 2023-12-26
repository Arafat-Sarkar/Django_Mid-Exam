
from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from Car.models import carmodel
from Brand.models import brandmodel

# Create your views here.

def Home(request , brand_slug = None):
    data = carmodel.objects.all()
    if brand_slug is not None:
        brand = brandmodel.objects.get(slug = brand_slug)
        data = carmodel.objects.filter(Brand = brand)
    BrandName = brandmodel.objects.all()
    return render(request, 'index.html ', {'data': data, 'BrandName':BrandName})

# def profile(request):
#     return render(request, 'profile.html')

def Register(request):
    if request.method == 'POST':
        regiser_form = forms.RegisterForm(request.POST)
        if regiser_form.is_valid():
            regiser_form.save()
            messages.success (request, 'Account Created Successfully') 
            return redirect('register')
    
    else :
        regiser_form = forms.RegisterForm(request.POST)
    return render (request, 'register.html', {'form': regiser_form, 'type': 'Register'})
       

class UserLogin(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profilepage')
    def form_valid(self,form):
        messages.success(self.request, 'Loggin successfully')
        return super().form_valid(form)
    
    def  form_invalid(self, form):
        messages.success(self.request, 'Loggin incorent')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['type']='Login'
        return context
    
    
class UserLogout(LogoutView):
    template_name = 'register.html',
    
    def get_success_url(self): 
        messages.success(self.request , 'Logout Succssfully')
        return reverse_lazy('register')
        
    
  
    
        
    
    
