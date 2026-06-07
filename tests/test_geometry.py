import unittest
from geomlib import (
    Circle,
    Hyperbola,
    Line,
    Line3D,
    Parabola,
    Plane,
    Point,
    Point3D,
    Polygon,
    Rectangle,
    Sphere,
    Square,
    Triangle,
    Vector2D,
    Vector3D,
    heron_area,
    section_formula,
)

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

    def test_triangle_centers_and_radii(self):
        triangle = Triangle(Point(0, 0), Point(6, 0), Point(0, 8))
        self.assertAlmostEqual(triangle.inradius(), 2)
        self.assertAlmostEqual(triangle.circumradius(), 5)
        self.assertEqual(triangle.incenter(), Point(2, 2))
        self.assertTrue(triangle.contains(Point(0, 4)))

    def test_line_circle_intersections(self):
        circle = Circle(Point(0, 0), 5)
        line = Line(Point(-10, 0), Point(10, 0))
        points = circle.line_intersections(line)
        self.assertEqual(len(points), 2)
        self.assertEqual(points[0], Point(-5, 0))
        self.assertEqual(points[1], Point(5, 0))

    def test_vector2d_operations(self):
        v = Vector2D(3, 4)
        self.assertEqual(v.magnitude(), 5)
        self.assertEqual(v.normalize(), Vector2D(0.6, 0.8))
        self.assertAlmostEqual(v.angle_with(Vector2D(1, 0)), 53.13010235415598)

    def test_polygon_area_centroid_and_contains(self):
        polygon = Polygon([Point(0, 0), Point(4, 0), Point(4, 3), Point(0, 3)])
        self.assertEqual(polygon.area(), 12)
        self.assertEqual(polygon.perimeter(), 14)
        self.assertEqual(polygon.centroid(), Point(2, 1.5))
        self.assertTrue(polygon.contains(Point(2, 2)))
        self.assertFalse(polygon.contains(Point(5, 2)))

    def test_conics(self):
        parabola = Parabola(Point(0, 0), 2, "up")
        self.assertEqual(parabola.focus(), Point(0, 2))
        self.assertEqual(parabola.directrix(), ("y", -2.0))
        self.assertTrue(parabola.contains(Point(4, 2)))

        hyperbola = Hyperbola(Point(0, 0), 3, 4)
        self.assertAlmostEqual(hyperbola.eccentricity(), 5 / 3)
        self.assertTrue(hyperbola.contains(Point(3, 0)))

    def test_3d_line_plane_geometry(self):
        line = Line3D(Point3D(0, 0, 0), Vector3D(1, 1, 1))
        plane = Plane.from_point_normal(Point3D(0, 0, 2), Vector3D(0, 0, 1))
        self.assertEqual(plane.line_intersection(line), Point3D(2, 2, 2))
        self.assertAlmostEqual(plane.distance_to_point(Point3D(0, 0, 5)), 3)

    def test_coordinate_formula_helpers(self):
        self.assertEqual(section_formula(Point(0, 0), Point(6, 6), 1, 2), Point(2, 2))
        self.assertEqual(heron_area(3, 4, 5), 6)

if __name__ == '__main__':
    unittest.main()
