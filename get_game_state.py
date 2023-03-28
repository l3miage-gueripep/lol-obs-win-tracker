import datetime
import requests
from requests.adapters import HTTPAdapter, Retry
from urllib3.exceptions import MaxRetryError

#set the number of retries to be done to 0
# s = requests.Session()
# retries = Retry(total=1)
# s.mount('http://', HTTPAdapter(max_retries=retries))

# Replace <region> and <summonerName> with the actual region and summoner name
region = 'euw1'
summoner_name = 'Caca Malveillant'


# Disable SSL verification
requests.packages.urllib3.disable_warnings()
# Path to your self-signed certificate
cert_path = r'C:\Users\Pouks\Documents\Stream Scripts\OBS-Studio-Python-Scripting-Cheatsheet-obspython-Examples-of-API\src\mine\riotgames.pem'

def is_playing():
    try:
        get_active_player_name()
        return True
    except Exception:
        return False
    
def get_active_player_name():
    return requests.get('https://127.0.0.1:2999/liveclientdata/activeplayername', verify=cert_path, timeout=0.1).json()

print(is_playing())