import math
class Circle:
    
    def __init__(self, radious: int) -> None:
        self.radious = radious


    @property
    def perimeter(self)->float:
        return 2*math.pi*self.radious

    @property
    def area(self)-> float:
        return math.pi*self.radious**2