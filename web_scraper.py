import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.youtube.com/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the website
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the data you want to scrape
    data = soup.find('div', {'id': 'data'})

    # Write the data to a file
    with open('data.txt', 'w') as file:
        file.write(str(data))

else:
    print("Failed to fetch the data. Response code:", response.status_code)
