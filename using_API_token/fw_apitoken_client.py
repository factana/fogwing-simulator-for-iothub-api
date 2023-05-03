import requests
import json

# Reading configuration file.
with open('configuration.json', 'r') as cred_file:
    cred = json.loads(cred_file.read())

config = cred.get("FW_CRED")
user_name = config.get("USERNAME")
password = config.get("PASSWORD")


def get_APItoken():
    """
    This function is to generate API token.
    :returns: API Token
    :rtype: String
    """
    credentials = {"username": user_name, "password": password}
    api_token_url = "https://api.fogwing.net/api/v1/iothub/getApiToken"
    resp = requests.post(api_token_url, json=credentials, verify=True)
    resp_dict = json.loads(resp.text)
    return resp_dict.get("data").get("token")


def send_data_API(payload):
    """
    This function is to send data to Fogwing.
    :param payload: Data to be sent to Fogwing
    :returns: API Response
    :rtype: Dict
    """
    header = {"Authorization": f"Bearer {get_APItoken()}"}
    postPayload_url = "https://api.fogwing.net/api/v1/iothub/postPayload"
    request_resp = requests.post(postPayload_url, data=json.dumps(payload), headers=header, verify=True)
    return request_resp.text


if __name__ == '__main__':
    # Sample data to send over Fogwing IoTHub.
    data = cred.get("PAYLOAD")
    print(send_data_API(data))
