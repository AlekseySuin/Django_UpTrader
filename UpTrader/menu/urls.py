from django.urls import path
from .views import PageWithMenuView

urlpatterns = [
    path('', PageWithMenuView.as_view(template_name='menu/home.html'), name='home'),
    path('about/', PageWithMenuView.as_view(template_name='menu/about.html'), name='about'),
    path('about/history/', PageWithMenuView.as_view(template_name='menu/history.html'), name='history'),
    path('about/team/', PageWithMenuView.as_view(template_name='menu/team.html'), name='team'),
    path('contact/', PageWithMenuView.as_view(template_name='menu/contact.html'), name='contact'),
]