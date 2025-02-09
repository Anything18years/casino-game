import math 
class Circle:
    def __init__(self,radius: float):
        self.radius = radius
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_from_point(self,other: "Point3D"):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)
    def __eq__(self,other: "Point3D"):
        if isinstance(other,Point3D):
            return self.x == other.x and self.y ==  other.y and self.z == other.z
        return False
    def __repr__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"
    

class Sphere:
    def __init__(self,centre_point: Point3D,radius: float):
        self.radius = radius
        self.centre_point = centre_point
    def diameter(self) -> float:
        return 2 * self.radius

    def surface_area(self) -> float:
        return 4 * math.pi * self.radius**2

    def volume(self) -> float:
        return (4 / 3) * math.pi * self.radius**3
    
    def distance_between_centres(self, other: "Sphere"):
        return self.centre_point.distance_from_point(other.centre_point)

    def distance_between_edges(self, other: "Sphere"):
        return self.distance_between_centres(other) - self.radius - other.radius
    def overlaps(self, other: "Sphere"):
        return self.distance_between_edges(other) <= 0 
    def __eq__(self, other) -> bool:

        if isinstance(other,Sphere):
            return self.centre_point == other.centre_point and self.radius == other.radius
        return False
    
    def __repr__(self):
         return f"Sphere(centre_point={self.centre_point}, radius={self.radius})"

import unittest

class SphereTest(unittest.TestCase):
    def test_sphere_centre_point_returns_correct_position3D(self):
        sphere = Sphere(Point3D(3,2,1),11)
        self.assertEqual(Point3D(3,2,1),sphere.centre_point)
    def test_sphere_radius_returns_correct_radius(self):
        sphere = Sphere(Point3D(3,2,1),11)
        self.assertEqual(11,sphere.radius)
    def test_equals_on_equal_spheres_returns_true(self):
        sphere_a = Sphere(Point3D(1, 2, 3), 1)
        sphere_b = Sphere(Point3D(1, 2, 3), 1)
        self.assertEqual(sphere_a, sphere_b)

    def test_equals_on_not_equal_spheres_returns_false(self):
        sphere_a = Sphere(Point3D(1, 2, 3), 1)
        sphere_b = Sphere(Point3D(1, 2, 3), 2)
        self.assertNotEqual(sphere_a, sphere_b)

    def test_equal_on_sphere_and_string_returns_false(self):
        sphere = Sphere(Point3D(1, 2, 3), 4)
        self.assertNotEqual("Sphere(centre_point=Point3D(x=1, y=2, z=3), radius=4)", sphere)

    def test_repr_arbitrary_sphere_returns_correct_string(self):
        sphere = Sphere(Point3D(1, 2, 3), 4)
        self.assertEqual("Sphere(centre_point=Point3D(x=1, y=2, z=3), radius=4)", str(sphere))
    def test_diameter_various_spheres_return_correct_diameter(self):
        cases=  [ 
            Sphere(Point3D(0,0,0),0),
            Sphere(Point3D(0,0,0),1),
            Sphere(Point3D(1,1,1),0),
            Sphere(Point3D(10,11,12),10.1),

        ]
        expecteds = [0,2,0,20.2]
        for (case,expect) in zip(cases, expecteds):
            with self.subTest():
                self.assertAlmostEqual(case.diameter(),expect,5)

unittest.main(argv=[''], verbosity=2, exit=False)