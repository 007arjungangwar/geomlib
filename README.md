# 📦 GeomLib - Advanced Geometry Library

A powerful and easy-to-use Python library for performing **2D and 3D geometric computations**.

---

## ✨ Features

### 🔷 2D Geometry

* Point, Line, Circle
* Square, Rectangle, Rhombus
* Parallelogram, Triangle, Ellipse

### 🔶 3D Geometry

* Point3D, Sphere
* Cube, Cuboid
* Cylinder, Cone

### 📐 Mathematical Operations

* Area, Perimeter
* Volume, Surface Area
* Distance calculations

### 🔍 Geometric Relations

* Intersection checking
* Containment tests

### 🔄 Transformations

* Translation
* Rotation
* Scaling

### ➕ Vector Operations

* Dot product
* Cross product
* Magnitude
* Normalization

---

## 📥 Installation

Install directly from PyPI:

```bash
pip install geomlib-advanced
```

---

## 🚀 Quick Start

```python
from geomlib import Point, Circle, Rectangle, Sphere

# -------------------
# 2D Geometry
# -------------------
circle = Circle(center=Point(0, 0), radius=5)

print("Circle Area:", circle.area())          # 78.54
print("Circle Perimeter:", circle.perimeter()) # 31.42

# -------------------
# 3D Geometry
# -------------------
sphere = Sphere(center=(0, 0, 0), radius=3)

print("Sphere Volume:", sphere.volume())           # 113.10
print("Sphere Surface Area:", sphere.surface_area())  # 113.10

# -------------------
# Shape Relationships
# -------------------
rect = Rectangle(Point(0, 0), width=10, height=5)

print("Point inside rectangle:", rect.contains(Point(2, 2)))  # True
```

---

## 💡 Example Output

```
Circle Area: 78.54
Circle Perimeter: 31.42
Sphere Volume: 113.10
Sphere Surface Area: 113.10
Point inside rectangle: True
```

---

## 📚 Use Cases

* Educational purposes (learning geometry)
* Competitive programming
* Game development (collision detection)
* Computer graphics and simulations
* AI/ML projects involving spatial data

---

## ⚙️ Requirements

* Python 3.7+

---

## 🛠️ Installation from Source

```bash
git clone https://github.com/007arjungangwar/geomlib.git
cd geomlib
pip install .
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Arjun Singh Gangwar**

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!
