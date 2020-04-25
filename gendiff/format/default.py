from gendiff import diff


def pack_dict(source, j):
    result = '{' + '\n'
    result += '    ' * (j + 1) + str(list(source.keys())[0]) + ': '
    result += str(list(source.values())[0])
    result += '\n' + '    ' * j + '}' + '\n'
    return result


def add_dict(operator, key, item, j):
    result = ('    ' * j) + operator + key + ': '
    if isinstance(item, dict):
        result += pack_dict(item, j + 1)
    else:
        result += str(item) + '\n'
    return result


def final_pack(item1, item2, key, j):
    result = ''
    if item1 == diff.CHANGED:
        old, new = item2
        result += add_dict('  + ', key, new, j)
        result += add_dict('  - ', key, old, j)
    else:
        if item1 == diff.ADDED:
            result += add_dict('  + ', key, item2, j)
        elif item1 == diff.REMOVED:
            result += add_dict('  - ', key, item2, j)
        elif item1 == diff.COMMON:
            result += add_dict('    ', key, item2, j)
    return result


def format(source, j=0):
    result = '{' + '\n'
    for key, item in tuple(sorted(source.items())):
        if item[0] == diff.NESTED:
            result += ('    ' * (j + 1)) + key + ': '
            result += format(item[1], j+1) + '\n'
        else:
            result += final_pack(item[0], item[1], key, j)
    if result[-1] != '}':
        result = result + ('    ' * j) + '}'
    else:
        result = result + '}'
    return result
