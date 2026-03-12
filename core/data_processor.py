from datetime import datetime, timedelta

class DataProcessor:
    def __init__(self):
        self.start_time, self.end_time = self.get_wake_window()

    def get_wake_window(self):

        while True:
            start_input = input("Enter start time (e.g. 6:10am): ")
            end_input = input("Enter end time (e.g. 6:40am): ")

            try:
                start_time = datetime.strptime(start_input, "%I:%M%p")
                end_time = datetime.strptime(end_input, "%I:%M%p")

                difference = end_time - start_time

                if difference == timedelta(minutes=30):
                    start_unix = start_time.timestamp()
                    end_unix = end_time.timestamp()
                    return start_unix, end_unix
                else:
                    print("The window must be exactly 30 minutes. Try again.\n")

            except:
                print("Invalid time format. Try again.\n")
            
    def is_within_range(self, current_time: float) -> bool:
        return self.start_time <= current_time <= self.end_time

    def read_input(self, raw_data: float) -> float:
        return self.clean_input(raw_data)

    def clean_input(self, voltage: float) -> float:
        return voltage
