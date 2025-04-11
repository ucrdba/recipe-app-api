
"""
# set up test environment
"""

from django import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_add_numbers_tuple(self):
        print("test_add_numbers_tuple")
        """Test adding numbers together."""
        res = calc.add((5, 6))
        self.assertEqual(res, 11)

    def subtract_numbers(self):
        """Test subtracting numbers."""
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)    