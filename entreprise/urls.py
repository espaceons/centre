
from django.urls import path
from . import views


app_name = 'entreprise'

urlpatterns = [
    # READ (Liste)
    path('', views.EntrepriseListView.as_view(), name='liste_entreprises'),

    # CREATE
    path('ajouter/', views.EntrepriseCreateView.as_view(),
         name='ajouter_entreprise'),

    # READ (Détail)
    path('<int:pk>/', views.EntrepriseDetailView.as_view(),
         name='detail_entreprise'),

    # UPDATE
    path('<int:pk>/modifier/', views.EntrepriseUpdateView.as_view(),
         name='modifier_entreprise'),

    # DELETE
    path('<int:pk>/supprimer/', views.EntrepriseDeleteView.as_view(),
         name='supprimer_entreprise'),
]
