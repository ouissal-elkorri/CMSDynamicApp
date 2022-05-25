from bs4 import BeautifulSoup
from selenium import webdriver

selected_chaine_youtube = 'https://www.youtube.com/c/ButtonPoetry/playlists'

def get_youtube_videos_list(selected_chaine_youtube):
    driver = webdriver.Chrome('C:/Users/user/Desktop/S6/internship/cnrst/chromedriver')

    List_videos = []

    driver.get(selected_chaine_youtube.format())
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    driver.quit()
    titles = soup.findAll('a', id='video-title')
    #update = soup.findAll('span', class_='style-scope ytd-video-meta-block')
    video_urls = soup.findAll('a', id="video-title")

    i = 0
    j = 0
    for title in titles:
        video_urls_str = str(format(video_urls[j].get('href')))
        video_id = video_urls_str[video_urls_str.find('v=') + 2:video_urls_str.find('&list')]
        info = {
            "title": title.text,
            #"updates": update[i].text,
            "Link": 'https://www.youtube.com{}'.format(video_urls[j].get('href')),
            "id": 'https://www.youtube.com/embed/{}'.format(video_id)

        }
        List_videos.append(info)
        i += 2
        j += 1


    return List_videos

"""
for element in get_youtube_videos_list(selected_chaine_youtube):
    print(element)
"""



