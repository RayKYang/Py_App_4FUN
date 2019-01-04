__author__ = 'rkzyang'

import requests

request = requests.get("https://www.amazon.com/AmazonBasics-High-Back-Executive-Chair-Black/dp/B00XBC3BF0/ref=sr_1_1_sspa?ie=UTF8&qid=1544059572&sr=8-1-spons&keywords=chair&psc=1")
content = request.content

from bs4 import BeautifulSoup
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_ourprice", "class": "a-size-medium a-color-price"}) # inspect the element of the price on the webpage
string_price = element.text.strip()

price = float(string_price[1:])

if price < 100:
    print("Buy it")
    print("The Price is {}".format(price))
else:
    print("Don't Buy")
    print("The Price is {}".format(price))

# compare code at: https://github.com/schoolofcode-me/whats_a_browser