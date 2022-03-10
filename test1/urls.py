from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.TableTest),
    path('test/submit.php',views.test)
]