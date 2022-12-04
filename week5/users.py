

class User:
    def __init__(self, firstName="", lastName="", 
            email="", userName = "", 
            password = "", uuid = "", phone = "", cell = "", 
            pictureLarge = "", pictureThumbnail = ""):
        
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.userName = userName
        self.password = password
        self.uuid = uuid
        self.phone = phone
        self.cell = cell
        self.pictureLarge = pictureLarge
        self.pictureThumbnail = pictureThumbnail
    
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
    def get_email(self):
        return self.email
    
    @get_email.setter
    def set_email(self, value):
        self.email = value

    @property
    def get_userName(self):
        return self.userName
    
    @get_userName.setter
    def set_userName(self, value):
        self.userName = value
    
    @property
    def get_password(self):
        return self.password
    
    @get_password.setter
    def set_password(self, value):
        self.password = value
    
    @property
    def get_uuid(self):
        return self.uuid
    
    @get_uuid.setter
    def set_uuid(self, value):
        self.uuid = value
    
    @property
    def get_phone(self):
        return self.phone
    
    @get_phone.setter
    def set_phone(self, value):
        self.phone = value
    
    @property
    def get_cell(self):
        return self.cell
    
    @get_cell.setter
    def set_cell(self, value):
        self.cell = value

    @property
    def get_pictureLarge(self):
        return self.pictureLarge
    
    @get_pictureLarge.setter
    def set_pictureLarge(self, value):
        self.pictureLarge = value
    
    @property
    def get_pictureThumbnail(self):
        return self.pictureThumbnail
    
    @get_pictureThumbnail.setter
    def set_pictureThumbnail(self, value):
        self.pictureThumbnail = value
