"""
Date: 25-4-2026
"""
class College:
    def __init__(self, ccode, cname, ccity):
        self.collcode = ccode
        self.collname = cname
        self.collcity = ccity

    def welcome_message(self):
        print("Hello There !!!")

    def display_college_details(self):
        print(f"College Code: {self.collcode}")
        print(f"College Name: {self.collname}")
        print(f"City: {self.collcity}")



'''
class College:
    def __init__(self, ccode, cname, ccity):
        self._collcode = ccode
        self._collname = cname
        self._collcity = ccity

    def welcome_message(self):
        print('Hello There !!! ')

    def display_college_details(self):
        print("College Code: {} \nCollege Name: {} \nCity: {}".format(
            self._collcode, self._collname, self._collcity
        ))
'''
