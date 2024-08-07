import requests

MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoiYW5kcmV3ZGViZW5oYW0iLCJhIjoiY2x6ajJ3cXp2MG1iazJqcHI5ZXFocmJyNCJ9.4IMVFlxsyqClkhiFYl81fA'

def geocode_location(country, region):
    location = f"{region}, {country}"
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{location}.json?access_token={MAPBOX_ACCESS_TOKEN}"
    response = requests.get(url)
    data = response.json()
    if data['features']:
        coordinates = data['features'][0]['center']
        return coordinates
    return None