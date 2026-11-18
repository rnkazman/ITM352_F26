# Scrape names of ITM faculty and grad students
import urllib.request
from bs4 import BeautifulSoup

itm_url = "https://shidler.hawaii.edu/itm/people"
print("Retrieving", itm_url)

itm_page = urllib.request.urlopen(itm_url)
itm_names = []

soup = BeautifulSoup(itm_page, "html.parser")
# Find all the faculty, which are in h2 tags with class="title"
faculty = soup.find_all("h2", class_="title")

for person in faculty:
    itm_names.append(person.text)
    print("Faculty:", person.text)

print("Total Faculty:", len(faculty))

