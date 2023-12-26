from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home, name= 'home'),
    path('brand/<slug:brand_slug>/', views.Home, name= 'brand_wise_post'),
    path('register/',views.Register, name='register'),
    path('login/', views.UserLogin.as_view(), name= 'login'),
    path('logout/', views.UserLogout.as_view(), name= 'logout'),
    # path('profile/', views.profile, name= 'profile'),
    
]
