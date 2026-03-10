from core.data_processor import DataProcessor


def test_within_range():
    dp = DataProcessor(100, 200)
    assert dp.is_within_range(150) is True
    assert dp.is_within_range(50) is False
    assert dp.is_within_range(250) is False


def test_boundary_values():
    dp = DataProcessor(100, 200)
    assert dp.is_within_range(100) is True   # inclusive start
    assert dp.is_within_range(200) is True   # inclusive end
