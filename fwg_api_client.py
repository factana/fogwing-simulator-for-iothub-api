import requests
import json
import urllib3

# Disabled Python warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def send_data_API(user_name, password, sample_data):
    # URL link for getting API-KEY.
    credentials = {"username": user_name, "password": password}
    api_key_url = 'https://enterprise.fogwing.net/api/iothub/getApiToken'
    resp = requests.post(api_key_url, json=credentials, verify=False)
    resp_dict = json.loads(resp.text)
    api_key = resp_dict['token']

    # URL link for posting data over Fogwing IoTHub.
    header = {"API-TOKEN": api_key}
    payload_url = 'https://enterprise.fogwing.net/api/iothub/postPayload'
    payload_resp = requests.post(payload_url, data=json.dumps(sample_data), headers=header, verify=False)
    print(json.dumps(sample_data, indent=4))
    print(payload_resp.text)


if __name__ == '__main__':
    # Reading configuration file.
    with open('configuration.json', 'r') as file:
        config = json.load(file)
    # Fogwing IoTHub credentials
    usr_name = config['Fwg_IoTHub_cred']['username']
    psw = config['Fwg_IoTHub_cred']['password']
    # Sample data to send over Fogwing IoTHub.
    data = config['payload']
    send_data_API(usr_name, psw, data)
