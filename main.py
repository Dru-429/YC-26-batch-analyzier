import requests
import os
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import json 

load_dotenv()

api_key = os.getenv("API_KEY")
url = "https://45bwzj1sgc-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser%3B%20JS%20Helper%20(3.16.1)&x-algolia-application-id=45BWZJ1SGC&x-algolia-api-key=NzllNTY5MzJiZGM2OTY2ZTQwMDEzOTNhYWZiZGRjODlhYzVkNjBmOGRjNzJiMWM4ZTU0ZDlhYTZjOTJiMjlhMWFuYWx5dGljc1RhZ3M9eWNkYyZyZXN0cmljdEluZGljZXM9WUNDb21wYW55X3Byb2R1Y3Rpb24lMkNZQ0NvbXBhbnlfQnlfTGF1bmNoX0RhdGVfcHJvZHVjdGlvbiZ0YWdGaWx0ZXJzPSU1QiUyMnljZGNfcHVibGljJTIyJTVE"

headers = {
  "X-Algolia-Application-Id": "45BWZJ1SGC",
  "X-Algolia-API-Key": api_key,
  "Content-Type": "application/json",
}

payload = {
  "requests": [
    {"indexName": "YCCompany_production", 
      "params":"facetFilters=%5B%5B%22batch%3AFall%202026%22%2C%22batch%3ASpring%202026%22%2C%22batch%3ASummer%202026%22%2C%22batch%3AWinter%202026%22%5D%5D&facets=%5B%22app_answers%22%2C%22app_video_public%22%2C%22batch%22%2C%22demo_day_video_public%22%2C%22industries%22%2C%22isHiring%22%2C%22nonprofit%22%2C%22question_answers%22%2C%22regions%22%2C%22subindustry%22%2C%22top_company%22%5D&hitsPerPage=1000&maxValuesPerFacet=1000&page=0&query=&tagFilters="
    }    
  ]
}

response = requests.post(
  url,
  headers=headers,
  json=payload
)

print(response.status_code)
# print(response.json())

data = response.json()
companies = data['results'][0]['hits']
json_companies  = json.dumps(companies, indent=4)

req_data = {}

for company in companies:
  data = {
    "id": company["id"],
    "name": company["name"],
    "one_liner" : company["one_liner"],
    "locations": company["all_locations"],
    "team_size": company["team_size"],
    "tags": company["tags"],
    "industries": company["industries"],
  }
  req_data[company["id"]] = data

with open('reqCompaniesData.json', 'w') as file:
  json.dump(req_data, file, indent=4)

print("Succesfullt required data flitered and saved")
print( f"Total no.of comapany in all batches of 2025 ar ${len(companies)}")



# # this will won't work as IN Next js base website the work on pumping data to the
# # frontend and not render the data itself, making it hard to scrape as that didn't exits at call
# # in this type of website we need to use selemiun( like puppeteer) or json api if exits and hence we don't needuse BS4 
# soup = BeautifulSoup(response.text, "html.parser")
# companies = soup.find_all("a")


# for company in companies:
#     href = company.get("href")
#     if href and "/companies/" in href:
#         print(href)

# print(soup.prettify)
