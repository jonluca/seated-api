import json
import pandas
restaurants = json.loads(open("restaurants.json").read())
print(len(restaurants))

reward = 'maxReward'


def by_discount(elem):
  return elem[reward]
restaurants.sort(key=by_discount, reverse=True)

discount_group = pandas.DataFrame(restaurants).groupby(reward).groups
print("Discount distribution")
for k, v in discount_group.items():
  print(f"{k}: {len(v)}")

print("Top discount restaurants")
for i in range(10):
  name = restaurants[i]['name']
  print(f"{name}: {restaurants[i][reward]}%")

for r in restaurants:
  if 'Boulton' in r['name']:
    print(r)