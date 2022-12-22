from django.urls import path

from Coworking import views


app_name = 'coworking'
urlpatterns = [
    path('info/', views.create_request, name='info'),
    path('rate/', views.rate, name='rate'),
]