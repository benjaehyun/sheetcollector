from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sheets/', views.sheets_index, name='index'),
    path('sheets/<int:sheet_id>/', views.sheets_detail, name='detail'),
    path('sheets/create/', views.SheetCreate.as_view(), name='sheets_create'),
    path('sheets/<int:pk>/update/', views.SheetUpdate.as_view(), name='sheets_update'),
    path('sheets/<int:pk>/delete/', views.SheetDelete.as_view(), name='sheets_delete'),
]