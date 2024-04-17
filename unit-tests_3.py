# Задание «Приложение для финансового планирования»
# Задайте первоначальные значения

salary = 100000  # Заработная плата
percent_mortgage = 30  # Ипотека
percent_life = 50  # На жизнь
in_year = 100000 * 12 # За год

# Напишите свой код здесь
mortgage = (salary * percent_mortgage / 100 ) * 12
percent_life_ = (salary * percent_life / 100 ) * 12
result = in_year - mortgage - percent_life_
print('Ипотека:', mortgage)
print('Накопления:', result)

import unittest

class TestCalculateSavings(unittest.TestCase):
    def test_calculate_savings_1(self):
        salary = 100000
        percent_mortgage = 30
        percent_life = 50
        in_year = salary * 12
        mortgage = (salary * percent_mortgage / 100) * 12
        percent_life_ = (salary * percent_life / 100) * 12
        expected_savings = in_year - mortgage - percent_life_
        self.assertEqual(result, expected_savings)

    def test_calculate_savings_2(self):
        salary = 50000
        percent_mortgage = 25
        percent_life = 40
        in_year = salary * 12
        mortgage = (salary * percent_mortgage / 100) * 12
        percent_life_ = (salary * percent_life / 100) * 12
        expected_savings = in_year - mortgage - percent_life_
        result = in_year - mortgage - percent_life_
        self.assertEqual(result, expected_savings)


if __name__ == '__main__':
    unittest.main()