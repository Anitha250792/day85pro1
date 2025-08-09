from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='list'),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), name='detail'),
    path('note/create/', views.NoteCreateView.as_view(), name='create'),
    path('note/<int:pk>/update/', views.NoteUpdateView.as_view(), name='update'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete'),
]
