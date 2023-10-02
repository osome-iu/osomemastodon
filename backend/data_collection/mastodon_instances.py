import requests, os,json


url = "https://instances.social/api/1.0/instances/list?&count=2000&sort_by=statuses&sort_order=desc"
payload = {}
headers = {
    'Authorization': 'Bearer ' + '8SAlkWdVLh7lolap93JKgfVn0kHl0EUCGkZBw8UGDZ6iEVrFqwwDoR3eDgSy1vAdvA4rRejBqic9HiifpxsFnPaBJAn0n6xbACGzGH09Zo3iqRuavAKUHLWDM3a9iukb'
}
response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()