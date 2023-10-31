import requests
import time
from bs4 import BeautifulSoup

print("List of Foods")
print("_______________________________________")

html_text= requests.get("https://saumik235.pythonanywhere.com/").text
soup=  BeautifulSoup(html_text,'lxml')
foods=soup.find_all('div' , class_='col-lg-3 col-md-6 col-sm-12 pb-1')

# print(foods,'\n')


for food in foods:
    F_name_tag = food.find('h6', class_='text-truncate mb-3')
    if F_name_tag:
        F_name = F_name_tag.text.strip()
    else:
        F_name = "Food name not available"
    
    price_div = food.find('div', class_='d-flex justify-content-center')
    if price_div and price_div.find('h6'):
        price = price_div.find('h6').text.strip()
    else:
        price = "Price not available"

    link_div = food.find('div', class_='card-footer d-flex justify-content-between bg-light border')
    if link_div and link_div.find('a'):
        link = link_div.a['href']
    else:
        link = "link not available"

    print(f'''Food Name: {F_name}
Price: {price}
Details: {link}
''')
