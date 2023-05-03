# **_Fogwing IIoT Simulator Program to send data using API Key_**
This repository contains three files that enable you to send sample data to Fogwing IoTHub via API using API Key.

>**Note:** This SDK is subject to change as it is currently in preview.

## **Fogwing IIoT Simulation using API client.**

To simulate data to Fogwing using an API, you will need to download the following files:
* [fw_apikey_client.py](https://github.com/factana/fogwing-simulator-for-iothub-api/blob/master/using_API_key/fw_apikey_client.py)
* [configuration.json](https://github.com/factana/fogwing-simulator-for-iothub-api/blob/master/using_API_key/configuration.json)
* [requirements.txt](https://github.com/factana/fogwing-simulator-for-iothub-api/blob/master/using_API_key/requirements.txt)

>**Note:** The purpose of the code is to send sample data over Fogwing IoTHub using an API client. To achieve this, you can modify the **configuration.json** file to configure the Fogwing IoTHub credentials and customize the sample data as needed.

## Here are the steps to follow in order to send data to Fogwing IIoT using an API:

### **1. Moving Files.**
* Move downloaded files to a directory of your choice on your system. Once you have done this, you can proceed with the next steps.

### **2. Installing Libraries** 
* You can install all the required libraries using pip and the requirements.txt file provided using follwing command.

  - `pip install -r requirements.txt`

### **3. Update Credentials**
* To update credentials for Fogwing IoTHub access, you need to modify the **configuration.json** file. 
* Replace the placeholder values of **USERNAME** and **PASSWORD** with your Fogwing IoTHub access credentials and save the file.
  
### **4. Run the Program and Get Started with Fogwing IIoT**
* To run the program, use the following command.
   - `python fw_apikey_client.py`


>**Note:** If everything goes according to the instructions mentioned above, you should see `{"statusCode":201,"message":"Created","description":"The Request Has Succeeded","data":"Successfully published"}` message displayed on the Terminal.

### **5. Analyze Your Data on the Fogwing Platform**
* Now you are ready to analyze your data at [Fogwing Platform](https://portal.fogwing.net/) portal,
  you can check all the data within the data storage in the portal.
  
## **Where to Find Help and Resources for Fogwing**
* [Fogwing Open APIs Docs.](https://api.fogwing.net/)
* [Fogwing Platform Forum.](https://community.fogwing.io/)
* [Fogwing Platform Docs.](https://docs.fogwing.io/)
 

## Please visit https://www.fogwing.io/industrial-iot-platform/ for more information about Fogwing Industrial IoT Platform. ##
