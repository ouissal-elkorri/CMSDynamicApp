"""
Le paquet "django.shortcuts" rassemble des fonctions et des classes utilitaires qui recouvrent plusieurs niveaux de l’architecture MVC.
En d’autres termes, ces fonctions/classes introduisent un couplage contrôlé à des fins de commodité.

"render" Combine un gabarit donné avec un dictionnaire contexte donné et renvoie un objet HttpResponse avec le texte résultant.

"""
from django.shortcuts import render
#On importe les clases créées dans models.py
from .models import Application, Menu_element, Sous_menu, Block_article
#On importe les fichiers du web scarping d'après le dossier webScraping
from webScaping import youtubeScraping, youtube_playlists_scrapping, face_book, scrapping_instagram


# Create your views here.

#Une fonction qui rend le menu dynamique

def list_menu(request):
    application = Application.objects.all().first()
    menu_element = Menu_element.objects.all()
    sous_menu = Sous_menu.objects.all()
    block_article = Block_article.objects.all()
    is_logo_display = True
    context = {'application': application, 'menu_element': menu_element, 'sous_menu': sous_menu, 'block_article': block_article,
               'is_logo_display': is_logo_display}

    return render(request, 'index.html', context)


#Une fonction qui rend le sous-menu dynamique

def list_sous_menu(request, pk):
    application = Application.objects.all().first()
    menu_element = Menu_element.objects.all()
    sous_menu = Sous_menu.objects.all()
    block_article = Block_article.objects.all()

    is_logo_display = True

    menu_element_selected = Menu_element.objects.get(id=pk)
    sous_menu_list = menu_element_selected.sous_menu_set.all()
    context = {'application': application, 'menu_element': menu_element, 'sous_menu': sous_menu,
               'block_article': block_article, 'sous_menu_list': sous_menu_list, 'menu_element_selected': menu_element_selected,
               'is_logo_display': is_logo_display}

    return render(request, 'index.html', context)

#Une fonction qui rend les articles dynamiques

def list_articles(request, pk):
    application = Application.objects.all().first()
    menu_element = Menu_element.objects.all()
    sous_menu = Sous_menu.objects.all()
    block_article = Block_article.objects.all()

    sous_menu_element_selected = Sous_menu.objects.get(id=pk)

    sous_menu_element_selected_sraping_type = sous_menu_element_selected.scraping_type

    block_scraping_list = []
    if sous_menu_element_selected_sraping_type == 'youtube':
        block_scraping_list = youtubeScraping.get_youtube_videos_list(sous_menu_element_selected.scraping_link)
    elif sous_menu_element_selected_sraping_type == 'youtube_playlist':
        block_scraping_list = youtube_playlists_scrapping.get_youtube_videos_list(sous_menu_element_selected.scraping_link)
    elif sous_menu_element_selected_sraping_type == 'facebook':
        block_scraping_list = face_book.get_facebook_link(sous_menu_element_selected.scraping_link)
    elif sous_menu_element_selected_sraping_type == 'instagram':
        block_scraping_list = scrapping_instagram.get_instagram_hashtags_list(sous_menu_element_selected.scraping_link)





    block_article_list = sous_menu_element_selected.block_article_set.all()

    menu_element_selected = Menu_element.objects.get(id=sous_menu_element_selected.menu_element.id)
    sous_menu_list = menu_element_selected.sous_menu_set.all()

    context = {'application': application, 'menu_element': menu_element, 'sous_menu': sous_menu,
               'block_article': block_article,'menu_element_selected': menu_element_selected, 'sous_menu_list': sous_menu_list,
                'block_article_list': block_article_list, 'sous_menu_element_selected': sous_menu_element_selected,
               'block_scraping_list': block_scraping_list, 'sous_menu_element_selected_sraping_type': sous_menu_element_selected_sraping_type}

    return render(request, 'index.html', context)
