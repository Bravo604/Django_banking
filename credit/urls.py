from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailClientView.as_view(), name='detail'),
    path('<int:pk>/credit', views.DetailCreditView.as_view(), name='detail_credit'),

    ]

