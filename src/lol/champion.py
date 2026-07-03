from lol.api import LoLAPI
import os
import sys
sys.path.append(os.path.join(os.getcwd(),'src'))

from common_utils import (
    find_value
)
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
        return False