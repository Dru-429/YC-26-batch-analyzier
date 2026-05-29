import requests
import pandas as pd 
import matplotlib.pyplot as plt
from bs4 import BeatifulSoup

url = "https://www.ycombinator.com/companies?batch=Winter%202027&batch=Winter%202026&batch=Spring%202026&batch=Summer%202026&batch=Fall%202026"

response = requests.get(url)

print(response.status_code)
