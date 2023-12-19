
from ..models.encounter import Encounter

class EncounterController:
    def __init__(self):
        self.model = Encounter()

    def get_encounter(self):
        data = self.model.get_encounter()
        return data

    def update_encounter(self, data):
        result = self.model.update_encounter(data)
        return result
