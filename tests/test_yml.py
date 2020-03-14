import json
import yaml
import pytest
from gendiff.generate_diff import generate_diff
from gendiff.generate_diff import converting


def test_answer_yml():
    fin = open('./tests/fixtures/answer.txt', 'r')
    answer = fin.read()
    assert generate_diff('./tests/fixtures/before.yml','./tests/fixtures/after.yml') == answer


def test_answer2_yml():
    fin = open('./tests/fixtures/answer2.txt', 'r')
    answer = fin.read()
    assert generate_diff('./tests/fixtures/before2.yml', './tests/fixtures/after2.yml') == answer


def test_answer3_yml():
    fin = open('./tests/fixtures/answer3.txt', 'r')
    answer = fin.read()
    assert generate_diff('./tests/fixtures/before3.yml', './tests/fixtures/after3.yml') == answer
