import json
import yaml


def converting(source):
    name = source.split('.')
    name = name[-1]
    if name == 'yml':
        source = yaml.safe_load(open(source))
    elif name == 'json':
        source = json.load(open(source))
    return source


def generate_diff(source1, source2):
    source1 = converting(source1)
    source2 = converting(source2)
    common = sorted(list(source1.keys() & source2.keys()))
    only_before = sorted(list(source1.keys() - source2.keys()))
    only_after = sorted(list(source2.keys() - source1.keys()))
    result = '{' + '\n'
    for i in common:
        if source1[i] == source2[i]:
            result = result + '    ' + i + ': ' + str(source1[i]) + '\n'
    for i in common:
        if source1[i] != source2[i]:
            result = result + '  + ' + i + ': ' + str(source2[i]) + '\n'
            result = result + '  - ' + i + ': ' + str(source1[i]) + '\n'
    for i in only_before:
        result = result + '  - ' + i + ': ' + str(source1[i]) + '\n'
    for i in only_after:
        result = result + '  + ' + i + ': ' + str(source2[i]) + '\n'
    result = result + '}'
    return result
