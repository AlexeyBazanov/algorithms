import sys


"""
-- ID ПОСЫЛКИ - 52019094 --

-- ПРИНЦИП РАБОТЫ --
Создаются две хэш-таблицы: одна для хранения докумнтов, другая - для хранения вхождений слов в документы.
Далее алгоритм перебирает поочереди все документы, создавая хэш-ключ, методом полномиального хэширования.
В таблицу с документами по ключу текущего хэша сохраняется позиция текущего документа. 
Документы могут быть одинаковыми, а значит - иметь одинаковый хэш. 
Следовательно, нужно сохранять номера документов в массив. 

Далее алгоритм разбивает по пробелу текущий документ на массив слов и итерирует его. 
В таблицу со словами мы сохраняем пары хэш документа => количество вхождений, 
инкрементируя вхождения слова каждый раз, встречая его снова в документе.  
Так же мы добавляем признак сортировки в каждую ячейку со словом. 
Это свойство пригодится, когда мы будем выбирать наиболее релевантные документы.

Теперь алгоритм готов обработать запросы. 
В цикле итерируем запросы.
Создаем хэш-таблицу с отображением релевантости запроса к документам. 
Создаем хэш-таблицу для хранения уникальных слов в запросе.
Каждый запрос разбиваем на слова. Итерируем массив слов в цикле.
Проверяем, есть ли слово в таблице с уникальными словами запроса. Если есть - пропускаем итерацию.
Смотрим слово в созданной ранее таблице вхождений слов в документы.
Если слово найдено - сортируем таблицу с вхождениями для слова по убыванию. 
Помечаем, что данная таблица отсторировна, чтобы не сортировать ее каждый раз. 
Выбираем из остортированного словаря первые N документов (по условию задачи нам нужно выводить 5 документов).
Далее добавляем в таблицу релевантности хэш документа => кол-во вхождений, 
суммируя значение кол-ва вхождений, если документ уже присутствует в таблице ролевантности.
Добавляем слово в таблицу с уникальными словами запроса. 

Сортируем по убыванию созданную ранее таблицу релевантности.
Создаем хэш-таблицу с отображением релевантности на массив позиций документов.

Итерируем таблицу релевантности, сохраняя в новую хэш таблицу для каждого значения релевантности 
массив документов, взятый по хэш-ключу из таблицы с отображение документов.

Затем итерируем еще раз последнюю таблицу, сортируя документы в порядке возрастания. 
Остается только пробежаться по данной таблице еще раз и напечатать результат. 

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
n - документы
m - запросы

Перебор всех документов и создание карт слов и документов. 
Так как в документе k слов - О(n*k). 
Значение k может быть максимум 500. 
Можно принебречь этим значением. Итого O(n).

Обработка одного запроса. 
Так же как в докумете мы итерируем j слов. 
Слов в запросе максимум 50. Так же опускаем это значение.
Так же алгоритм произведет сортировки отображений слов на карты документнов => релевантности,
для всех уникальных слов в запросе.
Обозначим уникальные слова в запросе как q. Итого получим q * n*log(n). 
Так как очевидно, что q <= k - можно так же пренебречь этим значением. 
Итого получаем n*log(n). 
В итоге алгоритм создает представление хэш документа => релевантность. 
У нас получется зависимость от n документов. Производим быструю сортировку за n*log(n).
Далее получаем представление релевантность => массив номеров документов.
По условиям задачи мы ограничиваем количество возвращаемых значений числом r (5 по условию).
Чтобы отсортировать все номера документов во всех ключах релевантности, нужно сделать быстрые сортировки за r * n*log(n).
Значение r можно так же опустить -> n*log(n).
Итого у нас получается 3(n*log(n)), опускаем тройку - итого n*log(n).
В конечном счете, чтобы обработать m запросов придется сделать O(m * n*log(n)) операций.

Итого финальная асимптоматика - O(n) + m * n*log(n). 
Так как O(n*log(n)) доминирует над O(n), мы получаем O(m * n*log(n)). 

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Здесь проще. Нам понадобится дополнительно O(n) памяти для хранения таблицы документов 
и O(n) для хранения таблицы вхождений слов. Итого O(2n), двойку опускаем - O(n). 
"""


BASE = 239017
MOD = 1000000007
DOCS_KEY = 'docs'
SORTED_KEY = 'sorted'
FREQUENCY_KEY = 'frequency'
DOC_NUMS_KEY = 'doc_num'


