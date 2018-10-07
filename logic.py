from py_osrm import Py_osmr
import json

if __name__ == "__main__":
    start = ('-79.25082550000002','43.77194799999999')
    to = ('-79.24355109999999','43.7575673')

    endpoint = 'https://router.project-osrm.org'
    wrapper = Py_osmr(endpoint)
    temp = wrapper.route(start_coord=('13.414167165756226','52.52167215019524'), end_coord=('13.4197763','52.5003103'),steps=True)
    print(json.dumps(temp, indent=2))