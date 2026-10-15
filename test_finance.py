import unittest

from main import (
    calculate_profit_margin,
    calculate_roa,
    calculate_roe,
)


class TestFinanceIQ(unittest.TestCase):

    def test_profit_margin(self):
        result = calculate_profit_margin(100000, 15000)
        self.assertAlmostEqual(result, 15.0)

    def test_roa(self):
        result = calculate_roa(15000, 250000)
        self.assertAlmostEqual(result, 6.0)

    def test_roe(self):
        result = calculate_roe(15000, 120000)
        self.assertAlmostEqual(result, 12.5)

    def test_zero_revenue(self):
        with self.assertRaises(ValueError):
            calculate_profit_margin(0, 15000)


if __name__ == "__main__":
    unittest.main()