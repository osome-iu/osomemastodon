import requests

# Specify your Mastodon instance URL and access token
instance_url = 'https://defcon.social'
access_token = 'edGLOqcYXd9GjBQaDKM2qrkmy1T145WOovgixfFhv7w'

# Specify the keyword you want to search for
keyword = 'books'

# Make the API request
api_url = f'{instance_url}/api/v2/search?q={keyword}'
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get(api_url, headers=headers)

print(response.status_code)

# Handle the API response
if response.status_code == 200:
    data = response.json()
    print(data)  # Print the entire response JSON
    results = data.get('statuses', [])
    print(results)  # Print the contents of the results list
    for result in results:
        print(result['content'])
else:
    print(f'Error: {response.status_code}')