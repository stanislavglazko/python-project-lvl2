import json
import yaml
from gendiff.format.plain import plain
from gendiff.format.rendering import rendering
from gendiff.format.make_json import make_json


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
            result[('    ' + i)] = source1[i]
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


def generate_diff(source1, source2, format=None):
    source1 = converting(source1)
    source2 = converting(source2)
    if format == 'plain':
        return plain(diff(source1, source2))[:-1]
    if format == 'json':
        return make_json(diff(source1, source2))
    return rendering(diff(source1, source2))
