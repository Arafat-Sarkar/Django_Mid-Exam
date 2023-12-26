from django.urls import path
from .import views

urlpatterns = [
    
    path ('details/<int:pk>/', views.Details.as_view(), name='detalisPage'),
    # path ('details/<int:pk>/', views.ProfileDetails.as_view(), name='profile'),
    path('buynow/<int:id>/', views.BuyNow, name='buynow')
]
