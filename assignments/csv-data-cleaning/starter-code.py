import csv
from pathlib import Path


def load_data(filename):
    """Load rows from a CSV file."""
    with open(filename, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def clean_name(value):
    """Standardize a name value."""
    if value is None:
        return ""
    return value.strip().title()


def clean_age(value):
    """Convert an age value to an integer when possible."""
    if value is None or value.strip() == "":
        return None
    try:
        return int(value)
    except ValueError:
        return None


# TODO: Add a function to clean the full dataset
# TODO: Add a function to create a summary report
# TODO: Save the cleaned data to a new CSV file
