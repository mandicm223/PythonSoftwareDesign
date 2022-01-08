from typing import List
from address import Address

class Person:
    def __init__(self, first, last, dob, phone, address):
        self.first_name = first
        self.last_name = last
        self.date_of_birth = dob
        self.phone = phone
        self.addresses = []

        #Check if adress is passed as instance of Address class, or list of instances of Address class

        if isinstance (address,Address):
            self.addresses.append(address)
        elif isinstance(address,list):
            for entry in address:
                if not isinstance(entry,Address):
                    raise TypeError('Invalid address...')
            self.addresses = address
        else:
            raise TypeError('Invalid address...')

    def add_address(self, address):
        if not isinstance(address,Address):
            raise TypeError('Invalid address...')
        self.addresses.append(address)

