# Задание «Площадь и периметр прямоугольника»
a = 5  # Сторона A
b = 7  # Сторона B

perimeter = 2 * (a + b)  # Расчёт периметра
area = a * b  # Расчёт площади

print('Периметр:', perimeter)
print('Площадь:', area)

import unittest

def calculate_perimeter(a, b):
    return 2 * (a + b)

def calculate_area(a, b):
    return a * b

class TestGeometryCalculations(unittest.TestCase):

    def test_perimeter_calculation(self):
        self.assertEqual(calculate_perimeter(5, 7), 24)

    def test_area_calculation(self):
        self.assertEqual(calculate_area(5, 7), 35)

if __name__ == '__main__':
    unittest.main()