
from core.classifier import StageClassifier
from core.data_processor import DataProcessor
from core.models import Person, SleepReading

def main() -> None:
    person = Person()
    # processor = DataProcessor()
    classifier = StageClassifier()

    start_unix, end_unix = get_wake_window()
    processor = DataProcessor(start_unix, end_unix)

    while True:

        # simulate device reading
        raw_voltage = random.uniform(0, 5)

        # get current time
        current_time = time.time() #returns current unix time

        # check if reading should be processed
        if processor.is_within_range(current_time): #checks whether start_time <= current_time <= end_time

            cleaned = processor.read_input(raw_voltage)

            stage = classifier.get_stage(cleaned)

            reading = SleepReading( #creates a record containing time, cleaned voltage reading, and sleep stage
                time=current_time,
                voltage=cleaned,
                stage=stage
            )

            person.update_state(reading)

            # prints information to the terminal
            print("Voltage:", cleaned)
            print("Sleep stage:", stage)

            # wake during window if deep sleep
            if processor.is_within_range(current_time) and stage == "deep_sleep":
                person.wake_up()
                break

            # wake at the end of the window regardless of stage
            if current_time > processor.end_time:
                print("Wake window ended.")
                person.wake_up()
                break

        time.sleep(1)
