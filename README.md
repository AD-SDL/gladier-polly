# Gladier Polly Client

This client process the data from the CNM polybot experiment and store it in a globus portal. 

## Flow Description

The simple polly flow:

* **Data input** : pollybot.json
* **Transfer** to ALCF Eagle 
* **Proc** creates thermo result. `tools/thermo.py`
* **Proc** creates images based on the json. `tools/create_images.py`
* **Proc** gathers metadata and structure it for the portal. `tools/gather_metadata.py`
* **Publish** metadata and images into the portal

## Installation

    conda create -n gladier python pip
    conda activate gladier

    git clone https://github.com/AD-SDL/gladier-polly
    cd gladier-polly
    pip install -r requirements.txt

## Usage

On `polly_client.py` change `local_endpoint_id = 'cde22510-5de7-11ec-9b5c-f9dfb1abb183'` with your globus endpoint id.

For single client:
`polly_client.py path/to/file.json` is a single shot client that creates a flow based on one single json file

For file watcher:
`polly_watcher.py --dir path/to/folder` creates a filesystem watchdog on a given folder and invokes `polly_client` when new json files arrive.

## TODO

* Create GCP at polly machine.
* update `local_polly_endpoint`

* create `sample_folder` per json (done)
* update 'proc' functions

* create polly_group at globus for access permission
* add polly_group on globus_endpoint, flow_permissions

* start new index
* create new portal and facets

* typo on the json `'ressitance_data'`
