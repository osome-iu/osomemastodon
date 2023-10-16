import requests, os,json
from bs4 import BeautifulSoup
import pandas as pd
import json

# URL of the website you want to scrape
url = "https://instances.social/list/old"
file_name = '/Users/pkamburu/iuni/mastodon/instance_data/2023_09_25.json'
json_data_list = []


response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')

    rows = []
    headers = []

    # Extract table headers
    for header in table.find_all('th'):
        headers.append(header.text.strip())

    for row in table.find_all('tr')[1:]:
        row_data = [cell.text.strip() for cell in row.find_all('td')]
        rows.append(row_data)

    for row in rows:
        mastodon_instance_info ={
            'score' : row[1],
            'instance' : row[2],
            'version' : row[3],
            'users': row[4],
            'statuses': row[5],
            'connections': row[6],
            'registrations': row[7],
            'uptime': row[8],
            'https': row[9],
            'obs': row[10],
            'ipv6': row[11]
        }

        os.makedirs(os.path.dirname(file_name), exist_ok=True)

        with open(file_name, 'a') as file:
            json.dump(mastodon_instance_info, file, default=str)
            file.write('\n')

    with open(file_name, 'r') as json_file:
        for line in json_file:
            json_data = json.loads(line)
            json_data_list.append(json_data)

    df = pd.DataFrame(json_data_list)
    df.to_csv('/Users/pkamburu/iuni/mastodon/instance_data/instance_data_2023_09_25.csv', index=False)

else:
    print("Failed to retrieve the web page. Status code:", response.status_code)