from General import *


def training(spam_loc='dataset/Spams.csv', ham_loc='dataset/Hams.csv'):
    spams = csv_to_list(read_csv(spam_loc))
    hams = csv_to_list(read_csv(ham_loc))
    spam_words = list_to_words(spams)
    ham_words = list_to_words(hams)
    words = list(set(spam_words + ham_words))
    spam_words = list(map(str.lower, spam_words))
    ham_words = list(map(str.lower, ham_words))
    writer = write_csv('dataset/WordMap.csv')
    for word in words:
        spam_count = spam_words.count(word.lower())
        ham_count = ham_words.count(word.lower())
        print(word, spam_count, ham_count)
        writer.writerow([word, spam_count, ham_count])


def main():
    training('dataset/Spams.csv', 'dataset/Hams.csv')


if __name__ == '__main__':
    main()
