from configs.database import db

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    isArchived = db.Column(db.Boolean, default=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('RolesModel', backref=db.backref('users', lazy=True))
    def serialize_full(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'isArchived': self.isArchived,
            'role': self.role.serialize_full() if self.role else None
        }