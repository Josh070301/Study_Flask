from configs.database import db

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    isArchived = db.Column(db.Boolean, default=False)

    def serialize_full(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'isArchived': self.isArchived
        }