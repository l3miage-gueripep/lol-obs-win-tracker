import requests

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