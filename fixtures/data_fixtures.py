import pytest

from helpers.generate_data import DataGenerate


@pytest.fixture(scope="function")
def generate_data():
    data = DataGenerate("ru_RU")
    name = data.generate_username()
    password = data.generate_password()
    email = data.generate_email()
    return name, password, email
