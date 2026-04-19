class UserProfile:
    def __init__(self, user_id, name, age, interests):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.interests = interests # List of strings (Unit 2)

class ProfileManager:
    def __init__(self):
        # Unit 4: Hashing Concept (Internal Dictionary)
        self.profiles = {}

    def add_user(self, user_id, name, age, interests):
        if user_id in self.profiles:
            print(f"Validation Error: User ID {user_id} already exists.")
            return False
        self.profiles[user_id] = UserProfile(user_id, name, age, interests)
        return True

    def get_user(self, user_id):
        return self.profiles.get(user_id, None)

    def update_user(self, user_id, name=None, age=None, interests=None):
        user = self.get_user(user_id)
        if not user:
            print("Validation Error: User not found.")
            return False
        if name: user.name = name
        if age: user.age = age
        if interests: user.interests = interests
        return True

    def display_all(self):
        print("\n--- Current User Profiles ---")
        for uid, p in self.profiles.items():
            print(f"ID: {uid} | Name: {p.name} | Age: {p.age} | Interests: {p.interests}")