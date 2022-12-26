from datetime import datetime


class Person:
    def __init__(self, name, year_of_birth, address=None):
        self.name = name
        self.yob = year_of_birth
        self.address = address

    def get_age(self):
        now = datetime.now()
        return now.year - self.yob

    # @property
    def get_name(self):
        return self.name

    # @username.setter
    def set_name(self, name):
        self.name = name

    # @property
    def get_address(self):
        return self.address

    # @user_address.setter
    def set_address(self, address):
        self.address = address

    def is_homeless(self):
        """
        returns True if address is not set, false in other case
        """
        return self.address is None


person = Person('Ivan', 1980, 'st.London-street')
# person = Person('Ivan', 1980)
