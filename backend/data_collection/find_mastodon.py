import json

file_name = '/Users/pkamburu/iuni/mastodon/data-scp/mastodon.social_2023-10-02.json'
trump_count = 0

with open(file_name, 'r') as json_file:
    for line in json_file:
        json_data = json.loads(line)

        # Check if the word 'trump' is present in any field of the record
        if any('nba' in str(value).lower() for value in json_data.values()):
            trump_count += 1
            print(json_data)

print(f"Number of records containing 'trump': {trump_count}")