from __init__ import create_app
from configs.database import db
from src.models.users import UserModel

app = create_app()

with app.app_context():
    # Create tables if they don't exist
    db.create_all()

    # Add seed data
    users = [
        UserModel(name="Alice"),
        UserModel(name="Bob"),
        UserModel(name="Charlie")
    ]
    db.session.bulk_save_objects(users)
    db.session.commit()
    print("Seeded users table.")