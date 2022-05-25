#pip install selenium
#pip install bs4
#pip install lxml
from bs4 import BeautifulSoup
from selenium import webdriver

marketplace_link ='https://web.facebook.com/marketplace/category/electronics'
def get_facebook_link(marketplace_link):
    list = []
    driver = webdriver.Chrome('C:/Users/user/Desktop/S6/internship/cnrst/chromedriver')
    driver.get(marketplace_link.format())
    driver.implicitly_wait(5)
    #driver.find_element_by_css_selector('div[aria-label=\"Tout accepter\"]').click()
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    list=[]
    name_box1 = soup.find_all("div", class_='sonix8o1')
    j = 0
    for val in name_box1:
        links = driver.find_elements_by_tag_name('img')

        #links = [link.get_attribute('src') for link in links]

        a = val.findChild("span").findChildren("span")
        try:
            price = a[1].contents[0]
            name = a[4].contents[0]
            adr = a[7].contents[0]
            #print(price, '|', name, '|', adr)

        except:
            continue

        info = {
            "price": price,
            "name": name,
            "adr": adr,
            "src": links[j].get_attribute('src')
        }
        list.append(info)
        j+=1

    return list

    driver.quit()

"""
for element in get_facebook_link(marketplace_link):
    print(element)
"""
