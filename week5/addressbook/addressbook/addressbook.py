import requests

class Contact():
    def __init__(self, firstName, lastName, emailAddress, phoneNumber, photoUrl):
        self.firstName = firstName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber
        self.photoUrl = photoUrl

    @property
    def get_firstName(self):
        return self.firstName
    
    @get_firstName.setter
    def set_firstName(self, value):
        self.firstName = value
    
    @property
    def get_lastName(self):
        return self.lastName
    
    @get_lastName.setter
    def set_lastName(self, value):
        self.lastName = value
    
    @property
    def get_emailAddress(self):
        return self.emailAddress

    @get_emailAddress.settter
    def set_emailAddress(self, value):
        self.emailAddress = value
    
    @property
    def get_photoUrl(self):
        return self.photoUrl

    @get_photoUrl.setter
    def set_photoUrl(self, value):
        self.photoUrl = value

    def __str__(self):
        return f"{self.emailAddress}"

    def __repr__(self):
        return "FIX THIS HERE"

class AddressBook():
    def __init__(self):
        self.addresses = []
        
    def addAddress(self,address):
        self.addresses.append(address)
        
    def getAllAddresses(self):
        return self.addresses
    
    def findAllMatching(self,searchStr):
        results = []
        for address in self.addresses:
            
            if address.getFirstName().lower().startswith(searchStr.lower()) or address.getLastName().lower().startswith(searchStr.lower()):
                results.append(address)
                
        return results
    
   