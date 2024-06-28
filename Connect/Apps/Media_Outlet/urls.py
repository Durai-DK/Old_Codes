from django.urls import path
from Apps.Media_Outlet import views

urlpatterns = [
    path('Asset/', views.AssetList),
    path('Asset/<int:pk>/', views.AssetDetail),
]
