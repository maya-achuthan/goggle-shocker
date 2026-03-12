import numpy as np

class StageClassifier:

    def __init__(self, data, baseline_minutes=30):
        """
        Args:
            data: Nx2 matrix
                  column 0 = time (seconds)
                  column 1 = proximity (16-bit IR value)
            baseline_minutes: amount of time used to compute baseline mean
        """

        data = np.array(data)

        times = data[:, 0]
        proximities = data[:, 1]

        # determine baseline period
        baseline_limit = baseline_minutes * 60
        baseline_values = proximities[times <= baseline_limit]

        # compute baseline mean (paper formula)
        self.mean = np.mean(baseline_values)


    def is_n1(self, voltage: float) -> bool:
        """
        Returns True if the voltage deviates more than 5% from the baseline mean.
        """

        deviation = abs(voltage - self.mean) / self.mean
        return deviation > 0.05


    def get_stage(self, voltage: float) -> str:
        return "n1" if self.is_n1(voltage) else "deep_sleep"