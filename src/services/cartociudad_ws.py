import requests

CARTOCIUDAD_WS_URL = "http://www.cartociudad.es/geocoder/api/geocoder/"
REVERSE_GEOCODE_WS = "reverseGeocode"
REVERSE_GEOCODE_PROV = "province"
REVERSE_GEOCODE_MUN = "muni"

def reverse_geocode(lat, lon):
  prov = None
  mun = None

  if lat and lon:
    url = CARTOCIUDAD_WS_URL + REVERSE_GEOCODE_WS
    res = requests.get(url, params={'lat': lat, 'lon': lon})
    if res.status_code == requests.codes.ok:
      json = res.json()
      prov = json[REVERSE_GEOCODE_PROV]
      mun = json[REVERSE_GEOCODE_MUN]

  return prov, mun
