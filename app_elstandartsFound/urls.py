from django.urls import path
from . import views

urlpatterns = [
    path('elstandardsfound/', views.StandardListView.as_view(), name='standard-list'),
    path('elstandardsfound/<int:pk>/', views.StandardDetailView.as_view(), name='standard-detail'),
    path('elstandardsfound/photos/', views.elstandartsFoundPhotoListView.as_view(), name='photo-list'),
    path('elstandardsfound/photos/<int:pk>/', views.elstandartsFoundPhotoDetailView.as_view(), name='photo-detail'),
]
