input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
length_list: int = len(input_list)

for i in range(length_list):
    elem = input_list.pop(0)

    if elem.isdigit() and elem.isalnum():
        input_list.append(f'"{int(elem):02d}"')

    elif elem[0] == "+" and elem[1].isdigit():
        input_list.append(f'"+{int(elem):02d}"')

    else:
        input_list.append(elem)

print(' '.join(input_list))
