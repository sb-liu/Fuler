from py_osrm import Py_osmr
import json

def view_steps_to_route(json_response):
    '''
    input: json json_respose, our result object from route api call to server
    output: list[(float, str, str)] word dictation of directions with distances
    '''
    to_parse = json_response['routes'][0]['legs'][0]['steps']
    result = []
    for step in to_parse:
        dist = step['distance']
        if step['maneuver']['type'] != 'arrive':
            word_dictation = step['maneuver']['modifier'] +' '+step['maneuver']['type']
        else:
            word_dictation = 'arrive'
        location = step['name']
        result.append((dist, word_dictation, location))
    return result

if __name__ == "__main__":
    start = ('-79.25082550000002','43.77194799999999')
    to = ('-79.24355109999999','43.7575673')

    endpoint = 'https://router.project-osrm.org'
    # routes, legs, legs, steps
    # to get to 
    wrapper = Py_osmr(endpoint)
    temp = wrapper.route(start_coord=('13.414167165756226','52.52167215019524'), end_coord=('13.4197763','52.5003103'),steps=True)
    print(view_steps_to_route(temp))
    # print(json.dumps(temp, indent=2))