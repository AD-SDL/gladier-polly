from gladier import GladierBaseTool, generate_flow_definition

def create_images(proc_dir = None, json_name = None, **data):
    import os
    import json

    os.chdir(proc_dir)

    with open(json_name,'r') as f:
        data = json.load(f)
        
    return data

@generate_flow_definition
class CreateImages(GladierBaseTool):
    funcx_functions = [create_images]
    required_input = [
        'proc_dir',
        'json_name',
        'funcx_endpoint_compute'
        ]

if __name__ == '__main__':
    data = {
        'proc_dir': '.',
        'json_name': 'test_data.json',
        'metadata': {},
        'groups': []
    }
    from pprint import pprint
    pprint(create_images(**data))