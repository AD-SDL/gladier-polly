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

`polly_client.py` is a single shot client that creates a flow based on one single json file
`polly_watcher.py` creates a filesystem watchdog on a given folder and invokes `polly_client` when new json files arrive.


## TODO:
* Create GCP at polly machine.
* update `local_polly_endpoint`
* update 'proc' functions
* start new index
* create new portal and facets
* create polly_group at globus for access permission

