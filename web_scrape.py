from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "lxml")
quotes = soup.find_all("span", attrs={"class":"text"})
authors = soup.find_all("small", attrs={"class":"author"})

file = open("scraped_quotes.csv", "w", encoding='utf-8')
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])

for quote, author in zip(quotes, authors):
    print(quote.text + " - By: " + author.text)
    writer.writerow([quote.text, author.text])

file.close()
