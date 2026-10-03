import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser") #soup now contains html of that website

books = soup.find_all("article", class_="product_pod")
print(f"Found {len(books)} books on this page!")

data = []
for book in books:
    price = book.find("p", class_="price_color")
    price_text = price.text[1:]
    price_text = float(price.text.replace("Â", "").replace("£", "")) #clean price
    book_name = book.find("h3").find("a")["title"]
    data.append({"Title": book_name, "Price": price_text})

df = pd.DataFrame(data)
df["Price"] = df["Price"].astype(float)
print(df)

df.to_csv("books.csv", index=False)
print("SUCESS!")