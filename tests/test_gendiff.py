from gendiff import generate_diff
import json
import yaml
import pytest
import os
from gendiff.format import DEFAULT, PLAIN, JSON


place = './tests/fixtures/'
check = {
    'answer.txt': ('before.json', 'after.json', DEFAULT,
                   'before.json', 'after.yml', DEFAULT,
                   'before.yml', 'after.yml', DEFAULT),
    'answer2.txt': ('before2.json', 'after2.json', DEFAULT,
                    'before2.yml', 'after2.yml', DEFAULT),
    'answer3.txt': ('before3.json', 'after3.json', DEFAULT,
                    'before3.yml', 'after3.yml', DEFAULT),
    'answer4.txt': ('before_complete.json', 'after_complete.json', DEFAULT,
                    'before_complete.yml', 'after_complete.json', DEFAULT,
                    'before_complete.yml', 'after_complete.yml', DEFAULT),
    'answer_plain.txt': ('before.json', 'after.json', PLAIN,
                         'before.json', 'after.yml', PLAIN,
                         'before.yml', 'after.yml', PLAIN),
    'plain_answer_complexe.txt': ('before_complete.json', 'after_complete.json', PLAIN,
                                  'before_complete.yml', 'after_complete.yml', PLAIN),
}


def test_default_plain():
    for key, item in check.items():
        file_json_before = item[0]
        file_json_after = item[1]
        format_json = item[2]
        file_yml_before = item[3]
        file_yml_after = item[4]
        format_yml = item[5]
        with open(os.path.join(place, key)) as file:
            result = file.read()
        assert generate_diff(os.path.join(place, file_json_before),
                             os.path.join(place, file_json_after), format_json) == result
        assert generate_diff(os.path.join(place, file_yml_before),
                             os.path.join(place, file_yml_after), format_yml) == result


def test_json():
    check = json.load(open(os.path.join(place,'test_answer_json.json')))
    check_json = generate_diff(os.path.join(place,'before.json'), os.path.join(place, 'after.json'), JSON)
    with open("new.json", "w") as file:
        file.write(check_json)
    check_json = json.load(open('new.json'))
    check_yml = generate_diff(os.path.join(place,'before.yml'), os.path.join(place, 'after.yml'), JSON)
    with open("new2.json", "w") as file:
        file.write(check_yml)
    check_yml = json.load(open('new2.json'))
    assert check == check_json
    assert check == check_yml
