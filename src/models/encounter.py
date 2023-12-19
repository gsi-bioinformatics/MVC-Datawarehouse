from .mongodb import get_db

class Encounter:
    @staticmethod
    def get_encounter():
        db = get_db()
        data_encounter = db.Encounter.find()
        return data_encounter
    
    @staticmethod
    def update_encounter(data):
        db = get_db()
        update_data_encounter = db.Encounter.update_one({'_id': data['_id']}, {"$set": data}, upsert=False)
        return update_data_encounter
