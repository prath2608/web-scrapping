import requests
from bs4 import BeautifulSoup
import csv

def scrape_amazon_books():
    # URL of the Amazon Best Sellers page for Books
    url = 'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books'
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract product information
        products = []
        for item in soup.find_all('div', class_='zg-item-immersion'):
            name = item.find('div', class_='p13n-sc-truncated').text.strip()
            price = item.find('span', class_='p13n-sc-price').text.strip()
            rating = item.find('span', class_='a-icon-alt').text.strip()
            products.append({'Name': name, 'Price': price, 'Rating': rating})
        
        # Write the product information to a CSV file
        with open('amazon_books.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Price', 'Rating'])
            writer.writeheader()
            writer.writerows(products)
        
        print("Product information scraped successfully and saved to 'amazon_books.csv'.")
    else:
        print("Failed to retrieve data from Amazon.")

# Example usage:
if __name__ == "__main__":
    scrape_amazon_books()
