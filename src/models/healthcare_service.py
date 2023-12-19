from .mongodb import get_db

class HealthcareService:
    @staticmethod
    def get_all_service():
        db = get_db()
        return db.HealthcareService.find()