def sort_dict(d, key, reverse=True):
    sorted_dict = {}
    sorted_tuples = sorted(d.items(), key=key, reverse=reverse)

    for i in sorted_tuples:
        sorted_dict[i[0]] = i[1]

    return sorted_dict


def add_doc(doc, doc_num, docs_map):
    doc_hash = hash(doc)
    if doc_hash not in docs_map:
        docs_map[doc_hash] = [doc_num]
        return doc_hash
    else:
        docs_map[doc_hash].append(doc_num)
        return False


def add_word(word, doc_hash, words_map):
    if word not in words_map:
        words_map[word] = {DOCS_KEY: {}, SORTED_KEY: False}

    if doc_hash not in words_map[word][DOCS_KEY]:
        words_map[word][DOCS_KEY][doc_hash] = 0

    words_map[word][DOCS_KEY][doc_hash] += 1


def sort_words_map(word, words_map):
    if not words_map[word][SORTED_KEY]:
        words_map[word][DOCS_KEY] = sort_dict(words_map[word][DOCS_KEY], key=lambda i: i[1])
        words_map[word][SORTED_KEY] = True


def get_most_frequent_docs(word, words_map, limit):
    sort_words_map(word, words_map)

    most_frequent_docs = {}
    last_frequency = -1
    i = 1

    for doc_hash, word_frequency in words_map[word][DOCS_KEY].items():
        most_frequent_docs[doc_hash] = word_frequency

        if word_frequency < last_frequency:
            i += 1

        if i > limit:
            break

        last_frequency = word_frequency

    return most_frequent_docs


def is_word_acceptable(word, words_map, unique_words_map):
    if word not in words_map:
        return False
    if word in unique_words_map:
        return False

    unique_words_map[word] = 0
    return True


def add_doc_frequency(doc_hash, relevant_docs, most_frequent_docs):
    if doc_hash not in relevant_docs:
        relevant_docs[doc_hash] = 0

    relevant_docs[doc_hash] += most_frequent_docs[doc_hash]


def get_relevant_docs(request, words_map, limit):
    relevant_docs = {}
    unique_words_map = {}

    for word in request.split(' '):
        if not is_word_acceptable(word, words_map, unique_words_map):
            continue

        most_frequent_docs = get_most_frequent_docs(word, words_map, limit)

        for doc_hash in most_frequent_docs:
            add_doc_frequency(doc_hash, relevant_docs, most_frequent_docs)

    return relevant_docs


def get_ordered_relevant_docs(relevant_docs, docs_map):
    docs_by_frequency = {}

    relevant_docs = sort_dict(relevant_docs, key=lambda x: x[1])

    for doc_hash in relevant_docs:
        frequency = relevant_docs[doc_hash]
        docs_numbers = docs_map[doc_hash]

        if frequency not in docs_by_frequency:
            docs_by_frequency[frequency] = []

        docs_by_frequency[frequency] += docs_numbers

    for frequency in docs_by_frequency:
        docs_by_frequency[frequency] = sorted(docs_by_frequency[frequency])

    return docs_by_frequency


def print_relevant_docs(ordered_relevant_docs, limit):
    output = ''
    docs_in_output = 0

    for frequency in ordered_relevant_docs:
        for doc_num in ordered_relevant_docs[frequency]:
            output += str(doc_num) + ' '
            docs_in_output += 1
            if docs_in_output >= limit:
                break

        if docs_in_output >= limit:
            break

    print(output.rstrip())


def save_input_to_maps(docs_map, words_map):
    docs_num = int(sys.stdin.readline().strip())

    for i in range(1, docs_num + 1):
        doc = sys.stdin.readline().strip()
        doc_hash = add_doc(doc, i, docs_map)

        if not doc_hash:
            continue

        for word in doc.split(' '):
            add_word(word, doc_hash, words_map)


def process_requests(docs_map, words_map, limit=5):
    requests_num = int(sys.stdin.readline().strip())

    for i in range(0, requests_num):
        requests = sys.stdin.readline().strip()
        relevant_docs = get_relevant_docs(requests, words_map, limit)
        relevant_docs = get_ordered_relevant_docs(relevant_docs, docs_map)
        print_relevant_docs(relevant_docs, limit)


def main():
    docs_map = {}
    words_map = {}

    save_input_to_maps(docs_map, words_map)
    process_requests(docs_map, words_map)


if __name__ == '__main__':
    main()
