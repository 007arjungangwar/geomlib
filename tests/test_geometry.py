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
    RelationResult,
    Sphere,
    Square,
    Triangle,
    Vector2D,
    Vector3D,
    heron_area,
    line_circle_relation,
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

    def test_line_circle_relations(self):
        circle = Circle(Point(0, 0), 5)
        tangent = Line(Point(-10, 5), Point(10, 5))
        secant = Line(Point(-10, 0), Point(10, 0))
        outside = Line(Point(-10, 6), Point(10, 6))

        tangent_relation = circle.relation_to_line(tangent)
        self.assertIsInstance(tangent_relation, RelationResult)
        self.assertEqual(tangent_relation.kind, "tangent")
        self.assertTrue(tangent_relation.touches)
        self.assertEqual(tangent_relation.intersections, (Point(0, 5),))
        self.assertTrue(tangent.is_tangent_to_circle(circle))

        secant_relation = line_circle_relation(secant, circle)
        self.assertEqual(secant_relation.kind, "secant")
        self.assertTrue(secant_relation.cuts)
        self.assertEqual(secant_relation.intersections, (Point(-5, 0), Point(5, 0)))
        self.assertEqual(circle.chord_length_from_line(secant), 10)
        self.assertTrue(circle.is_secant_to_line(secant))

        outside_relation = outside.relation_to_circle(circle)
        self.assertEqual(outside_relation.kind, "outside")
        self.assertTrue(outside_relation.disjoint)

    def test_segment_circle_relations(self):
        circle = Circle(Point(0, 0), 5)
        segment_secant = Line(Point(-6, 0), Point(6, 0))
        segment_inside = Line(Point(-1, 0), Point(1, 0))
        segment_crossing = Line(Point(0, 0), Point(10, 0))

        self.assertEqual(segment_secant.segment_relation_to_circle(circle).kind, "segment_secant")
        self.assertEqual(segment_inside.segment_relation_to_circle(circle).kind, "segment_inside")
        crossing = segment_crossing.segment_relation_to_circle(circle)
        self.assertEqual(crossing.kind, "segment_crossing")
        self.assertEqual(crossing.intersections, (Point(5, 0),))

    def test_circle_circle_relation_points(self):
        c1 = Circle(Point(0, 0), 5)
        c2 = Circle(Point(8, 0), 5)
        relation = c1.relation(c2)

        self.assertEqual(relation.kind, "intersecting")
        self.assertEqual(len(relation.intersections), 2)
        self.assertAlmostEqual(relation.intersections[0].x, 4)
        self.assertAlmostEqual(abs(relation.intersections[0].y), 3)

    def test_line_rectangle_relation(self):
        rect = Rectangle(Point(0, 0), 4, 3)
        line = Line(Point(-1, 1), Point(5, 1))
        relation = line.relation_to_rectangle(rect)

        self.assertEqual(relation.kind, "cutting")
        self.assertEqual(relation.intersections, (Point(4, 1), Point(0, 1)))

    def test_line_sphere_relations(self):
        sphere = Sphere(Point3D(0, 0, 0), 5)
        tangent = Line3D(Point3D(-10, 5, 0), Vector3D(1, 0, 0))
        secant = Line3D(Point3D(-10, 0, 0), Vector3D(1, 0, 0))

        self.assertEqual(tangent.relation_to_sphere(sphere).kind, "tangent")
        self.assertTrue(tangent.is_tangent_to_sphere(sphere))
        secant_relation = secant.relation_to_sphere(sphere)
        self.assertEqual(secant_relation.kind, "secant")
        self.assertTrue(secant.is_secant_to_sphere(sphere))
        self.assertEqual(secant_relation.intersections, (Point3D(-5, 0, 0), Point3D(5, 0, 0)))

if __name__ == '__main__':
    unittest.main()
