from presentation import views
from django.urls import path

urlpatterns = [
    path('presentation/',views.accueil,name='home'),
    path('contact/', views.contact, name='contact'),
    path('observation/', views.observation, name='observation')
]