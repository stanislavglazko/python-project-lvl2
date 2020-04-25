from gendiff import diff


def format_engine(source, j):
    keys = {diff.ADDED, diff.REMOVED, diff.CHANGED}
    result = ''
    for key, item in tuple(sorted(source.items())):
        if item[0] == diff.NESTED:
            result += format_engine(item[1], j=(j+key+'.'))
        elif item[0] in keys:
            status = item[0]
            value = item[1]
            result += "Property '{}{}' was {}".format(j, key, status)
            if status == diff.CHANGED:
                old, new = value
                result += ". From '{}' to '{}'\n".format(old, new)
            elif status == diff.ADDED:
                if isinstance(value, dict):
                    result += " with value: 'complex value'" + '\n'
                else:
                    result += " with value: '{}'\n".format(value)
            elif status == diff.REMOVED:
                result += '\n'
    return result


def format(source):
    return format_engine(source, j='')
