# _Fogwing IoT Simulator Program for Raspberry Pi using API_
This directory provide three files that sends sample data over Fogwing IoTHub using API.

**Note that these SDKs are currently in preview and are subject to change.**

## Fogwing IoT Simulation using API client
We have provided three files:
* [fwg_api_client.py](https://github.com/factana/fogwing-simulator-for-iothub-api/blob/master/fwg_api_client.py)
* [configuration.json](https://github.com/factana/fogwing-simulator-for-iothub-api/blob/master/configuration.json)
* [requirements.txt](https://github.com/factana/fogwing-simulator-for-iothub-api/blob/master/requirements.txt)

The logic behind the code is to send the sample data over Fogwing
IoTHub using API client and the **configuration.json** file is to
configure the Fogwing IoTHub credential and modify the sample data as you want.

## Step:1
### Python & json file
* Copy all the files into your Rasberry Pi and 
  you are good to start ! You now finish with coding part.
  
## Step:2
### Installing the libraries
* Install all required libraries using pip with our requirements.txt file.
    ```
    pip install -r requirements.txt
    ```
## Step:3
### Credentials
**Note:-** Do the following modification in **configuration.json** file.
* Enter **username** and **password** of your Fogwing IoTHub access. 
  
## Step:4
### Run and Get Started with Fogwing IoT
* Now run the file with the below command.
    ```
    python fwg_api_client.py
    ```
  **Note:-** Provided everything goes in line with the above mentioned instructions,
         you will be able to see a message that reads 'successfully published' in command line.

## Step:5
### Start analyzing your data at Fogwing Platform
* Now you are ready to analyze your data at [Fogwing Platform](https://enterprise.fogwing.net/) portal,
  you can check all the data within the data storage in the portal.
  
 ### Getting help and finding Fogwing docs
 * [Fogwing Platform Forum](https://enterprise.fogwing.net/)
 * [Fogwing Platform Docs](https://docs.fogwing.io/)
