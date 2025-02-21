import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://readings.com.pk/sub-menu/new-releases/R"
HEADERS = {"User-Agent": "Mozilla/5.0"}
def get_books(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("div", class_="product-dtl")

    print(books)
    book_list = []

    for book in books:
        title = book.div["title"]
        price = book.find("p", class_="price_color").text
        stock = book.find("p", class_="instock availability").text.strip()
        book_list.append({"Title": title, "Price": price, "Availability": stock})

    return book_list

books_data = get_books(URL)
df = pd.DataFrame(books_data)
df.to_csv("books.csv", index=False)
print("Data saved to books.csv")