from General import *
from Preprocessing import *


def data_to_list(data, m_type):
    data_list = []
    for row in data:
        words = row[0].split() + row[1].split()
        words = list(map(str.lower, words))
        count_map = {word: words.count(word) for word in list(set(words))}
        data_list.append([count_map, row[0], row[1], row[2], row[3]]) \
            if m_type == 'training' else data_list.append([count_map, row[0], row[1], row[2]])
    return data_list


def euclidean_distance(x, y):
    x_keys = list(x[0].keys())
    y_keys = list(y[0].keys())
    words = x_keys + y_keys
    words = list(set(words))
    dist = 0
    for word in words:
        if not word in x_keys: x[0].update({word: 0})
        if not word in y_keys: y[0].update({word: 0})
        dist += (x[0][word]-y[0][word])**2
    return dist**0.5


def knn_classifier(spam_loc='dataset/Spams.csv', ham_loc='dataset/Hams.csv', loc='dataset/TestingData.csv', k='5'):
    k = int(k)
    test_data = csv_to_list(read_csv(loc))      # read from loc and converts it to list
    spams = csv_to_list(read_csv(spam_loc))
    hams = csv_to_list(read_csv(ham_loc))
    result = write_csv('dataset/kNNResult.csv')     # knn result is store in a csv file
    spams = [spams[i] for i in range(100)]
    hams = [hams[i] for i in range(50)]
    training_data = data_to_list(spams + hams, 'training')      # 4 cols are there subject body sender and type
    test_data = data_to_list(test_data, 'testing')      # 3 cols are there subject body sender
    for test in test_data:
        dist_map = {}
        for train in training_data:
            dist = euclidean_distance(test, train)
            dist_map.update({dist: train})
        keys = sorted(list(dist_map.keys()))
        m_type = [dist_map[keys[i]][4] for i in range(k)]
        spam_count = m_type.count('Spam')
        ham_count = m_type.count('Ham')
        test.append('Spam' if spam_count > ham_count else 'Ham')
        row = [test[i] for i in range(1, 5)]
        result.writerow(row)
        print(row)


def main():
    # data_cleaning('original dataset/TestingData.csv')
    knn_classifier('dataset/TestingData.csv', '5')


if __name__ == '__main__':
    main()
