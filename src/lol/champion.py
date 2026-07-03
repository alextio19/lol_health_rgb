from lol.api import LoLAPI

class Champion:
    def __init__(self):
        self.gold = 0
        self.last_gold = 0
        self.last_health = 0
        self.api = LoLAPI()
        self.events = dict()
        self.current_health = 0
        self.max_health = 0

    def refresh_data(self):
        data = self.api.active_player()
        if data:
            self.name = data.get('summonerName')
            self.level = data.get('level')
            self.gold = data.get('currentGold')
            self.max_health = find_value(data, "maxHealth")
            self.current_health = find_value(data, "currentHealth")
            if self.current_health and self.max_health:
                self.health_percentage = int((self.current_health/self.max_health) * 100)
                return True
            else:
                return False
        else:
            return False