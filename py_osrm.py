import requests
import json

class Py_osmr():
    
    def __init__(self, endpoint=''):
        self.endpoint = endpoint
    
    def route(self, start_coord, end_coord, intermediate=None, alternatives=False, 
                 steps=False, output="full",
                 geometry='geojson', overview="simplified",
                 annotations=False, continue_straight='default',
                 version='v1', generate_hints = False):
        
        url = self.endpoint + '/route/' + version + '/driving/'
        url_parse_start_coord = start_coord[0] + ',' + start_coord[1]
        
        if intermediate:
            for coord in intermediate:
                url += coord[0] + ',' + coord[1] + ';'

        url_parse_end_coord = end_coord[0] + ',' + end_coord[1]
        url += url_parse_start_coord + ';' + url_parse_end_coord
        
        params = ''.join([
            '?overview={}'.format(overview),
            '&steps={}'.format(str(steps).lower()),
            '&alternatives={}'.format(str(alternatives).lower()),
            '&geometries={}'.format(geometry),
            '&continue_straight={}'.format(continue_straight),
            '&generate_hints={}'.format(str(generate_hints).lower())
            ])
        if annotations:
            params += '&annotations=true'
        url += params
        
        req = requests.get(url)
        
        if (not (req.status_code == 200)):
            raise ValueError(
                'Error: Repose ' + str(req.status_code) + '\n' + 'from URL: ' + url
            )
        print(url)
        #response_json = json.loads(req.json(), encoding='utf-8')
        return req.json()
