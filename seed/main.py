from seed import create_app
from configs.database import db
from src.models.users import UserModel
from src.models.roles import RolesModel

app = create_app()

with app.app_context():
    # Create tables if they don't exist
    db.create_all()

    # Seed roles
    admin_role = RolesModel(name="Admin", description="Administrator role")
    user_role = RolesModel(name="User", description="Regular user role")
    superadmin_role = RolesModel(name="SuperAdmin", description="Super user role")
    db.session.add_all([admin_role, user_role, superadmin_role])
    db.session.commit()

    # Seed users with role_id references
    users = [
        UserModel(name="Alice", email="alice@example.com", password="alicepass", role_id=admin_role.id),
        UserModel(name="Bob", email="bob@example.com", password="bobpass", role_id=user_role.id),
        UserModel(name="Charlie", email="charlie@example.com", password="charliepass", role_id=superadmin_role.id)
    ]
    db.session.add_all(users)
    db.session.commit()
    print("Seeded roles and users.")