from .mongodb import get_db

class Encounter:
    @staticmethod
    def get_all():
        db = get_db()
        return db.Encounter.find()
