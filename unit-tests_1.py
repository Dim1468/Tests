# Задание «Площадь и периметр квадрата»
a = 6  # Сторона квадрата

perimeter = 4 * a  # Расчёт периметра
area = a ** 2  # Расчёт площади

print('Периметр:', perimeter)
print('Площадь:', area)

import unittest

def calculate_perimeter(a):
    return 4 * a

def calculate_area(a):
    return a ** 2

class TestCalculations(unittest.TestCase):

    def test_calculate_perimeter(self):
        self.assertEqual(calculate_perimeter(6), 24)
        self.assertEqual(calculate_perimeter(0), 0)
        self.assertEqual(calculate_perimeter(10), 40)

    def test_calculate_area(self):
        self.assertEqual(calculate_area(6), 36)
        self.assertEqual(calculate_area(0), 0)
        self.assertEqual(calculate_area(10), 100)

if __name__ == '__main__':
    unittest.main()
