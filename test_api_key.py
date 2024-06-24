import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWSAPI_API_KEY")


API_KEY = os.getenv("NEWSAPI_API_KEY")
url = "https://newsapi.org/v2/top-headlines?country=ar"

headers = {
    "X-Api-Key": API_KEY
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("API Key is correctly configured and working!")
    data = response.json()
    print(f"Total results: {data['totalResults']}")
else:
    print(f"Failed to authenticate with the API: Status code {response.status_code}")
    print(f"Response: {response.text}")
    exit(1)
