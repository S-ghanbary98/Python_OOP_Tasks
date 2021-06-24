

class Area:
    def __init__(self):


    def circle_area(self, radius):
        return self.radius * self.radius * 3.14

    def circle_perimeter(self, radius):
        return radius * 2 * 3.14

m = Area(5)
print(m.circle_area(5))