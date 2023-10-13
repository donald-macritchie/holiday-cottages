from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('homestead-cottage/', views.homestead_cottage,
         name="homestead_cottage"),
    path('marketview-cottage/', views.marketview_cottage,
         name="marketview_cottage"),
    path('contact/', views.contact, name="contact"),
    path('success/', views.ContactSuccessView.as_view(), name="success"),
]
