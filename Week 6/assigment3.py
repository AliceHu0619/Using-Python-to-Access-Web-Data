"""
=================================================================
05 - APIs / Geocoding
Using Python to Access Web Data (University of Michigan / Coursera)
=================================================================
Example of calling a web-based API with query parameters and
parsing a nested JSON response.
"""

import urllib.request
import urllib.parse
import json


# --- 1. Call a geocoding API and parse nested JSON ---
"""
Calls the OpenGeo geocoding web service with an address, then parses
the nested JSON response to extract the location's plus code.
"""
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

address = 'Budapest University of Technology and Economics'
params = {'q': address, 'key': 42}

# Build the URL: .../opengeo?q=Lviv+Poly+...&key=42
url = serviceurl + urllib.parse.urlencode(params)

# Fetch the data
uh = urllib.request.urlopen(url)
data = uh.read().decode()

# Convert the JSON response into a Python object
js = json.loads(data)

# Navigate the nested structure to find the value we need:
# js['features'] -> a list
# [0]             -> the first item in the list
# ['properties']  -> the properties dictionary
# ['plus_code']   -> the code we're looking for
plus_code = js['features'][0]['properties']['plus_code']

print(plus_code)