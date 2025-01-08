import requests

# Define the API endpoint
url = "https://percallpro.leadportal.com/apiJSON.php"

# Define the initial payload
initial_payload = {
    "Request": {
        "Key": "c366069fb8928731803bc0320714e22c45ae7f674d7ece8fd4fea2d8fa24cbc6",
        "API_Action": "iprSubmitLead",
        "TYPE": "35",
        "Mode": "ping",
        "Return_Best_Price": "1",
        "Return_Min_Duration": "1",
        "SRC": "Zizye_Dynamic",
        "Origin_Phone": "7276347664",
        "State": "FL",
        "ZIP": "33130",
        "Terminating_Phone": "7273535323",
        "Test_Lead": "1",
        "Format": "JSON"  # Added Format: JSON
    }
}

# Send the initial POST request
response = requests.post(url, json=initial_payload)

# Parse the JSON response
try:
    response_data = response.json()
    print("Initial Response:", response_data)
except ValueError:
    print("Error parsing JSON:", response.text)
    exit()

# Check if the response contains "Matched" case-sensitive
if response_data.get('response', {}).get('status') == "Matched":
    # Extract the lead_id from the response (case-sensitive correction)
    lead_id = response_data.get('response', {}).get('lead_id')  # Correctly accessing lead_id
    if not lead_id:
        print("lead_id not found in the response!")
        exit()

    # Prepare the new payload with Mode: post, lead_id, and Format: JSON
    new_payload = {
        "Request": {
            "Key": "c366069fb8928731803bc0320714e22c45ae7f674d7ece8fd4fea2d8fa24cbc6",
            "API_Action": "iprSubmitLead",
            "TYPE": "35",
            "Mode": "post",
            "Return_Best_Price": "1",
            "Return_Min_Duration": "1",
            "SRC": "Zizye_Dynamic",
            "Origin_Phone": "7276347664",
            "State": "FL",
            "ZIP": "33130",
            "Terminating_Phone": "7273535323",
            "Lead_ID": lead_id,  # Ensure Lead_ID is included in the payload
            "Format": "JSON"  # Added Format: JSON
        }
    }

    # Send the second POST request
    second_response = requests.post(url, json=new_payload)

    # Parse and display the second response
    try:
        second_response_data = second_response.json()
        print("Second Response:", second_response_data)
    except ValueError:
        print("Error parsing JSON in second request:", second_response.text)
else:
    print("Response did not match the criteria for re-sending the request.")
print("Second Payload:", new_payload)
