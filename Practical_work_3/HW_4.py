def thesaurus_adv(*args):
    d = dict()
    for name in args:
        s0 = name.split()[1][0]
        s1 = name[0]
        if s0 not in d:
            d[s0] = dict()
            if s1 not in d[s0]:
                d[s0][s1] = []
            d[s0][s1].append(name)
        return d


print("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
