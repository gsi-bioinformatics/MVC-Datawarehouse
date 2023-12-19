from datetime import datetime
from bson import ObjectId

class Encounter:

    def __init__(self, identifier:str, status: str, class_: str, priority: str, type: str, serviceType: str, subject: str, 
                  serviceProvider: str, appointment: str, actualPeriod: object, diagnosis: str, location:str):
        
        self._id = str(ObjectId())
        self.identifier = identifier
        self.status = status
        self.class_ = class_
        self.priority = priority
        self.type = type
        self.serviceType = serviceType
        self.subject = subject
        self.serviceProvider = serviceProvider
        self.appointment = appointment
        self.actualPeriod = actualPeriod
        self.diagnosis = diagnosis
        self.location = location
        

    def to_dict(self) -> dict:
        return {
            '_id': self._id,
            'documentId': self.documentId,
            'storagePath': self.storagePath,
            'documentName': self.documentName,
            'storageSize': self.storageSize,
            'createdBy': self.createdBy,
            'type': self.type,
            'source': self.source,
            'createdAt': self.createdAt
        }