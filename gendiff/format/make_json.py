import json


def make_dict_json(source):
    operators = ['+', '-', ' ']
    for i in list(source.keys()):
        if i[2] in operators:
            j = i[2:]
            source[j] = source[i]
            source.pop(i)
            if isinstance(source[j], dict):
                source[j] = make_dict_json(source[j])
        else:
            j = '  ' + i
            source[j] = source[i]
            source.pop(i)
            if isinstance(source[j], dict):
                source[j] = make_dict_json(source[j])
    return source


def make_json(source):
    source = make_dict_json(source)
    return json.dumps(source, indent=2)
