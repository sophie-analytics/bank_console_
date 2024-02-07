class Address:
    def __init__(self, city: str, state: str, country: str, house_no: str, street: str) -> None:
        self.city = city
        self.state = state
        self.country = country
        self.house_no = house_no
        self.street = street

    def get_city(self):
        return self.city

    def set_city(self, value):
        self.city = value

    def get_state(self):
        return self.state

    def set_state(self, value):
        self.state = value

    def get_country(self):
        return self.country

    def set_country(self, value):
        self.country = value

    def get_house_no(self):
        return self.house_no

    def set_house_no(self, value):
        self.house_no = value

    def get_street(self):
        return self.street

    def set_street(self, value):
        self.street = value
