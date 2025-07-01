from faker import Faker

fake = Faker()

class RegisterModel:
    def random(self):
        return {"login": fake.name(), "password": fake.password()}
