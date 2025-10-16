
from django.urls import path

from . import views


app_name = 'personnel'

urlpatterns = [

    # =======================================================
    # CRUD PERSONNEL
    # =======================================================

    # CREATE (Liste personnel)
    path('', views.PersonnelListView.as_view(), name='liste_personnels'),

    # CREATE (Ajouter personnel)
    path('ajouter/', views.PersonnelCreateView.as_view(), name='ajouter_personnel'),

    # READ (Détail personnel)
    path('<int:pk>/', views.detail_personnel, name='detail_personnel'),

    # UPDATE (Modifier personnel)
    path('<int:pk>/modifier/', views.PersonnelUpdateView.as_view(),
         name='modifier_personnel'),

    # DELETE (Supprimer personnel)
    path('<int:pk>/supprimer/', views.PersonnelDeleteView.as_view(),
         name='supprimer_personnel'),



    # =======================================================
    # CRUD VISITES
    # =======================================================

    # CREATE (Ajout direct)
    path('visites/ajouter/', views.VisiteCreateView.as_view(), name='ajouter_visite'),

    # CREATE (Ajout depuis le détail du personnel - optionnel, mais plus pratique)
    path('personnel/<int:personnel_pk>/visites/ajouter/',
         views.VisiteCreateView.as_view(),
         name='ajouter_visite_pour_personnel'),

    # UPDATE
    path('visites/<int:pk>/modifier/',
         views.VisiteUpdateView.as_view(), name='modifier_visite'),

    # DELETE
    path('visites/<int:pk>/supprimer/',
         views.VisiteDeleteView.as_view(), name='supprimer_visite'),





    # NOUVELLE ROUTE : Afficher l'Ordre de Mission pour impression
    path('visites/<int:pk>/ordre-mission/',
         views.OrdreMissionView.as_view(), name='ordre_mission'),
]
