from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="home"),
    path("about-us/", views.AboutView.as_view(), name="about"),
    path("services/", views.ServicesView.as_view(), name="services"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path('upload/', views.CSVUploadView.as_view(), name='upload_csv')
]