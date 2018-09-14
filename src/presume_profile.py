"""Profile class object
"""
import datetime as dt


class Profile(object):
    """
    """
    def __init__(self, name, phone_num=None, email=None):
        self.name = name
        self.email = email
        self.phone_num = phone_num
        self.address = {}  # dict with street, city, state, zip as keys
        self.skills = set()  # set of tuples
        self._created_date = dt.datetime.today()
        self._touched_date = dt.datetime.today()
        print(f"Profile created for {self.name} at {self._created_date}.")

    def __repr__(self):
        return f"Profile(name={self.name}, created={self._created_date})"

    def edit_address(self, street=None, city=None, state=None, zip=None):
        address = self.address
        params = ['street', 'city', 'state', 'zip']

        # edit fields only if user provides the parameter
        for param in params:
            if eval(param) is not None:
                address[param] = str(eval(param))

        self._touched_date = dt.datetime.today()

    def edit_skills(self, skill_list):
        self.skills.update(set(skill_list))

    def edit_education(self, skill_list):
        pass

    def edit_socialmedia(self, skill_list):
        pass

    def edit_description(self, skill_list):
        pass

    def edit_misc(self, skill_list):
        pass
