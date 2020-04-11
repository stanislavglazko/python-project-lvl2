import json


def format(source):
    sorted_diff = {k: source[k] for k in sorted(source)}
    return json.dumps(sorted_diff, indent=2)
