import json


def generate_diff(source1, source2):
    source1 = json.load(open(source1))
    source2 = json.load(open(source2))
    common = source1.keys() & source2.keys()
    only_before = source1.keys() - source2.keys()
    only_after = source2.keys() - source1.keys()
    result = '{' + '\n'
    for i in common:
        if source1[i] == source2[i]:
            result = result + '   ' + i + ': ' + str(source1[i]) + '\n'
        else:
            result = result + ' + ' + i + ': ' + str(source2[i]) + '\n'
            result = result + ' - ' + i + ': ' + str(source1[i]) + '\n'
    for i in only_before:
        result = result + ' - ' + i + ': ' + str(source1[i]) + '\n'
    for i in only_after:
        result = result + ' + ' + i + ': ' + str(source2[i]) + '\n'
    result = result + '}'
    return result
