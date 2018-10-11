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
        step_type = step['maneuver']['type']
        special_step_types = ['arrive', 'depart']
        if step_type in special_step_types:
            word_dictation = step_type
        else:
            word_dictation = step['maneuver']['modifier'] +' '+step['maneuver']['type']
        location = step['name']
        result.append((dist, word_dictation, location))
    return result

if __name__ == "__main__":
    start = ('-70','41')
    to = ('-72','42')

    endpoint = 'https://router.project-osrm.org'
    # routes, legs, legs, steps
    # to get to 
    wrapper = Py_osmr(endpoint)
    temp = wrapper.route(start_coord=start, end_coord=to,steps=True)
    print(view_steps_to_route(temp))
    # print(json.dumps(temp, indent=2))