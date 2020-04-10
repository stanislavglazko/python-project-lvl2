ADDED, REMOVED, CHANGED, COMMON = 'added', 'removed', 'changed', 'common'


def format(source, j=''):
    keys = {ADDED, REMOVED, CHANGED}
    result = ''
    for key, item in tuple(sorted(source.items())):
        if isinstance(item, dict):
            result += format(item, j=(j+key+'.'))
        elif item[0] in keys:
            result += "Property '{}{}' was {}".format(str(j), key, item[0])
            if item[0] == CHANGED:
                old, new = item[1]
                result += ". From '{}' to '{}'\n".format(str(old), str(new))
            elif item[0] == ADDED:
                if isinstance(item[1], dict):
                    result += " with value: 'complex value'" + '\n'
                else:
                    result += " with value: '{}'\n".format(str(item[1]))
            elif item[0] == REMOVED:
                result += '\n'
    return result
