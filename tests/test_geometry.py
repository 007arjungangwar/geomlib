import unittest
from geomlib import Point, Circle, Rectangle, Square, Triangle, Sphere, Point3D

class TestGeometry(unittest.TestCase):
    
    def test_point_distance(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        self.assertEqual(p1.distance_to(p2), 5.0)
    
    def test_circle_area(self):
        circle = Circle(Point(0, 0), 5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)
    
    def test_rectangle_area(self):
        rect = Rectangle(Point(0, 0), 10, 5)
        self.assertEqual(rect.area(), 50)
    
    def test_square_perimeter(self):
        square = Square(Point(0, 0), 4)
        self.assertEqual(square.perimeter(), 16)
    
    def test_triangle_area(self):
        triangle = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))
        self.assertEqual(triangle.area(), 6)
    
    def test_sphere_volume(self):
        sphere = Sphere(Point3D(0, 0, 0), 3)
        self.assertAlmostEqual(sphere.volume(), 113.09733552923255)

if __name__ == '__main__':
    unittest.main()