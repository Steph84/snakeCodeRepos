import json
import math
import matplotlib.pyplot as plt


class Agent:
    def say_hello(self, first_name):
        return "Bien le bonjour " + first_name + " !"

    def __init__(self, position, **agent_attributes):
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)


class Position:
    def __init__(self, longitude_degrees, latitude_degrees):
        self.longitude_degrees = longitude_degrees
        self.latitude_degrees = latitude_degrees

    @property
    def longitude(self):
        return self.longitude_degrees * math.pi / 180

    @property
    def latitude(self):
        return self.latitude_degrees * math.pi / 180


class Zone:
    # attribut de classe
    ZONE = []
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1
    HEIGHT_DEGREES = 1
    EARTH_RADIUS_KILOMETERS = 6371

    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = []

    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)

    @property # car donne une info mais ne fait pas d'action
    def population(self):
        return len(self.inhabitants)

    @property
    def width(self):
        return abs(self.corner1.longitude - self.corner2.longitude) * self.EARTH_RADIUS_KILOMETERS

    @property
    def height(self):
        return abs(self.corner1.latitude - self.corner2.latitude) * self.EARTH_RADIUS_KILOMETERS

    @property
    def area(self):
        return self.height * self.width

    def population_density(self):
        return self.population/self.area

    @classmethod # niveau classe et non plus instance = méthode static
    def _initialize_zones(cls):
        for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude, latitude)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONE.append(zone)

    def contains(self, position):
        return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
               position.longitude < max(self.corner1.longitude, self.corner2.longitude) and \
               position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
               position.latitude < max(self.corner1.latitude, self.corner2.latitude)

    @classmethod
    def find_zone_that_contains(cls, position):
        # compute the index in the ZONE array that contains the given position
        if not cls.ZONE:
            cls._initialize_zones()
        longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES)/cls.WIDTH_DEGREES)
        latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES)/cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES)/cls.WIDTH_DEGREES) # 180 - (-180) / 1
        zone_index = latitude_index * longitude_bins + longitude_index

        # just checking that the index is correct
        zone = cls.ZONE[zone_index]
        assert zone.contains(position)

        return zone

    def average_agreeableness(self):
        if not self.inhabitants:
            return 0
        #agreeableness = []
        #for inhabitant in self.inhabitants:
        #agreeableness.append(inhabitant.agreeableness)
        #return sum(agreeableness) / self.population
        return sum([inhabitant.agreeableness for inhabitant in self.inhabitants])/self.population


class BaseGraph:

    def __init__(self):
        self.title = "graph"
        self.x_label = "x label"
        self.y_label = "y_label"
        self.show_grid = True

    def show(self, zones):
        x_values, y_values = self.xy_values(zones)
        plt.plot(x_values, y_values, '.')
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.grid(self.show_grid)
        plt.show()

    def xy_values(self, zones):
        raise NotImplementedError


class AgreeablenessGraph(BaseGraph): # inherit of BaseGraph

    def __init__(self):
        super().__init__() # launch the init of the parent class
        self.title = "nice people live in the countryside"
        self.x_label = "population density"
        self.y_label = "agreeableness"

    def xy_values(self, zones):
        x_values = [zone.population_density() for zone in zones]
        y_values = [zone.average_agreeableness() for zone in zones]
        return x_values, y_values


def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        # pop because the value have to be in Position but not in Agent
        latitude = agent_attributes.pop('latitude')
        longitude = agent_attributes.pop('longitude')
        position = Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)
        zone = Zone.find_zone_that_contains(position)
        zone.add_inhabitant(agent)
        #print(zone.average_agreeableness())

    agreeableness_graph = AgreeablenessGraph()
    agreeableness_graph.show(Zone.ZONE)

#agent_attributes = {"neuroticism": -0.0739192627121713, "language": "Shona", "latitude": -19.922097800281783, "country_tld": "zw", "age": 12, "income": 333, "longitude": 29.798455535838603, "sex": "Male", "religion": "syncretic", "extraversion": 1.051833688742943, "date_of_birth": "2005-01-10", "agreeableness": 0.1441229877537559, "id_str": "LB3-3Cl", "conscientiousness": 0.2419104411765549, "internet": 'false', "country_name": "Zimbabwe", "openness": -0.024607605122172617, "id": 6636726630}

main()
