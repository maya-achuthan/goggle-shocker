
from core.classifier import StageClassifier
from core.data_processor import DataProcessor
from core.models import Person, SleepReading


def main() -> None:
    person = Person()
    # processor = DataProcessor()
    classifier = StageClassifier()


    # start reading from the device
    # see if within time range
    # if so, classify the reading
    # wake up person if they are in deep sleep
    # FUTURE: save data to the data/stages.json

if __name__ == "__main__":
    main()
