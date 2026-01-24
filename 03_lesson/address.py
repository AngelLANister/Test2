class Address:
    def __init__(self, index, city, street, building, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self.apartment = apartment

    def __str__(self):
        return (f"{self.index}, "
                f"{self.city}, "
                f"{self.street}, "
                f"{self.building} - "
                f"{self.apartment}")
