import requests
import json

# Reading configuration file.
with open('configuration.json', 'r') as cred_file:
    cred = json.loads(cred_file.read())

config = cred.get("FW_CRED")
edgeEUI = config.get("EDGE_EUI")
apiKey = config.get("API_KEY")
accountID = config.get("ACCOUNT_ID")


def send_data_API(payload):
    """
    This function is to send data to Fogwing using API Key.
    :param payload: Data to be sent to Fogwing
    :returns: API Response
    :rtype: Dict
    """
    header = {"accountID": accountID, "apiKey": apiKey, "edgeEUI": edgeEUI}
    postPayload_url = "https://api.fogwing.net/api/v1/iothub/postPayload/withApiKey"
    resp = requests.post(postPayload_url, data=json.dumps(payload), headers=header, verify=True)
    return resp.text


if __name__ == '__main__':
    # Sample data to send over Fogwing IoTHub.
    data = cred.get("PAYLOAD")
    print(send_data_API(data))
