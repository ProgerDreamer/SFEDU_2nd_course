import pickle as pk


def read_dict():
    out_dict = dict()
    allowed_types = ['int', 'float', 'str', 'bool', 'list_', 'list_int', 'list_float']
    types_str = ''
    for type_ in allowed_types:
        types_str += type_ + ' '
    print('Enter you dictionary: ')
    print('Use format: "key1:val1:val_type1 key2:val_2:val_type2",')
    print(f'valid values for val_type: {types_str}')
    print('for list values use format: "key:elem1;elem2;elem3"')
    print('for set values use format: "key:elem1;elem2;elem3:set"')
    data = input().split()
    for i, item in enumerate(data):
        item = item.split(':')
        if ';' in item[1]:
            values = item[1].split(';')
            try:
                for i1, _ in enumerate(values):
                    values[i1] = int(values[i1])
            except ValueError:
                try:
                    for i1, _ in enumerate(values):
                        values[i1] = float(values[i1])
                except ValueError:
                    for i1, _ in enumerate(values):
                        values[i1] = str(values[i1])
            try:
                if item[2] == 'set':
                    out_dict[item[0]] = set(values)
                else:
                    out_dict[item[0]] = values
            except IndexError:
                out_dict[item[0]] = values
        else:
            try:
                out_dict[item[0]] = int(item[1])
            except ValueError:
                try:
                    out_dict[item[0]] = float(item[1])
                except ValueError:
                    out_dict[item[0]] = item[1]
    return out_dict


data_dict = read_dict()
# data_dict = {'kurs': 2, 'group': 6, 'name': 'Liza', 'stature':150, 'weight': 50.5}

with open('dict_file.pickle', 'wb') as f:
    pk.dump(data_dict, f)

with open('dict_file.pickle', 'rb') as f:
    new_data_dict = pk.load(f)

print(new_data_dict)
