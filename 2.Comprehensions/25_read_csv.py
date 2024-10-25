import csv


def read_csv(filename):
    """
    Reads a CSV file and returns its contents as a list of dictionaries.

    Args:
        filename (str): The path to the CSV file to be read.

    Returns:
        list of dict: A list where each element is a dictionary representing a row in the CSV file.
                      The keys of the dictionary are the column headers, and the values are the corresponding data.
    """
    with open(filename) as f:
        reader = csv.DictReader(f, delimiter=",")
        return [row for row in reader]


if __name__ == "__main__":
    data = read_csv("data.csv")
    print(data)
