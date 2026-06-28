## Python Job Listings Scraper

A beginner web scraping project that collects job listings from the 
[Fake Python Jobs](https://realpython.github.io/fake-jobs/) website 
and exports them to a CSV file.

## What It Does
- Scrapes job title, company name, location, and job detail URL
- Saves all listings to a structured CSV file

## How to Run
1. Clone the repo
2. Install dependencies:
   pip install requests beautifulsoup4
3. Run the scraper:
   python web-scrapping.py

## Output
Generates a CSV file with columns: Job Title, Company, Location, URL

## Built With
- Python
- Requests
- BeautifulSoup4 (bs4)

## What I Learned
How to parse HTML structure, extract specific elements with BeautifulSoup, 
and handle real-world data with Python.

---
Project inspired by [roadmap.sh](https://roadmap.sh/projects/job-listings-scraper)