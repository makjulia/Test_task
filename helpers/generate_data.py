from faker import Faker

class DataGenerate:
    def __init__(self, locale="ru_RU"):
        self.fake = Faker(locale)

    def generate_username(self):
        """Метод для генерации данных для поля Username"""
        username = self.fake.first_name()
        return username

    def generate_password(self):
        """Метод для генерации данных для поля Password"""
        password = self.fake.password()
        return password

    def generate_email(self):
        """Метод для генерации данных для поля Email"""
        email = self.fake.email()
        return email