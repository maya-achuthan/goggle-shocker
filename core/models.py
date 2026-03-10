from dataclasses import dataclass
from typing import List


@dataclass
class SleepReading:
    time: float
    voltage: float
    stage: str

class Person:
    def __init__(self) -> None:
        self.curr_stage: str = ""
        self.history: List[SleepReading] = []

    def update_state(self, reading: SleepReading) -> None:
        self.curr_stage = reading.stage
        self.history.append(reading)
