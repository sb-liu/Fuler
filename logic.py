import requests
import json


r = requests.get('https://router.project-osrm.org/route/v1/driving/13.414167165756226,52.52167215019524;13.4197763,52.5003103?geometries=geojson&alternatives=false&steps=true&generate_hints=false')

if (r.status_code == 200):
    print (json.dumps(r.json(), sort_keys=True, indent=2))
else:
    print(r.status_code)