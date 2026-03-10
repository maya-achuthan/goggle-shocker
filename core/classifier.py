class StageClassifier:
    def get_stage(self, voltage: float) -> str:
        if voltage > 2.5:
            return "n1"
        return "deep_sleep"
