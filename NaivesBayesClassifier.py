from General import *


def naive_bayes_classifer(testing_data):
    map_reader = read_csv('dataset/WordMap.csv')
    test_data = csv_to_list(read_csv(testing_data))
    result = write_csv('dataset/NaiveBayesResult.csv')
    word_map = {row[0].lower(): [row[1], row[2]] for row in map_reader}
    total_spams = 0
    total_hams = 0
    for word in word_map.keys():
        total_spams += int(word_map[word][0])
        total_hams += int(word_map[word][1])
    total_words = total_spams + total_hams
    p_spams = total_spams / total_words
    p_hams = total_hams / total_words
    print("Spam Word Count = %d, Ham Word Count = %d, Total Words = %d" %(total_spams, total_hams, total_words))
    for row in test_data:
        words = row[0].split() + row[1].split()
        words = list(map(str.lower, words))
        p_words_spam = p_words_ham = 1
        for word in list(set(words)):
            spam_count = int(word_map[word][0]) if word in word_map.keys() else 0
            ham_count = int(word_map[word][1]) if word in word_map.keys() else 0
            p_word_spam = (spam_count + 1) / (total_words + 2) if spam_count == 0 else spam_count / total_words
            p_word_ham = (ham_count + 1) / (total_words + 2) if ham_count == 0 else ham_count / total_words
            p_words_spam *= p_word_spam
            p_words_ham *= p_word_ham
        p_spam_words = p_words_spam * p_spams
        p_ham_words = p_words_ham * p_hams
        row.append('Spam' if p_spam_words > p_ham_words else 'Ham')
        result.writerow(row)
        print(row)

def main():
    # data_cleaning('original dataset/TestingData.csv')
    naive_bayes_classifer('dataset/TestingData.csv')


if __name__ == '__main__':
    main()
