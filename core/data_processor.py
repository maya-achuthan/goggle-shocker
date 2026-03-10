class DataProcessor:
    def __init__(self, start_time: float, end_time: float) -> None:
        self.start_time = start_time
        self.end_time = end_time

start = float(input("Enter start time: "))
end = float(input("Enter end time: "))
        
processor = DataProcessor(start, end)

    def is_within_range(self, current_time: float) -> bool:
        return self.start_time <= current_time <= self.end_time

    def read_input(self, raw_data: float) -> float:
        return self.clean_input(raw_data)

    def clean_input(self, voltage: float) -> float:
        return voltage
