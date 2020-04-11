import json
import yaml
import os


def load(source):
    _, type = os.path.splitext(source)
    if type == '.json' or type == '.JSON':
        return json.load(open(source))
    return yaml.safe_load(open(source))


def keys(source1, source2):
    common = list(source1.keys() & source2.keys())
    only_before = list(source1.keys() - source2.keys())
    only_after = list(source2.keys() - source1.keys())
    return common, only_before, only_after


def common1(source1, source2):
    source = keys(source1, source2)[0]
    result = {}
    for i in source:
        if source1[i] == source2[i]:
            result[i] = ('common', source1[i])
    return result


def common2(source1, source2):
    result = common1(source1, source2)
    for i in keys(source1, source2)[0]:
        if source1[i] != source2[i]:
            if isinstance(source1[i], dict) and isinstance(source2[i], dict):
                result[i] = diff(source1[i], source2[i])
            else:
                result[i] = ('changed', (source1[i], source2[i]))
    return result


def before_after(source1, source2):
    before, after = keys(source1, source2)[1], keys(source1, source2)[2]
    result = common2(source1, source2)
    for i in before:
        result[i] = ('removed', source1[i])
    for i in after:
        result[i] = ('added', source2[i])
    return result


def diff(source1, source2):
    return before_after(source1, source2)
