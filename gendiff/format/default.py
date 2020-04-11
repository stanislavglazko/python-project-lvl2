ADDED, REMOVED, CHANGED, COMMON = 'added', 'removed', 'changed', 'common'


def packing_dict(source, j):
    result = '{' + '\n'
    result += '    ' * (j + 1) + str(list(source.keys())[0]) + ': '
    result += str(list(source.values())[0])
    result += '\n' + '    ' * j + '}' + '\n'
    return result


def adding_dict(operator, key, item, number):
    result = ('    ' * number) + operator + key + ': '
    if isinstance(item, dict):
        result += packing_dict(item, number + 1)
    else:
        result += str(item) + '\n'
    return result


def final_packing(item1, item2, key, j):
    result = ''
    if item1 == CHANGED:
        old, new = item2
        result += adding_dict('  + ', key, new, j)
        result += adding_dict('  - ', key, old, j)
    else:
        if item1 == ADDED:
            result += adding_dict('  + ', key, item2, j)
        elif item1 == REMOVED:
            result += adding_dict('  - ', key, item2, j)
        elif item1 == COMMON:
            result += adding_dict('    ', key, item2, j)
    return result


def format(source, j=0):
    result = '{' + '\n'
    for key, item in tuple(sorted(source.items())):
        if isinstance(item, dict):
            result += ('    ' * (j + 1)) + key + ': '
            result += format(item, j+1) + '\n'
        else:
            result += final_packing(item[0], item[1], key, j)
    if result[-1] != '}':
        result = result + ('    ' * j) + '}'
    else:
        result = result + '}'
    return result
