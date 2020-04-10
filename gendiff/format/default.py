ADDED, REMOVED, CHANGED, COMMON = 'added', 'removed', 'changed', 'common'


def packing_dict(source, j):
    result = '{' + '\n'
    result += '    ' * (j + 1) + str(list(source.keys())[0]) + ': '
    result += str(list(source.values())[0])
    result += '\n' + '    ' * j + '}' + '\n'
    return result


def format(source, j=0):
    result = '{' + '\n'
    for key, item in tuple(sorted(source.items())):
        if isinstance(item, dict):
            result += ('    ' * (j + 1)) + key + ': '
            result += format(item, j+1) + '\n'
        else:
            if item[0] == CHANGED:
                old, new = item[1]
                result += ('    ' * j) + '  + ' + key + ': '
                if isinstance(new, dict):
                    result += packing_dict(new, j+1)
                else:
                    result += str(new) + '\n'
                result = result + ('    ' * j) + '  - ' + key + ': '
                if isinstance(old, dict):
                    result += packing_dict(old, j+1)
                else:
                    result += str(old) + '\n'
            elif item[0] == ADDED:
                result += ('    ' * j) + '  + ' + key + ': '
                if isinstance(item[1], dict):
                    result += packing_dict(item[1], j+1)
                else:
                    result += str(item[1]) + '\n'
            elif item[0] == REMOVED:
                result += ('    ' * j) + '  - ' + key + ': '
                if isinstance(item[1], dict):
                    result += packing_dict(item[1], j+1)
                else:
                    result += str(item[1]) + '\n'
            else:
                result += ('    ' * j) + '    ' + key + ': '
                if isinstance(item[1], dict):
                    result += packing_dict(item[1], j+1)
                else:
                    result += str(item[1]) + '\n'
    if result[-1] != '}':
        result = result + ('    ' * j) + '}'
    else:
        result = result + '}'
    return result
