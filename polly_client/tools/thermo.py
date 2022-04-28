from gladier import GladierBaseTool, generate_flow_definition

def thermo(proc_dir = None, polly_json = None, **data):
    import os
    import json

    os.chdir(proc_dir)

    return polly_json

@generate_flow_definition
class Thermo(GladierBaseTool):
    funcx_functions = [thermo]
    required_input = [
        'proc_dir',
        'polly_json',
        'funcx_endpoint_compute'
        ]
