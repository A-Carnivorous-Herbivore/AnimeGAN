import requests
from bs4 import BeautifulSoup
url = 'https://wall.alphacoders.com/by_sub_category.php?id=237089&name=Your+Lie+in+April+Wallpapers'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
images = soup.find_all('img')
#images = soup.findAll('img',{"src":True})
print(images)
name = range(0,1000)
i = 0
num = 30
for image in images:
    if i >= 3 and i%2 == 0:
        #name = image['alt']
        link = image['src']
        with open(str(num), 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            num = num + 1
    i = i + 1
'''def returnHTML(url):
    html = requests.get(url).content
    return html

def getImg(html):
    soup = BeautifulSoup(html,"html.parser")
    #items = soup.find_all(attrs= {"class":"thumb section--two__search-grid__single-photo__thumb"})
    items  = soup.find_all(attrs= {"class":"hide-featured-badge hide-favorite-badge"})
    print(len(items))
    for item in items:
        img = item.find("img")
        url=img.get("src")
        name=img.get("alt")
        content=requests.get(url).content
        with open(name,"wb") as file:
                file.write(content)
                print("Downloading"+name)

'''
'''def getImg(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('img')
    for index, item in enumerate(items):
        #img = item.find("img")
        #url = img.get("src")
        #name = img.get("alt")
        html = requests.get(item.get('src'))
        name = str(index) + 'png'
        with open(name, "wb") as file:
            file.write(html.content)
            print("Downloading" + name)
url="https://gratisography.com"
url = "https://www.pexels.com/search/anime/"
html=returnHTML(url)
getImg(html)'''
