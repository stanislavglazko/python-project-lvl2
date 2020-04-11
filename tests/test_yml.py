from gendiff import generate_diff
import json
import yaml
import pytest


def test_yml():
    place = './tests/fixtures/'
    answers = {
        'answer.txt': ('before.yml', 'after.yml', 'None'),
        'answer2.txt': ('before2.yml', 'after2.yml', 'None'),
        'answer3.txt': ('before3.yml', 'after3.yml', 'None'),
        'answer4.txt': ('before_complete.yml', 'after_complete.yml', 'None'),
        'answer_plain.txt': ('before.yml', 'after.yml', 'plain'),
        'plain_answer_complexe.txt': ('before_complete.yml', 'after_complete.yml', 'plain'),
        'answer_json.txt': ('before.json', 'after.json', 'json'),
    }
    for key, item in answers.items():
        with open(place + key) as file:
            answer = file.read()
        assert generate_diff(place+item[0], place+item[1], item[2]) == answer
