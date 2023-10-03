from .import views
from django.urls import path,include


urlpatterns = [
path('home',views.home),
path('sign_up',views.sign_up, name="sign_up")

]
