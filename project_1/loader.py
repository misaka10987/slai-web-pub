import csv


def load(path: str) -> dict:
    res = {}
    file = open(path, "r")
    reader = csv.DictReader(file)
    arr = [e for e in reader]
    print(arr)
    for element in arr:
        res[int(element["AtomicNumber"])] = element
    return res
