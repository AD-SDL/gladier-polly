#!/usr/bin/env python

##Basic Python import's
import argparse
import os

##Base Gladier imports
from gladier import GladierBaseClient, generate_flow_definition

##Import tools that will be used on the flow definition
from tools.transfer_from_polly import PollyJsonOut
from tools.thermo import Thermo
from tools.create_images import CreateImages
from tools.gather_metadata import GatherMetadata
## from gladier_tools
from gladier_tools.publish import Publish

@generate_flow_definition(modifiers={
   'publish_gather_metadata': {'payload': '$.GatherMetadata.details.result[0]'}
})
class PollyClient(GladierBaseClient):
    gladier_tools = [
        PollyJsonOut,
        Thermo,
        CreateImages,
        GatherMetadata,
        Publish
    ]

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('json_path', help='json file')
    return parser.parse_args()

def run_poly_flow(json_path):

    ##local variables
    local_endpoint_id = 'cde22510-5de7-11ec-9b5c-f9dfb1abb183' #GCP ID
    ##Remote variables
    remote_endpoint_id = 'b59a9a91-835d-47d2-88bc-3250f989fc93' #dtn_eagle
    funcx_endpoint_compute = 'e449e8b8-e114-4659-99af-a7de06feb847'

    json_name = os.path.basename(json_path)
    print(json_path)
    ## Flow inputs necessary for each tool on the flow definition.
    flow_input = {
        'input': {
            'json_name' : json_name,

            #local server information
            'transfer_source_endpoint_id': local_endpoint_id,
            'transfer_source_path': json_path,

            #remote server information
            'transfer_destination_endpoint_id':remote_endpoint_id,
            'transfer_destination_path':'',

            # funcX tutorial endpoint
            'funcx_endpoint_non_compute': funcx_endpoint_compute,
            'funcx_endpoint_compute': funcx_endpoint_compute,
            'proc_dir' : '/eagle/APSDataAnalisys/POLLY/proc',

            # Publication index and project
            'search_index': '',
            'search_project': 'polybot',
            'source_globus_endpoint': remote_endpoint_id,
            'groups': [],
            'pilot': {}
        }
    }

    client_run_label = 'AutoPolly: ' + json_name

    flow_run = pollyClient.run_flow(flow_input=flow_input, label=client_run_label)

    print('Run started with ID: ' + flow_run['action_id'])
    print('https://app.globus.org/runs/' + flow_run['action_id'])


if __name__ == '__main__':

    args = arg_parse()

    ##The first step Client instance
    pollyClient = PollyClient()

    run_poly_flow(args.json_path)
    
