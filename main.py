import requests
import json
import os

headers = {
  'Host': 'api.seatedapp.io',
  'Content-Type': 'application/json',
  'Flavor': 'native_app_v1',
  'Accept': '*/*',
  'Authorization': f"Bearer {os.environ.get('BEARER_TOKEN')}",
  'Accept-Language': 'en-US,en;q=0.9',
  'Accept-Encoding': 'gzip, deflate',
  'Platform': 'ios',
  'User-Agent': 'Seated/1075 CFNetwork/1327.0.4 Darwin/21.2.0',
  'Device': '?unrecognized?',
  'Build': '1075',
}


def get_params_from_page(page=1):
  return (
    ('city', '2'),
    ('isRemoveFutureWalkInVariant', 'false'),
    ('latitude', '40.71'),
    ('longitude', '-73.98'),
    ('mapLatitude', '40.71'),
    ('mapLongitude', '-73.99'),
    ('page', str(page)),
    ('size', '400'),
    ('slotForDate', '2022-01-02T18:30:00.000Z'),
  )


restaurants = []
page = 1
while True:
  params = get_params_from_page(page)
  response = requests.get('https://api.seatedapp.io/v2/search/map/dinein', headers=headers, params=params)
  data = response.json()
  if 'restaurants' in data:
    restaurants += data['restaurants']
  else:
    print("Something went wrong")
  if 'metaData' in data and not data['metaData']['hasMoreItems']:
    break
  print(f"Completed page {str(page)}")
  page += 1

print(f"Found {len(restaurants)} restaurants")
with open('restaurants.json', 'w') as out:
  out.write(json.dumps(restaurants))
  out.close()
