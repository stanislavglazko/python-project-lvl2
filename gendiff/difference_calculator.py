import json
import yaml
import os


def load(source):
    _, type = os.path.splitext(source)
    if type == '.json' or type == '.JSON':
        return json.load(open(source))
    return yaml.safe_load(open(source))


def diff(source1, source2):
    common = list(source1.keys() & source2.keys())
    only_before = list(source1.keys() - source2.keys())
    only_after = list(source2.keys() - source1.keys())
    result = {}
    for i in common:
        if source1[i] == source2[i]:
            result[i] = ('common', source1[i])
        elif source1[i] != source2[i]:
            if type(source1[i]) == dict and type(source2[i]) == dict:
                result[i] = diff(source1[i], source2[i])
            else:
                result[i] = ('changed', (source1[i], source2[i]))
    for i in only_before:
        result[i] = ('removed', source1[i])
    for i in only_after:
        result[i] = ('added', source2[i])
    return result
