import requests
import datetime

# API URL for POST request
api_url = 'http://52.24.41.159:8083/process_sldc_dsm_files'

# authentication 
username = 'ops_dsm_di'
password = 'ops@#123dsm'

# Input data to be sent in the request body
input_data = {
    'entity_id': 'IN_MH',
    'rev_num': "R1",
    'version': 'v1',
    'time_period': '2023_WK18'
}


# POST request with basic authentication and input data
response = requests.post(api_url, json=input_data, auth=(username, password))

if response.status_code == 200:
    # Generating log file name with a timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_file_name = f'log_{timestamp}.txt'

    # storing log file as .text
    with open(log_file_name, 'w') as file:
        file.write(response.text)
    print(f"Log file saved as '{log_file_name}'")
else:
    # If failed.
    print(f"Request failed with status code {response.status_code}")