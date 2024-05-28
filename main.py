
from bs4 import BeautifulSoup
import requests

nike_mens_shoes = "https://www.nike.com/w/mens-shoes-nik1zy7ok?sort=newest"
nike_womens_shoes = "https://www.nike.com/w/womens-shoes-5e1x6zy7ok?sort=newest"
nike_kids_shoes = "https://www.nike.com/w/kids-shoes-v4dhzy7ok?sort=newest"

response = requests.get(nike_mens_shoes)

soup = BeautifulSoup(response.text, "html.parser")

product_cards = soup.find_all("div", class_="product-card")
product_info_list = []

for card in product_cards:
	link = card.find("a", class_="product-card__link-overlay")["href"]
	title = card.find("div", class_="product-card__title").text.strip()
	product_info_list.append({"title": title, "link":link})

for product_info in product_info_list:
	print(product_info)
