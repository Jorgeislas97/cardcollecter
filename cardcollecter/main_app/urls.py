from django.urls import path
from . import views 



urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('cards/',views.cards_index, name='index'),
    path('cards/<int:card_id>/', views.cards_detail, name='detail'),
    path('cards/create/', views.CardCreate.as_view(), name='Cards_create'),
    path('card/<int:pk>/update/' , views.CardUpdate.as_view(),name='cards_update'),
    path('card/<int:pk>/delete/' , views.CardDelete.as_view(),name='cards_delete'),

]