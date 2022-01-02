import json

restaurants = json.loads(open("restaurants.json").read())
print(len(restaurants))
