import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL = "https://finance.yahoo.com/topic/stock-market-news/"
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

# books_data = get_books(URL)
# df = pd.DataFrame(books_data)
# df.to_csv("books.csv", index=False)
# print("Data saved to books.csv")

url = "https://finance.yahoo.com/topic/stock-market-news/"

# Define the search terms (Apple, NVIDIA, QUALCOMM)
search_terms = ["Apple", "NVIDIA", "QUALCOMM"]

# Send a GET request to the Yahoo Finance News page
response = requests.get(url, headers=HEADERS)

if response.status_code != 200:
    print("Failed to retrieve the page. Status code:", response.status_code)
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all news articles on the page
articles = soup.find_all("li", class_="stream-item story-item yf-1usaaz9")

# Filter and print articles related to Apple, NVIDIA, or QUALCOMM
for article in articles:
    title = article.find("h3").text.strip() if article.find("h3") else "No Title"
    link = article.find("a")["href"] if article.find("a") else "No Link"

    print(title)
    print(link)
    print("-" * 50)
    
    # # Check if the title contains any of the search terms
    # if any(term.lower() in title.lower() for term in search_terms):
    #     print(f"Title: {title}")
    #     print(f"Link: {link}")
    #     print("-" * 50)