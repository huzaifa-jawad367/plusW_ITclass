import yfinance as yf
import sqlite3
import pandas as pd
import time
from yfinance.exceptions import YFRateLimitError

class StockScraper:
    def __init__(self, companies, period="5y", db_name="stock_data.db", max_retries=3, retry_delay=5):
        """
        Initialize the StockScraper with company data and SQLite configuration.

        :param companies: Dictionary mapping company names to ticker symbols.
        :param period: Historical data period to fetch (default is "5y").
        :param db_name: Name of the SQLite database file.
        :param max_retries: Maximum number of retries on rate limit error.
        :param retry_delay: Delay in seconds between retries.
        """
        self.companies = companies
        self.period = period
        self.db_name = db_name
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def fetch_stock_data(self, company, ticker):
        """
        Fetch historical stock data for a given company using yfinance,
        with retry logic on YFRateLimitError.

        :param company: Name of the company.
        :param ticker: Ticker symbol of the company.
        :return: DataFrame containing the historical data or None if unavailable.
        """
        print(f"Fetching data for {company} ({ticker})...")
        stock = yf.Ticker(ticker)
        attempts = 0
        data = None

        while attempts < self.max_retries:
            try:
                data = stock.history(period=self.period)
                break  # Exit loop if successful.
            except YFRateLimitError:
                attempts += 1
                print(f"Rate limit error for {company} ({ticker}). Retrying in {self.retry_delay} seconds... (Attempt {attempts}/{self.max_retries})")
                time.sleep(self.retry_delay)

        if data is None or data.empty:
            print(f"No data available for {company} ({ticker}) after {attempts} attempt(s).")
            return None

        data.reset_index(inplace=True)
        data["Company"] = company
        data["Ticker"] = ticker
        return data

    def save_to_sqlite(self, data, table_name="stocks"):
        """
        Save the DataFrame to an SQLite database.

        :param data: DataFrame containing the historical data.
        :param table_name: Name of the table where data will be stored.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                data.to_sql(table_name, conn, if_exists="append", index=False)
                print(f"Data saved to SQLite table '{table_name}'.")
        except Exception as e:
            print(f"Error saving data to SQLite: {e}")

    def scrape(self):
        """
        Fetch data for each company and save the records into SQLite.
        """
        for company, ticker in self.companies.items():
            data = self.fetch_stock_data(company, ticker)
            if data is not None:
                self.save_to_sqlite(data)
        print("Scraping complete.")

if __name__ == "__main__":
    # Define the companies and their ticker symbols.
    companies = {
        "NVIDIA": "NVDA",
        "QUALCOMM": "QCOM",
        "APPLE": "AAPL",
        "GOOGLE": "GOOGL",
        "FACEBOOK": "META",  # Facebook is now Meta Platforms.
        "MICROSOFT": "MSFT",
        "AMAZON": "AMZN"
    }
    
    # Create an instance of the scraper and run it.
    scraper = StockScraper(companies)
    scraper.scrape()
