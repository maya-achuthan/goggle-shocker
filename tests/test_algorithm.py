import unittest
from core.classifier import StageClassifier


class TestStageClassifier(unittest.TestCase):
    # TODO: CHANGE THESE TO ACTUALLY TEST THE ALGORITHM
    def test_stage_logic(self):
        sc = StageClassifier()
        self.assertEqual(sc.get_stage(3.0), "n1")
        self.assertEqual(sc.get_stage(1.0), "deep_sleep")

    def test_boundary_threshold(self):
        sc = StageClassifier()
        self.assertEqual(sc.get_stage(2.5), "deep_sleep")  # not strictly greater
        self.assertEqual(sc.get_stage(2.51), "n1")


if __name__ == "__main__":
    unittest.main()