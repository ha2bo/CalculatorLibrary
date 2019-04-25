import urllib
from bs4 import BeautifulSoup
import string


'''Codigo Hombre 93427
Codigo Mujer 3034

Brand = Marca de Zapato

Tamanho zapato hombre = US%2520Shoe%2520Size%2520%2528Men%2527s%2529
Tamanho zapato mujer = US%2520Shoe%2520Size%2520%2528Women%2527s%2529

sop=16&_sop=15 Ascendente
sop=16&_sop=16 Descendente

hola = [1, "hola"]
print(str(hola[0])+"hello")

'''

webpage = "https://www.ebay.com"
male_size = "/sch/93427/i.html?_from=R40&US%2520Shoe%2520Size%2520%2528Men%2527s%2529=" 
female_size= "/sch/3034/i.html?_from=R40&US%2520Shoe%2520Size%2520%2528Women%2527s%2529="
shoe_size = "10"
price_ascendant = "&sop=16&_sop=15"
shoe_brand ="_&Brand=PUMA"

url = webpage + male_size + shoe_size+ price_ascendant + shoe_brand

print(url)