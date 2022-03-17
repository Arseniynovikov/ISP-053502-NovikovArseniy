import re


def n_gram(text, n, k):
    text = text.replace(',', '').replace(',', '').replace('!', '').replace('?', '').replace(' ', '')
    i = 0
    j = 0
    gram_numbers = dict()
    while i < len(text) - (n + 1):
        gram = text[i: i + n]
        if gram not in gram_numbers:
            gram_numbers[gram] = 0
            while j < len(text):
                gram_buf = text[j: j + n]
                if gram == gram_buf:
                    gram_numbers[gram] += 1
                j += 1
            j = 0
        i += 1
    j = 0

    while j < k:
        max_value = 0
        max_key = ""
        for key in gram_numbers:
            if gram_numbers[key] > max_value:
                max_value = gram_numbers[key]
                max_key = key
        j += 1
        print(f"{max_key} : {max_value}")
        del gram_numbers[max_key]


def median(text):
    text = re.split("[.!?]", text)
    text.pop()
    for sent in text:
        number = list()
        word_dic = dict()
        sent_buf = sent.split()
        for word_key in sent_buf:
            if word_key in word_dic:
                word_dic[word_key] += 1
            else:
                word_dic[word_key] = 1
        for ind in word_dic:
            number.append(word_dic[ind])
        number.sort()
        print(f"Median value:\"{number}\": {number[len(number) // 2]}")
        number.clear()


def count(text):
    text = text.replace('. ', ' ').replace('?', ' ').replace('! ', ' ')
    word_dic = dict()
    text = text.split()
    for word_key in text:
        if word_key in word_dic:
            word_dic[word_key] += 1
        else:
            word_dic[word_key] = 1
    return word_dic


def awer_count(text):
    sent_list = re.split("[.?!]", text)
    sent_list.pop()
    print(sent_list)
    count_dict = dict()
    _count = 0
    for sent in sent_list:
        count_dict[sent] = 0
        for char in sent:
            if char == " ":
                count_dict[sent] += 1
        _count += count_dict[sent]
    a_count = _count / len(sent_list)
    print(a_count)


def input_txt():
    with open("text") as file:
        text = file.read()
    text = text.replace('\n', ' ').replace(':', '').replace(',', '').replace('-', '').replace(';', '').lower()
    return text


def main():
    text = input_txt()
    print(count(text))
    awer_count(text)
    median(text)
    ex = False
    while ex is False:
        try:
            ch = input("n = 4, r = 10? (y/n) ")
            if ch == 'y':
                n = 4
                k = 10
                ex = True
            else:
                n = int(input("n ="))
                k = int(input("k ="))
                ex = True
        except:
            print("Wrong numbers.")
            ex = False

    n_gram(text, n, k)


main()
