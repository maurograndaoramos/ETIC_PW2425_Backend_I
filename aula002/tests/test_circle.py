import unittest
from ..circle import Circle

class CircleTests(unittest.TestCase):


    def setUp(self) -> None:
        self.circle = Circle(radious=5)

    
    def test_perimeter(self):
        assert 31.416 == round(self.circle.perimeter, 3)

    def test_area(self):
        assert 78.54 == round(self.circle.area, 2)


if __name__ == "__main__":
    unittest.main()