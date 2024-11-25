class Vehicle:
    def __init__(self, color, number_of_doors, gas_powered):
        self.__color = color
        self.__number_of_doors = number_of_doors
        self.__gas_powered = gas_powered

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        available_colors = ['black', 'white', 'grey', 'red', 'blue']
        if isinstance(value, str) and value.lower() in available_colors:
            self.__color = value.lower()
        else:
            raise ValueError(f'You should choose the color from {available_colors}')

    @property
    def number_of_doors(self):
        return self.__number_of_doors

    @number_of_doors.setter
    def number_of_doors(self, value):
        available_doors = ['2', '4', '5']
        if isinstance(value, int) and value in available_doors:
            self.__number_of_doors = value
        else:
            raise ValueError(f'You have to choose the number of doors from {available_doors}')

    @property
    def gas_powered(self):
        return self.__gas_powered

    @gas_powered.setter
    def gas_powered(self, value):
        if isinstance(value, bool):
            self.__gas_powered = value
        else:
            raise ValueError(f'It should be True or False')

    def __str__(self):
        return f"The vehicle has {self.color} color, and {self.number_of_doors} of doors, and gas powered: {self.gas_powered}"

    def eco_friendly(self):
        return self.number_of_doors == 2 and not self.gas_powered


class Truck(Vehicle):
    def __init__(self, color, number_of_doors, gas_powered, seats, space_trunk):
        super().__init__(color, number_of_doors, gas_powered)
        self.__seats = seats
        self.__space_trunk = space_trunk

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, value):
        if isinstance(value, int) and value > 0:
            self.__seats = value
        else:
            raise ValueError(f'The seats should be a positive number')

    @property
    def space_trunk(self):
        return self.__space_trunk

    @space_trunk.setter
    def space_trunk(self, value):
        if isinstance(value, int) and value > 0:
            self.__space_trunk = value
        else:
            raise ValueError(f'The trunk should be a positive number')

    def __str__(self):
        return (f"The Truck has {self.color} color, and {self.number_of_doors} of doors, and gas powered: {self.gas_powered} "
                f"and {self.seats} of seats, {self.space_trunk} of trunk")

    def eco_friendly(self):
        base_eco_friendly = super().eco_friendly
        return base_eco_friendly and self.seats <= 2 and self.space_trunk == 1
