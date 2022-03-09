import random


def get_jokes(n, no_repeat=True):
    """
    Функция возвращающая n случайных шуток.

    :param n: Количество шуток для генерации.
    :return: Список шуток.
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    for i in range(n):
        words = list(map(random.choice, (nouns, adverbs, adjectives)))
        joke = ' '.join(words)
        jokes.append(joke)
        if no_repeat:
            for el in words:
                nouns = list(filter(lambda x: x != el, nouns))
                adverbs = list(filter(lambda x: x != el, adverbs))
                adjectives = list(filter(lambda x: x != el, adjectives))
    return jokes


print(get_jokes(5))
