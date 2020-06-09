import requests
import json


def send_data_API():
    # Reading configuration file.
    with open('configuration.json', 'r') as file:
        config = json.load(file)

    # Fogwing IoTHub credentials
    username = config['Fwg_IoTHub_cred']['username']
    password = config['Fwg_IoTHub_cred']['password']

    # Sample data to send over Fogwing IoTHub.
    sample_data = config['sample_data']

    # URL link for getting API-KEY.
    credentials = {"username": username, "password": password}
    api_key_url = 'https://non-prod.fogwing.net/api/iothub/IoT Hub API Methods/getApiKey'
    resp = requests.post(api_key_url, json=credentials, verify=False)
    resp_dict = json.loads(resp.text)
    api_key = resp_dict['token']

    # URL link for posting data over Fogwing IoTHub.
    header = {"API-KEY": api_key}
    payload_url = 'https://non-prod.fogwing.net/api/iothub/IoT Hub API Methods/postPayload'
    payload_resp = requests.post(payload_url, data=json.dumps(sample_data), headers=header, verify=False)
    print(payload_resp.text)


send_data_API()
