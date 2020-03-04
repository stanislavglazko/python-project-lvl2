import json


def generate_diff(source1, source2):
    before = json.load(open(source1))
    after = json.load(open(source2))
    before_keys = before.keys()
    after_keys = after.keys()
    common = before_keys & after_keys
    only_before = before_keys - after_keys
    only_after = after_keys - before_keys
    result = ['{', ]
    for i in common:
        if before[i] == after[i]:
            result.append('   ' + i + ': ' + str(before[i]))
        else:
            result.append('+  ' + i + ': ' + str(after[i]))
            result.append('-  ' + i + ': ' + str(before[i]))
    for i in only_before:
        result.append('-  ' + i + ': ' + str(before[i]))
    for i in only_after:
        result.append('+  ' + i + ' ' + str(after[i]))
    result.append('}')
    answer = ''
    for i in result:
        answer = answer + i + '\n'
    return answer
