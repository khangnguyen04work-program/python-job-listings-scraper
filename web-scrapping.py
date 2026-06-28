from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://realpython.github.io/fake-jobs/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

job_title = soup.find_all("h2", attrs={"class": "title is-5"})
company = soup.find_all("h3", attrs={"class": "subtitle is-6 company"})
location = soup.find_all("p", attrs={"class": "location"})
job_detail_page_URL = soup.find_all("a", attrs={"href": True})

file = open("job_listings.csv", "w")
writer = csv.writer(file)
writer.writerow(["Job Title", "Company", "Location", "Detail Page URL"])


for job in zip(job_title, company, location, job_detail_page_URL):
    writer.writerow([job[0].text, job[1].text, job[2].text, job[3].get('href')])
    print(f"Job Title: {job[0].text}")
    print(f"Company: {job[1].text}")
    print(f"Location: {job[2].text}")
    print(f"Detail Page URL: {job[3].get('href')}")
    print(f"\n--------------------------------\n")

file.close()
