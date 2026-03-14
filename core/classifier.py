import numpy as np

class StageClassifier:

    """
        Args:
            data: Nx2 matrix (we're making this assumed format for now, can change later)
                  column 0 = time (seconds)
                  column 1 = proximity (16-bit IR value)
            baseline_minutes: amount of time used to compute baseline mean
    """
    def __init__(self, data, baseline_minutes=30):

        # convert data to numpy array for easier processing
        data = np.array(data)

        times = data[:, 0]
        proximities = data[:, 1]

        # determine baseline period
        baseline_limit = baseline_minutes * 60 #baseline minutes (30) converted to seconds
        baseline_values = proximities[times <= baseline_limit]

        # compute baseline mean (paper formula)
        self.mean = np.mean(baseline_values)


    """
    Returns True if the readout deviates more than 5% from the baseline mean.
    """
    def is_n1(self, voltage: float) -> bool:

        deviation = abs(voltage - self.mean) / self.mean
        return deviation > 0.05

    """
    Returns string value of the stage based on the readout.
    """
    def get_stage(self, voltage: float) -> str:
        return "n1" if self.is_n1(voltage) else "deep_sleep"