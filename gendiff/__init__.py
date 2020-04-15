from gendiff.diff import load
from gendiff.diff import generate
from gendiff import format


def generate_diff(source1, source2, name=None):
    source1 = load(source1)
    source2 = load(source2)
    if name == format.PLAIN:
        return format.plain(generate(source1, source2))[:-1]
    if name == format.JSON:
        return format.json(generate(source1, source2))
    return format.default(generate(source1, source2))
