"""
Les bibliothèques utilisés:
#pip install selenium
#pip install bs4
#pip install lxml

# Le module selenium.webdriver fournit toutes les implémentations de WebDriver.
# Les implémentations WebDriver actuellement prises en charge sont Firefox, Chrome, IE et Remote.
"""

from bs4 import BeautifulSoup
from selenium import webdriver

def get_youtube_videos_list(selected_chaine_youtube):
    # Ensuite, l'instance de Chrome WebDriver est créée.
    driver = webdriver.Chrome('C:/Users/user/Desktop/S6/internship/cnrst/chromedriver')
    List_videos = []

    # La méthode driver.get naviguera vers une page donnée par l'URL.
    # WebDriver attendra que la page soit complètement chargée (c'est-à-dire que l'événement
    # "onload" se soit déclenché) avant de rendre le contrôle à votre test ou script.
    driver.get(selected_chaine_youtube.format())

    # tout le contenu de la page sera encodé puis dépouillé puis stocké dans une variable appelée "content"
    content = driver.page_source.encode('utf-8').strip()

    # maintenant nous allons faire de ce contenu dans un objet de BeautifulSoup
    # et il prend comme paramètres le contenu et lxml qui est l'analyseur,
    # donc bs4 pourrait analyser le contenu
    soup = BeautifulSoup(content, 'lxml')
    driver.quit()

    # Utilisant BeautifulSoup pour stocker le titre de cette page dans une variable appelée titles
    # nous passons la balise a à la méthode findall donc pour toutes les balises a sur la page où l'identifiant est le titre de la vidéo,
    # leurs titres seront récupérés
    titles = soup.findAll('a', id='video-title')
    views = soup.findAll('span', class_='style-scope ytd-grid-video-renderer')
    video_urls = soup.findAll('a', id="video-title")

    i = 0  # views and period
    j = 0  # urls
    for title in titles:
        info = {
            # nous avons appelé .text sur ceux-ci pour obtenir la chaîne
            "title": title.text,
            "Views": views[i].text,
            "Period": views[i + 1].text,
            # ici, nous extrayons également l'attribut 'href' des liens avec leur texte.
            "Link": 'https://www.youtube.com{}'.format(video_urls[j].get('href'))

        }
        # nous avons déjà créé une liste appelée List_videos, où nos dicts seront stockés
        List_videos.append(info)
        i += 2
        j += 1

    return List_videos

"""
selected_chaine_youtube = 'https://www.youtube.com/channel/UCqet7gjqhl6cVJdntCcq1EA/videos'

for element in get_youtube_videos_list(selected_chaine_youtube):
    #cela imprimera tous nos dicts
    print(element)
"""
