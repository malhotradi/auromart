from datetime import datetime

class User:
    def __init__(self, user_id, email, tier="STANDARD"):
        self.id = user_id
        self.email = email
        self.tier = tier  # Options: STANDARD, GOLD, PLATINUM
        self.created_at = datetime.now()
        self.is_active = True

    def __repr__(self):
        return f"<User {self.email} ({self.tier})>"
