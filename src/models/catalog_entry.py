from .mongodb import get_db

class CatalogEntry:
    @staticmethod
    def get_all():
        db = get_db()
        return db.CatalogEntry.find()
