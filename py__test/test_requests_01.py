#!/usr/bin/python3

import requests

# Führt einen API-Aufruf durch und speichert die Antwort.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

print(f"Status code: {r.status_code}")

# Speichert die API-Antwort in einer Variablen.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Gibt Informationen über die Repositories aus.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Untersucht das erste Repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
