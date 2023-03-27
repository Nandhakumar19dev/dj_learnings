from django.urls import path, include
from . import views
urlpatterns = [
    path("home", views.home_view, name="home-view"),
    path('success/', views.success_view, name='payments-success'), # new
    path('cancel/', views.cancel_view, name='payments-cancel'), # new
    path("checkout/", views.checkout, name='checkout'),
]