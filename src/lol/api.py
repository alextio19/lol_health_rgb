requests = __import__('requests')
urllib3 = __import__('urllib3')

class LoLAPI:
    def __init__(self):
        self.base_url = "https://127.0.0.1:2999/liveclientdata"

    def active_player(self):
        response = None
        try:
            urllib3.disable_warnings()
            url = self.base_url + "/activeplayer"
            response = requests.get(url, verify=False).json()
        except Exception as e:
            return False
        return response