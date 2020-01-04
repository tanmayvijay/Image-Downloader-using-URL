import requests
from bs4 import BeautifulSoup
import shutil

URL = "https://www.pexels.com/search/quotes/"

response = requests.get(URL)

bs = BeautifulSoup(response.text, 'html.parser')
formatted_text = bs.prettify()

list_imgs = bs.find_all('img')

no_of_imgs = len(list_imgs)
list_as = bs.find_all('a')
no_of_as = len(list_as)

j = 1
for img_tag in list_imgs:
    try:
        img_link = img_tag.get('src')
        ext = img_link[img_link.rindex('.'):]
        ext = ext[:4]
        filen = str(j) + ext
        res = requests.get(img_link, stream=True)

        with open(filen, 'wb') as file:
            shutil.copyfileobj(res.raw, file)
    
    except Exception as e:
        print(e)
    
    j +=1

            