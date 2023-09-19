import json

robot_id = '?'

with open("./secrets.json") as secrets_file:
    secrets = json.load(secrets_file)
    robot_id = str(secrets["robot_id"])

WIFI_SSID=f'xrp102-{robot_id}'
WIFI_PASSWORD='robot102'

# Set up a wireless hotspot with WIFI_SSID/WIFI_PASSWORD above, useful for testing
WIFI_AP_MODE=True