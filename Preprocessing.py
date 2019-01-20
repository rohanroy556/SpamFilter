import csv

import re
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

def clean_me(html):
    soup = BeautifulSoup(html)
    for s in soup(['script', 'style']):
        s.decompose()
    return ' '.join(soup.stripped_strings)

def string_cleaning(str):
    stop_words = set(stopwords.words('english'))
    str = re.sub(r'[^a-zA-Z0-9.@ \']+', '', str)
    #str = ' '.join(str.split())
    #filtered_sentence = list(set([w for w in str.split() if not w.lower() in stop_words]))
    #return ' '.join(filtered_sentence)
    return str

def data_cleaning(loc):
    rows = []
    with open(loc, "r+", encoding="utf-8", errors='ignore') as f:
        reader = csv.reader(f)
        for row in reader:
            row[0] = string_cleaning(row[0])
            row[1] = clean_me(row[1])
            row[1] = string_cleaning(row[1])
            m = re.findall(r'[\w\.-]+@[\w\.-]+', row[2])
            if len(m) != 0:
                row[2] = m[0]
            rows.append(row)
    writer = csv.writer(open('dataset/'+loc.split('/')[-1], 'w+', encoding='utf-8', newline=''))
    writer.writerows(rows)

def preprocessing(spams_loc, hams_loc):
    data_cleaning(spams_loc)
    data_cleaning(hams_loc)

def main():
    preprocessing('original dataset/Spams.csv', 'original dataset/Hams.csv')


if __name__ == '__main__':
    main()