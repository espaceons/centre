
from django.urls import path
from . import views


app_name = 'entreprise'

urlpatterns = [
    # CRUD pour le modèle Entreprise
    # -------------------------------------

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

    # tuteur entreprise
    # CRUD pour le modèle TuteurEntreprise
    # -------------------------------------
    # CREATE
    path('tuteur/ajouter/', views.TuteurEntrepriseCreateView.as_view(),
         name='ajouter_tuteur'),
    # UPDATE
    path('tuteur/<int:pk>/modifier/',
         views.TuteurEntrepriseUpdateView.as_view(), name='modifier_tuteur'),
    # DELETE
    path('tuteur/<int:pk>/supprimer/',
         views.TuteurEntrepriseDeleteView.as_view(), name='supprimer_tuteur'),
    # READ (Liste)
    path('tuteur/', views.TuteurEntrepriseListView.as_view(), name='liste_tuteurs'),
    # READ (Détail)
    path('tuteur/<int:pk>/', views.TuteurEntrepriseDetailView.as_view(),
         name='detail_tuteur'),

]
