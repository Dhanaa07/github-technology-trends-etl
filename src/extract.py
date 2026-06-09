import requests
import json
from pathlib import Path

# Create data/raw folder if it doesn't exist
#here i already created the data/raw folder, so i can save the raw json file there.

Path("data/raw").mkdir(parents=True, exist_ok=True)

# GitHub Search API endpoint
# Used to search repositories based on filters
url = "https://api.github.com/search/repositories"

#query parameters for the API request
#parameters allow us to specify the search criteria, sorting, and pagination for the results we want to retrieve from the GitHub API instead of retrieving all.
params = {

    #search for repositories created after May 1, 2026
    "q": "created:>2026-05-01",

    #sort results by stars in descending order
    "sort": "stars",

    #sort order: descending
    "order": "desc",

    #number of results per page (max 100)
    "per_page": 200
}

#Send GET request to GitHub API with the specified parameters
response = requests.get(url, params=params)

#HTTP status code refers whether the request was successful (200) or if there was an error (e.g., 404, 500)
print("Status Code:", response.status_code)

if response.status_code == 200:
    #Parse the JSON response from the API into a Python dictionary
    data = response.json()

    #Save the raw JSON data into a file named github_repos_raw.json in the data/raw directory
    with open(
        "data/raw/github_repos_raw.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(data, f, indent=4)

    print("Raw JSON saved successfully!")
    print("Total matches:", data["total_count"])
    print("Repos returned:", len(data["items"]))

else:
    print("API request failed")