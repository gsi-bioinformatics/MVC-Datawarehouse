from .mongodb import get_db

class HealthcareService:
    @staticmethod
    def get_all():
        db = get_db()
        return db.HealthcareService.find()
