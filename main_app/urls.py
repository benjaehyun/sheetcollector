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
    path('sheets/<int:sheet_id>/add_listening/', views.add_listening, name='add_listening'),
    path('sheets/<int:sheet_id>/assoc_practice/<int:practice_id>/', views.assoc_practice, name='assoc_practice'),
    path('sheets/<int:sheet_id>/unassoc_practice/<int:practice_id>/', views.unassoc_practice, name='unassoc_practice'),
    path('practices/', views.PracticeList.as_view(), name='practices_index'), 
    path('practices/<int:pk>/', views.PracticeDetail.as_view(), name='practices_detail'), 
    path('practices/create/', views.PracticeCreate.as_view(), name='practices_create'), 
    path('practices/<int:pk>/update/', views.PracticeUpdate.as_view(), name='practices_update'), 
    path('practices/<int:pk>/delete/', views.PracticeDelete.as_view(), name='practices_delete'), 
]