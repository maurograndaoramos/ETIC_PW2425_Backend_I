

class Rectangle:
    
    def __init__(self, width:int, height:int) -> None:
        self.width=width
        self.height=height

    def get_area(self) -> int:
        """
        Calculates the Rectangle's area
        """
        return self.width*self.height

    def get_perimeter(self)->int:
        return 2*self.height+2*self.width