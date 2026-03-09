# Amazon Product Scraper

Python web scraper built with Scrapy that extracts product data from Amazon search results.

## Features

- Extract product title
- Extract product price
- Extract original price
- Extract rating
- Extract number of reviews
- Extract stock availability

## Technologies

- Python
- Scrapy
- Web Scraping
- Data Extraction

## Usage

Run the scraper:

scrapy crawl amazon -a search="gaming mouse" -a pages=2

## Output

The scraper exports the data to:

- amazon_products.csv
- amazon_products.json

## Example Data

| Title | Price | Rating | Reviews |
|------|------|------|------|
| Gaming Mouse RGB | $29.99 | 4.5 | 2300 |

## Use Cases

- Product research
- Competitor analysis
- Price monitoring
- Market research
