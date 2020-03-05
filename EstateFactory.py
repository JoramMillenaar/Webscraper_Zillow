
class Geo():
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
    
    def __repr__(self):
        return f'{self.__class__.__name__}: latidude={self.latitude}, longitude={self.longitude}'

class Location():
    def __init__(self, streetAddress, city, state, postalCode, geo:Geo):
        self.streetAddress = streetAddress
        self.city = city
        self.state =state
        self.postalCode = postalCode
        self.geo = geo

    def __repr__(self):
        return f'{self.__class__.__name__}: Address= {self.streetAddress}, {self.city}, {self.state}, {self.postalCode}'

    def getStreet(self):
        return self.streetAddress

class Estate():
    def __init__(self, _type, price, agency, size, location:Location, availability):
        self._type = _type
        self.price = price
        self.agency = agency
        self.location = location
        self.size = size
        self.availability = availability

    def getKey(self):
        return self.location.getStreet()

class House(Estate):
    def __init__(self, _type, price, agency, size, location:Location, availability, rooms):
        Estate.__init__(self, _type, price, agency, size, location, availability)
        rms = [i for i in rooms if i in '1234567890']
        self.beds = rms[0]
        self.baths = rms[1]
        self.rooms = {'Beds': self.beds, 'Baths': self.baths}

    def __repr__(self):
        return f'{self.__class__.__name__}:\n\ttype= {self._type}\n\tprice={self.price}\n\tagency={self.agency}\n\tsize= {self.size} (sqft)\n\trooms={self.rooms}'
    
    def getRooms(self):
        return self.rooms

    def getBeds(self):
        return self.beds

    def getBaths(self):
        return self.baths

class Lot(Estate):
    def __init__(self, _type, price, agency, size, location:Location, availability):
        Estate.__init__(self, _type, price, agency, size, location, availability)

    def __repr__(self):
        return f'{self.__class__.__name__}:\n\ttype= {self._type}\n\tprice={self.price}\n\tagency={self.agency}\n\tsize= {self.size} (acres)'

