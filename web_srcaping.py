from bs4 import BeautifulSoup

with open("index.html",'r') as file:
     content= file.read()

     soup= BeautifulSoup(content, 'lxml')
     tags=soup.find_all('h5')
     course=soup.find_all('div', class_='card')

     for cr in course:  
        cr_name=cr.h5.text
        cr_price=cr.p.text.split()[-1]
        print(f"{cr_name} cost {cr_price}")