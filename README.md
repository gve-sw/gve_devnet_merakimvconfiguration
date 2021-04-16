# GVE Devnet Meraki MV Camera Audio Configuration 

A python script to turn the audio settings for the meraki camera on/off. 

## Contacts
* Eda Akturk (eakturk@cisco.com)

## Solution Components
* Meraki MV Camera
* Python 3.8

## Installation/Configuration

#### Clone the repo :
```$ git clone (link)```

#### *(Optional) Create Virtual Environment :*
Initialize a virtual environment 

```virtualenv venv```

Activate the virtual env

*Windows*   ``` venv\Scripts\activate```

*Linux* ``` source venv/bin/activate```

#### Install the libraries :

```$ pip install -r requirements.txt```

## Setup: 

1. Enable api access and generate an api key for your Meraki Dashboard to use the Dashboard API. 
You can enable access and generate an api key by following the steps [here.](https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API)

2. Import your meraki api key to main.py  
```
API_KEY = " "
```

3. (Optional) The python scripts uses the "Update Device Camera Quality And Retention Settings" api which can be found [here.](https://developer.cisco.com/meraki/api/#!update-device-camera-quality-and-retention-settings)
You can extend the scripts by adding more payload parameters and/or api calls. 

4. Add the camera serial id's to the serial id list in main.py. 
```
serial_id_list  = [ 'id' , 'id' ]
```
If you would like all the camera's in your organization use the function 'get_camera_ids' with your organization id to populate the serial id list. 
```
org_id = ' '
serial_id_list = get_camera_ids(org_id)
```

## Usage

Run the python script by:

    $ python main.py

Some options to run automatically:

- cron tab tasks to execute the scripts periodically 
- schedule alarms to run the script

## License
Provided under Cisco Sample Code License, for details see [LICENSE](../../Desktop/CodeExchange/meraki_servicenow_integration/LICENSE.md).



## Code of Conduct
Our code of conduct is available [here](../../Desktop/CodeExchange/meraki_servicenow_integration/CODE_OF_CONDUCT.md).



## Contributing
See our contributing guidelines [here](../../Desktop/CodeExchange/meraki_servicenow_integration/CONTRIBUTING.md).
