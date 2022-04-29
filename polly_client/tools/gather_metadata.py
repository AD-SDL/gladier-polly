from gladier import GladierBaseTool, generate_flow_definition



def gather_polybot_metadata(proc_dir = None, json_name = None, **data):
    import json
    import os
    import datetime 

    os.chdir(proc_dir)

    json_file = os.path.join(proc_dir, json_name)

    if not os.path.exists(json_file):
        return 'error!'

    metadata = data.get('metadata',{})

    json_base = json_name.replace('.json','')


    metadata.update({
        "creators": [{"creatorName": "Polybotters"}],
        'description': f'{json_base}: Automated data processing.',
        'title': json_base,
        'publicationYear': f'{datetime.datetime.now().year}',
        'resourceType': {
            'resourceType': 'Dataset',
            'resourceTypeGeneral': 'Dataset'
        },
        "subjects": [{"subject": "SDL Polybot"}],
    })

    with open(json_file, 'r') as f:
        hframe = json.load(f)                
        metadata.update(hframe)
    os.unlink(json_file) #Necessary?

    pilot = data.get('pilot',{})
    # metadata passed through from the top level takes precedence. This allows for
    # overriding fields through $.input
    metadata.update(pilot.get('metadata', {}))

    pilot['metadata'] = metadata
    pilot['groups'] = data.get('groups', [])
    pilot['destination'] = data.get('dest','/')
    return pilot

@generate_flow_definition
class GatherPolybotMetadata(GladierBaseTool):
    funcx_functions = [gather_polybot_metadata]
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
    pprint(gather_polybot_metadata(**data))

