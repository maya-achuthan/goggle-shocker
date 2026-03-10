import unittest
from core.data_processor import DataProcessor


class TestDataProcessor(unittest.TestCase):
    def test_within_range(self):
        dp = DataProcessor(100, 200)
        self.assertTrue(dp.is_within_range(150))
        self.assertFalse(dp.is_within_range(50))
        self.assertFalse(dp.is_within_range(250))

    def test_boundary_values(self):
        dp = DataProcessor(100, 200)
        self.assertTrue(dp.is_within_range(100))   # inclusive start
        self.assertTrue(dp.is_within_range(200))   # inclusive end


if __name__ == "__main__":
    unittest.main()
