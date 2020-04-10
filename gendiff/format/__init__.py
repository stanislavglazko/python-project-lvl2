from gendiff.format.j_son import format as json
from gendiff.format.plain import format as plain
from gendiff.format.default import format as default


FORMATTERS = (JSON, PLAIN, DEFAULT) = (
    'json', 'plain', 'default'
)

__all__ = ('json', 'plain', 'default')
