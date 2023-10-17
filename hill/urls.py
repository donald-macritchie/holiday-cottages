from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('homestead-cottage/', views.cottage_view,
         {'cottage_name': 'Homestead'}, name='homestead_cottage'),
    path('marketview-cottage/', views.cottage_view,
         {'cottage_name': 'Marketview'}, name='marketview_cottage'),
    path('contact/', views.ContactMessage.as_view(), name='contact'),
    path('success/', views.ContactSuccessView.as_view(), name='success'),
    path('things_to_do/', views.things_to_do, name='things_to_do'),
]
