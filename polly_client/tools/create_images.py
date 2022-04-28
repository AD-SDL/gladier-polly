from gladier import GladierBaseTool, generate_flow_definition

def create_images(proc_dir = None, json_name = None, **data):
    import os
    import json

    os.chdir(proc_dir)

    return json_name

@generate_flow_definition
class CreateImages(GladierBaseTool):
    funcx_functions = [create_images]
    required_input = [
        'proc_dir',
        'json_name',
        'funcx_endpoint_compute'
        ]
