import unittest

from src.fizzbuzz import fizzbuzz


class FizzBuzzTestCase(unittest.TestCase):

    def test_python_test_setup_works(self):
        self.assertTrue(True)

    def test_it_returns_1_when_number_is_1(self):
        # Arrange / Given

        # Act / When
        result = fizzbuzz(1)

        # Assert / Then
        self.assertEqual('1', result)

    def test_it_returns_2_when_number_is_2(self):
        # Arrange / Given

        # Act / When
        result = fizzbuzz(2)

        # Assert / Then
        self.assertEqual('2', result)

    def test_it_returns_fizz_when_number_is_3(self):
        # Arrange / Given

        # Act / When
        result = fizzbuzz(3)

        # Assert / Then
        self.assertEqual('fizz', result)

    def test_it_returns_buzz_when_number_is_5(self):
        # Arrange / Given

        # Act / When
        result = fizzbuzz(5)

        # Assert / Then
        self.assertEqual('buzz', result)
