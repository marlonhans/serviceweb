from django.urls import path
from catalogo import views


urlpatterns = [
    path('', views.index, name='index'),
    path('servicios/', views.ServiceListView.as_view(), name='servicios'),
    path('service/<int:pk>', views.ServiceDetailView.as_view(), name='service-detail'),
]