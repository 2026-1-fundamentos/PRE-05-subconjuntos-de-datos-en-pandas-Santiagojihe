from __future__ import annotations
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_CSV = BASE_DIR / 'files' / 'input' / 'truck_event_text_partition.csv'
OUTPUT_CSV = BASE_DIR / 'files' / 'output' / 'specific-columns.csv'

SPECIFIC_COLUMNS = ['driverId', 'truckId', 'eventDate', 'eventType', 'longitude', 'latitude']


def generate_specific_columns() -> None:
    """Generate the specific-columns.csv subset from the input dataset."""
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(INPUT_CSV)
    df.to_csv(OUTPUT_CSV, columns=SPECIFIC_COLUMNS, index=False)


if __name__ == '__main__':
    generate_specific_columns()
