from calculatorOperations import Calculator

class Functional_Calculator(Calculator):
    def __init__(self):
        super().__init__()

    def circle_area(self, radius):
        area = radius ** 2 * math.pi

        if (area - math.floor(area)) <= 0.49:
            return math.floor(area)
        else:
            return math.ceil(area)

    def square_area(self, length):
        area = length ** 2

        if (area - math.floor(area)) <= 0.49:
            return math.floor(area)
        else:
            return math.ceil(area)

    def equilateral_triangle_area(self, length):
        area = 0.433 * (length ** 2)

        if (area - math.floor(area)) <= 0.49:
            return math.floor(area)
        else:
            return math.ceil(area)

