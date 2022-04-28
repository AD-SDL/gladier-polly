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
##
from gladier_tools.publish import Publish

@generate_flow_definition
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

if __name__ == '__main__':

    args = arg_parse()


    ##The first step Client instance
    pollyClient = PollyClient()

    ##local variables
    local_endpoint_id = '' #GCP ID
    json_path = args.json_path
    json_name = os.path.basename(json_path)
    
    ##Remote variables
    remote_endpoint_id = ''
    funcx_endpoint_compute = ''

    ## Flow inputs necessary for each tool on the flow definition.
    flow_input = {
        'input': {
            'json_name' : '/test/test.txt',
            'proc_dir' : '/eagle/APSDataAnalisys/POLLY/proc',

            #local server information
            'simple_transfer_source_endpoint_id': local_endpoint_id,
            'simple_transfer_source_path': os.path.expanduser(args.dir),

            #remote server information
            'simple_transfer_destination_endpoint_id':remote_endpoint_id,
            'simple_transfer_destination_path':'/proc',

            # funcX tutorial endpoint
            'funcx_endpoint_compute': funcx_endpoint_compute,
        }
    }

    client_run_label = 'AutoPolly: ' + json_name

    flow_run = pollyClient.run_flow(flow_input=flow_input, label=client_run_label)

    print('Run started with ID: ' + flow_run['action_id'])
    print('https://app.globus.org/runs/' + flow_run['action_id'])
    
