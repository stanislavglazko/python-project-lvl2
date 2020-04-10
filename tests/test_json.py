from gendiff import generate_diff
import json
import yaml
import pytest


def test_json():
    place = './tests/fixtures/'
    answers = {
        'answer.txt': ('before.json', 'after.json', 'None'),
        'answer2.txt': ('before2.json', 'after2.json', 'None'),
        'answer3.txt': ('before3.json', 'after3.json', 'None'),
        'answer4.txt': ('before_complete.json', 'after_complete.json', 'None'),
        'answer_plain.txt': ('before.json', 'after.json', 'plain'),
        'plain_answer_complexe.txt': ('before_complete.json', 'after_complete.json', 'plain'),
    }
    for key, item in answers.items():
        with open(place + key) as file:
            answer = file.read()
        assert generate_diff(place+item[0], place+item[1], item[2]) == answer
