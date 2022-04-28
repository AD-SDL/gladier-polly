from gladier import GladierBaseTool, generate_flow_definition



def gather_polybot_metadata(proc_dir = None, json_name = None, **data):
    import json
    import os

    os.chdir(proc_dir)

    json_file = os.path.join(proc_dir, json_name)

    if not os.path.exists(json_file):
        return 'error!'

    GENERAL_METADATA = {
        "creators": [
            {
                "creatorName": "Polybotters"
            }
        ],
        "publicationYear": "2019",
        "publisher": "Argonne National Lab",
        "resourceType": {
            "resourceType": "Dataset",
            "resourceTypeGeneral": "Dataset"
        },
        "subjects": [
            {
                "subject": "beamline"
            }
        ],
    }

    def gather_json(json_file):
        with open(json_file, 'r') as f:
            hframe = json.load(f)

        metadata.update(hframe)
        # metafilename, _ = os.path.splitext(os.path.basename(json_file))
        metadata = GENERAL_METADATA.copy()

        return metadata

    # Generate metadata
    metadata = gather_json(json_file)
    pilot = data.get('pilot','')
    # metadata passed through from the top level takes precedence. This allows for
    # overriding fields through $.input
    metadata.update(pilot.get('metadata', {}))

    pilot['metadata'] = metadata
    pilot['groups'] = data.get('groups', [])
    return pilot

@generate_flow_definition
class GatherMetadata(GladierBaseTool):
    funcx_functions = [gather_polybot_metadata]
    required_input = [
        'proc_dir',
        'json_name',
        'funcx_endpoint_compute'
        ]


if __name__ == '__main__':
    proc_dir = '/eagle/APSDataAnalysis/POLLY'
    json_name = 'test_data.json'
    data = {
        'proc_dir': proc_dir,
        'json_name': json_name,
        'metadata': {},
        'groups': []
    }
    from pprint import pprint
    pprint(gather_polybot_metadata(proc_dir, json_name, **data))
