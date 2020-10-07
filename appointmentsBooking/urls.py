from django.urls import path
from . import views

urlpatterns = [
    path ('',views.home, name="home"),
    path ('home.html',views.home, name="home"),
    path('client.html',views.client, name="client"),
    path('practitioner.html',views.practitioner, name="practitioner"),
    path ('makeAppointment',views.makeAppointment, name="makeAppointment"),
    path ('makeRegistration',views.makeRegistration, name="makeRegistration"),
    path ('makeRecommendation',views.makeRecommendation, name="makeRecommendation"),
    path ('viewClientAppointment',views.viewClientAppointment, name="viewClientAppointment"),
    path ('viewRecommendation',views.viewRecommendation, name="viewRecommendation"),
    path ('viewPractionerAppointment',views.viewPractionerAppointment, name="viewPractionerAppointment"),
]
