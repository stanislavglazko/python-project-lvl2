import json
import yaml


def converting(source):
    name = source.split('.')[-1]
    if name == 'yml':
        source = yaml.safe_load(open(source))
    elif name == 'json':
        source = json.load(open(source))
    return source


def diff(source1, source2):
    common = sorted(list(source1.keys() & source2.keys()))
    only_before = sorted(list(source1.keys() - source2.keys()))
    only_after = sorted(list(source2.keys() - source1.keys()))
    result = {}
    for i in common:
        if source1[i] == source2[i]:
            result[('    ' + i)] = str(source1[i])
        if source1[i] != source2[i]:
            if type(source1[i]) == dict and type(source2[i]) == dict:
                result[('    ' + i)] = diff(source1[i], source2[i])
            else:
                result[('  + ' + i)] = source2[i]
                result[('  - ' + i)] = source1[i]
    for i in only_before:
        result[('  - ' + i)] = source1[i]
    for i in only_after:
        result[('  + ' + i)] = source2[i]
    return result


def rendering(source, j=0):
    result = '{' + '\n'
    for i in list(source.keys()):
        if isinstance(source[i], dict):
            result += ('\t' * j) + i + ': ' + rendering(source[i], j+1) + '\n'
        else:
            if i[0] != ' ':
                result += ('\t' * (j + 1)) + i + ': ' + str(source[i]) + '\n'
            else:
                result += ('\t' * j) + i + ': ' + str(source[i]) + '\n'
    if result[-1] == '}':
        result = result + '\n' + '}'
    else:
        result = result + ('\t' * j) + '}'
    return result


def generate_diff(source1, source2):
    source1 = converting(source1)
    source2 = converting(source2)
    return rendering(diff(source1, source2))
