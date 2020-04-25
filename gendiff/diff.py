import json
import yaml
import os


ADDED, REMOVED, CHANGED = 'added', 'removed', 'changed'
COMMON, NESTED = 'common', 'nested'


def load(source):
    _, type = os.path.splitext(source)
    if type == '.json' or type == '.JSON':
        return json.load(open(source))
    elif type == '.yml' or type == '.yaml' or type == '.YML':
        return yaml.safe_load(open(source))
    return None


def generate(source1, source2):
    common = source1.keys() & source2.keys()
    only_before = source1.keys() - source2.keys()
    only_after = source2.keys() - source1.keys()
    result = {}
    for key in common:
        source1_item = source1[key]
        source2_item = source2[key]
        if source1_item == source2_item:
            result[key] = (COMMON, source1_item)
        else:
            if type(source1_item) == dict and type(source2_item) == dict:
                result[key] = (NESTED, generate(source1_item, source2_item))
            else:
                result[key] = (CHANGED, (source1_item, source2_item))
    for key in only_before:
        source1_item = source1[key]
        result[key] = (REMOVED, source1_item)
    for key in only_after:
        source2_item = source2[key]
        result[key] = (ADDED, source2_item)
    return result
