"""
Un modèle est la source d’information unique et définitive à propos de vos données. Il contient les champs et le comportement essentiels des données
que vous stockez. Généralement, chaque modèle correspond à une seule table de base de données.

Les bases :

-Chaque modèle est une classe Python qui hérite de django.db.models.Model.
-Chaque attribut du modèle représente un champ de base de données.
-Avec tout ça, Django vous offre une API d’accès à la base de données générée automatiquement ;
Donc on doit importer la bibliothèque "models"
"""
from django.db import models
# Create your models here.

"""
Par la suite on va créer les classes de notre diagramme de classe qui sont: Application, Menu_element, Sous_menu et Block_article
"""

# la classe application(intitulé, logo, bg_couleur_menu_element, bg_couleur_sous_menu,  bg_couleur_application)

class Application(models.Model):
    intitule = models.CharField(max_length=500)
    logo = models.CharField(max_length=10000)
    bg_couleur_menu_element = models.CharField(max_length=8)
    bg_couleur_sous_menu = models.CharField(max_length=8)
    bg_couleur_application = models.CharField(max_length=8)

    # cette methode permet Django à nous afficher le nom de l'application au lieu des mots qui ne sont pas significatifs
    def __str__(self):
        return self.intitule

# la classe menu_element(intitule, couleur, lien, ordre)

class Menu_element(models.Model):
    intitule = models.CharField(max_length=50)
    couleur = models.CharField(max_length=8)
    lien = models.TextField()
    ordre = models.IntegerField()
    application = models.ForeignKey(Application, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.intitule

# la classe sous_element(intitule, couleur, lien, ordre)

class Sous_menu(models.Model):
    SCRAPING_TYPE_CHOICES = (('youtube','youtube'),('youtube_playlist','youtube_playlist'), ('facebook','facebook'), ('instagram','instagram'),)
    intitule = models.CharField(max_length=50)
    couleur = models.CharField(max_length=8)
    lien = models.TextField()
    ordre = models.IntegerField()
    menu_element = models.ForeignKey(Menu_element, null=True, on_delete=models.SET_NULL)
    scraping_link = models.CharField(max_length=500, default='')
    scraping_type = models.CharField(max_length=20, choices=SCRAPING_TYPE_CHOICES, default='youtube')



    def __str__(self):
        return self.intitule

# la classe block_article(intitule, couleur, lien, ordre)

class Block_article(models.Model):
    intitule = models.CharField(max_length=50)
    couleur = models.CharField(max_length=8)
    lien = models.TextField()
    ordre = models.IntegerField()
    sous_menu = models.ForeignKey(Sous_menu, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.intitule
