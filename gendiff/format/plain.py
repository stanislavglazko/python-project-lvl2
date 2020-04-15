from gendiff.diff import ADDED, REMOVED, CHANGED


def format(source, j=''):
    keys = {ADDED, REMOVED, CHANGED}
    result = ''
    for key, item in tuple(sorted(source.items())):
        if isinstance(item, dict):
            result += format(item, j=(j+key+'.'))
        elif item[0] in keys:
            status = item[0]
            value = item[1]
            result += "Property '{}{}' was {}".format(j, key, status)
            if status == CHANGED:
                old, new = value
                result += ". From '{}' to '{}'\n".format(old, new)
            elif status == ADDED:
                if isinstance(value, dict):
                    result += " with value: 'complex value'" + '\n'
                else:
                    result += " with value: '{}'\n".format(value)
            elif status == REMOVED:
                result += '\n'
    return result
