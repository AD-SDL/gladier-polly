from gladier import GladierBaseTool


class PollyJsonOut(GladierBaseTool):

    flow_definition = {
        'Comment': 'Transfer a file or directory in Globus',
        'StartAt': 'PollyJsonOut',
        'States': {
            'PollyJsonOut': {
                'Comment': 'Transfer a file or directory in Globus',
                'Type': 'Action',
                'ActionUrl': 'https://actions.automate.globus.org/transfer/transfer',
                'Parameters': {
                    'source_endpoint_id.$': '$.input.simple_transfer_source_endpoint_id',
                    'destination_endpoint_id.$': '$.input.simple_transfer_destination_endpoint_id',
                    'transfer_items': [
                        {
                            'source_path.$': '$.input.simple_transfer_source_path',
                            'destination_path.$': '$.input.simple_transfer_destination_path',
                            'recursive.$': '$.input.simple_transfer_recursive',
                        }
                    ]
                },
                'ResultPath': '$.PollyJsonOut',
                'WaitTime': 600,
                'End': True
            },
        }
    }

    flow_input = {
        'simple_transfer_sync_level': 'checksum',
        'simple_transfer_recursive': False,

    }
    required_input = [
        'simple_transfer_source_path',
        'simple_transfer_destination_path',
        'simple_transfer_source_endpoint_id',
        'simple_transfer_destination_endpoint_id',
    ]