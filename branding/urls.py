from django.urls import path
from .views import (
    BrandingListView, 
    BrandingDetailView,
    BrandingCreateView,
    BrandingUpdateView,
    BrandingDeleteView
)
from . import views

urlpatterns = [
    path('', BrandingListView.as_view(), name='branding-home'),
    path('branding/<int:pk>/', BrandingDetailView.as_view(), name='branding-detail'),
    path('branding/new/', BrandingCreateView.as_view(), name='branding-create'),
    path('branding/<int:pk>/update/', BrandingUpdateView.as_view(), name='branding-update'),
     path('branding/<int:pk>/delete/', BrandingDeleteView.as_view(), name='branding-delete'),
    path('about/', views.about, name='branding-about'),
]
