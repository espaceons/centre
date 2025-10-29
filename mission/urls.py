
from django.urls import path

from mission import views


app_name = 'mission'

urlpatterns = [



    # =======================================================
    # CRUD VISITES
    # =======================================================

    # Listes des Visites
    path('', views.VisiteListView.as_view(), name='liste_missions'),

    # CREATE (Ajout direct)
    # 1. URL de base pour créer une mission (peut être appelée depuis le menu principal)

    path('creer/', views.VisiteCreateView.as_view(), name='creer_mission'),

    # 2. URL pour créer une mission dans le contexte d'un personnel spécifique
    # Cette URL est utile pour pré-remplir le champ 'personnel' dans le formulaire.

    path('personnel/<int:personnel_pk>/creer/',
         views.VisiteCreateView.as_view(), name='creer_mission_pour_personnel'),

    # 3. URL pour modifier une mission existante (nécessite l'ID de la mission)

    path('<int:pk>/modifier/', views.VisiteUpdateView.as_view(),
         name='modifier_mission'),


    # NOUVELLE ROUTE : Afficher l'Ordre de Mission pour impression
    # path('visites/<int:pk>/ordre-mission/',
    #      views.OrdreMissionView.as_view(), name='ordre_mission'),
]
