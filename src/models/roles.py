from configs.database import db

class RolesModel(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    
    def serialize_full(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }