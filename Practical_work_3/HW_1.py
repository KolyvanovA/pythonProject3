def num_translate_adv(eng_num):
    dict_num = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'десять': 'ten'}
    if eng_num.lower() in dict_num:
        print(dict_num[eng_num.lower()].capitalize() if eng_num[0:1].isupper() else dict_num[eng_num.lower()])
    else:
        print('None')


num_translate_adv("One")

num_translate_adv("two")
