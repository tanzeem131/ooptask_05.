class Travel:
    def __init__(self,number_of_passengers, distance_travelled, mode_of_transportation):
        self.__number_of_passengers=number_of_passengers
        self.distance_travelled =distance_travelled
        self.mode_of_transportation = mode_of_transportation

class Train(Travel):
    def __init__(self, number_of_passengers, distance_travelled, mode_of_transportation):
        super().__init__(number_of_passengers, distance_travelled, mode_of_transportation)

    def cost_of_trip(self):
        return self._Travel__number_of_passengers*60

class Bus(Travel):
    def __init__(self, number_of_passengers, distance_travelled, mode_of_transportation):
        super().__init__(number_of_passengers, distance_travelled, mode_of_transportation)

    def cost_of_trip(self):
        return self._Travel__number_of_passengers*100

T =Train(10,100,'Train')
B =Bus(10,100,'Bus')

T.cost_of_trip()
B.cost_of_trip()
print("COST OF TRIP THROUGH TRAIN IS: Rs",T.cost_of_trip(),"\nCOST OF TRIP THROUGH BUS IS: Rs",B.cost_of_trip())
