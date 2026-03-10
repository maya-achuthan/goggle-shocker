from core.classifier import StageClassifier

# TODO: CHANGE THESE TO ACTUALLY TEST THE ALGORITHM 
def test_stage_logic():
    sc = StageClassifier()
    assert sc.get_stage(3.0) == "n1"
    assert sc.get_stage(1.0) == "deep_sleep"


def test_boundary_threshold():
    sc = StageClassifier()
    assert sc.get_stage(2.5) == "deep_sleep"  # not strictly greater
    assert sc.get_stage(2.51) == "n1"
