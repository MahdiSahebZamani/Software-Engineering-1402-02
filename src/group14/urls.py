from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add-new-card/',views.add_new_card,name='add-new-card'),
    path('list-cards/', views.list_cards,name='list-cards'),
    path('edit-card/<int:card_id>/', views.edit_card,name='edit-card'),
    path('delete-card/<int:card_id>/', views.delete_card,name='delete-card')
] 
