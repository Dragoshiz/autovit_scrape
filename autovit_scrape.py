from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('autovit_cars.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Source','Name', 'Year', 'Mileage', 'Engine', 'Fuel type', 'Price', 'U.R.L'])

page = 1 
while page <= 500:
    base_link = requests.get('https://www.autovit.ro/autoturisme/?search%5Border%5D=created_at%3Adesc&page={}'.format(page)).text
    soup = BeautifulSoup(base_link, 'lxml')

    for article in soup.find_all('article'):
        
        cars = {}
        try:
            cars['name'] = article.h2.a.text.strip()
            cars['year'] = article.find('li', {'data-code':'year'}).span.text
            cars['mileage'] = article.find('li', {'data-code':'mileage'}).span.text
            cars['engine'] = article.find('li', {'data-code':'engine_capacity'}).span.text
            cars['fuel type'] = article.find('li', {'data-code':'fuel_type'}).span.text
            cars['price'] = article.find('span', class_='offer-price__number ds-price-number').span.text
            cars['U.R.L'] = article.find('a')['href']
        except Exception :
            cars['year']= ''
            cars['mileage'] = ''
            cars['engine'] = ''
            cars['fuel type'] =''
            cars['price'] = ''
            cars['U.R.L'] = ''
        print(cars)
        csv_writer.writerow(['Autovit',cars['name'],cars['year'],cars['mileage'],cars['engine'],cars['fuel type'],cars['price'],cars['U.R.L']])
    page = page + 1
    
csv_file.close()
       
