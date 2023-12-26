from django.shortcuts import render,redirect
from django.views.generic import DetailView
from Car.models import carmodel
from Car import models
from .import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
# class ProfileDetails(DetailView):
#     model = models.carmodel
#     pk_url_kwarg = 'pk'
#     template_name = 'profile.html'
#     context_object_name = 'Car'
@method_decorator(login_required, name='dispatch')
class Details(DetailView):
    model = models.carmodel
    pk_url_kwarg = 'pk'
    template_name = 'showDetails.html'
    context_object_name = 'Car' 
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object # post model er object ekhane store korlam
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    

def BuyNow(request,id):
    car = carmodel.objects.get(pk = id)
    if car.quantity >0:
        car.quantity -= 1
        car.save()
        # return redirect('detalisPage')
    return redirect('profilepage')

