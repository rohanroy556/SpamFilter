import csv


def csv_to_list(reader):
    rows = []
    for row in reader:
        rows.append(row)
    return rows

def list_to_words(list):
    words = []
    for row in list:
        words += row[0].split() + row[1].split()
    return words

def read_csv(loc):
    return csv.reader(open(loc, encoding="utf-8", errors='ignore'))

def write_csv(loc):
    return csv.writer(open(loc, 'w+', encoding='utf-8', newline=''))
