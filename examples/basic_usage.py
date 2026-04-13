from geomlib import Point, Circle, Rectangle, Square, Triangle, Sphere, Point3D

def main():
    print("=== 2D Geometry Examples ===\n")
    
    # Points
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print(f"Distance between {p1} and {p2}: {p1.distance_to(p2):.2f}")
    
    # Circle
    circle = Circle(Point(0, 0), 5)
    print(f"\nCircle at {circle.center} with radius {circle.radius}")
    print(f"Area: {circle.area():.2f}")
    print(f"Circumference: {circle.perimeter():.2f}")
    
    # Rectangle
    rect = Rectangle(Point(0, 0), 10, 5)
    print(f"\nRectangle: {rect}")
    print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}")
    print(f"Center: {rect.center}")
    
    # Square
    square = Square(Point(0, 0), 4)
    print(f"\nSquare: {square}")
    print(f"Area: {square.area()}, Diagonal: {square.diagonal():.2f}")
    
    # Triangle
    triangle = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))
    print(f"\nTriangle: {triangle}")
    print(f"Area: {triangle.area()}, Perimeter: {triangle.perimeter():.2f}")
    print(f"Angles: {triangle.angles()}")
    
    print("\n=== 3D Geometry Examples ===\n")
    
    # 3D Point
    p3d = Point3D(1, 2, 3)
    print(f"3D Point: {p3d}")
    print(f"Distance to origin: {p3d.distance_to_origin():.2f}")
    
    # Sphere
    sphere = Sphere(Point3D(0, 0, 0), 3)
    print(f"\nSphere at {sphere.center} with radius {sphere.radius}")
    print(f"Volume: {sphere.volume():.2f}")
    print(f"Surface Area: {sphere.surface_area():.2f}")

if __name__ == "__main__":
    main()