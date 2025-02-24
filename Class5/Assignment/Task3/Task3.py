import os
import re
import requests
from bs4 import BeautifulSoup

class ArticleScraper:
    def __init__(self, base_path="Class5/Assignment/Task3", search_terms=None):
        self.base_url = "https://finance.yahoo.com"
        self.news_url = "https://finance.yahoo.com/topic/stock-market-news/"
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.search_terms = search_terms if search_terms else ["Apple", "Nvidia"]
        
        # Set up the base path and articles directory
        self.base_path = base_path
        self.articles_dir = os.path.join(self.base_path, "articles")
        os.makedirs(self.articles_dir, exist_ok=True)

    def fetch_page(self, url):
        """Fetch the HTML content of a given URL."""
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to retrieve page at {url}. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching page {url}: {e}")
            return None

    def get_article_list(self):
        """Get the list of article elements from the main news page."""
        html_content = self.fetch_page(self.news_url)
        if not html_content:
            return []
        soup = BeautifulSoup(html_content, "html.parser")
        articles = soup.find_all("li", class_="stream-item story-item yf-1usaaz9")
        return articles

    def process_article(self, article):
        """Process a single article element, extract details, and save to file."""
        # Extract the title and link from the article element
        title_element = article.find("h3")
        title = title_element.text.strip() if title_element else "No Title"
        a_tag = article.find("a")
        link = a_tag["href"] if a_tag and "href" in a_tag.attrs else None
        if not link:
            return

        # Convert relative links to absolute URLs
        if not link.startswith("http"):
            link = self.base_url + link

        # Check if the title contains any of the search terms
        if not any(term.lower() in title.lower() for term in self.search_terms):
            return

        print(f"Title: {title}")
        print(f"Link: {link}")
        print("-" * 50)

        # Open the article link and parse its content
        article_html = self.fetch_page(link)
        if not article_html:
            return

        article_soup = BeautifulSoup(article_html, "html.parser")

        # Fetch the author name
        author_div = article_soup.find("div", class_="byline-attr-author yf-1k5w6kz")
        author = author_div.text.strip() if author_div else "Author not found"

        # Fetch the publication date and time from the <time> tag
        time_tag = article_soup.find("time", class_="byline-attr-meta-time")
        datetime_attr = time_tag["datetime"] if time_tag and "datetime" in time_tag.attrs else None
        date_time_text = time_tag.text.strip() if time_tag else "Date/Time not found"
        # Extract only the date (YYYY-MM-DD)
        date_only = datetime_attr.split("T")[0] if datetime_attr else "unknown_date"

        # Create a subdirectory for the specific date inside the articles directory
        date_dir = os.path.join(self.articles_dir, date_only)
        os.makedirs(date_dir, exist_ok=True)

        # Fetch the full article text from all <p> tags with the specified class
        paragraphs = article_soup.find_all("p", class_="yf-1pe5jgt")
        article_text = "\n\n".join(p.text.strip() for p in paragraphs if p.text.strip())
        if not article_text:
            article_text = "Article content not found."

        # Sanitize the title to create a valid filename
        filename = re.sub(r'[\\/*?:"<>|]', "", title) + ".txt"
        file_path = os.path.join(date_dir, filename)

        # Save the extracted content to a text file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"Title: {title}\n")
            file.write(f"Link: {link}\n")
            file.write(f"Author: {author}\n")
            file.write(f"DateTime (attribute): {datetime_attr}\n")
            file.write(f"DateTime (text): {date_time_text}\n")
            file.write("\nArticle Content:\n")
            file.write(article_text)

        print(f"Saved article to {file_path}")

    def run(self):
        """Fetch and process articles from the main news page."""
        articles = self.get_article_list()
        for article in articles:
            self.process_article(article)


if __name__ == "__main__":
    scraper = ArticleScraper(search_terms=["Apple", "Nvidia"])
    scraper.run()
