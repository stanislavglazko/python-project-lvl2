from gendiff.difference_calculator import load
from gendiff.difference_calculator import diff
import gendiff.format


def generate_diff(source1, source2, name=None):
    source1 = load(source1)
    source2 = load(source2)
    if name == format.PLAIN:
        return format.plain(diff(source1, source2))[:-1]
    if name == format.JSON:
        return format.json(diff(source1, source2))
    return format.default(diff(source1, source2))
