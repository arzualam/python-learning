import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print(json)

# How to get the list of people alone from this output

for person in json['people']:
    print(person)
 #also only print the name
    print(person['name'])