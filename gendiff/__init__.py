from gendiff.diff import load
from gendiff.diff import generate
from gendiff import format


def generate_diff(source1, source2, name=None):
    source1 = load(source1)
    source2 = load(source2)
    if source1 is not None and source2 is not None:
        if name == format.PLAIN:
            return format.plain(generate(source1, source2))[:-1]
        elif name == format.JSON:
            return format.json(generate(source1, source2))
        return format.default(generate(source1, source2))
    print('Compare yml or json file, please')
    answer = 'Correct name of file: name.json or name.yml'
    return answer
