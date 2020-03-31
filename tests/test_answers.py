import json
import yaml
import pytest
from gendiff.generate_diff import generate_diff
from gendiff.generate_diff import converting


def test_answer():
    fin = open('./tests/fixtures/answer.txt', 'r')
    answer = fin.read()
    assert generate_diff('./tests/fixtures/before.json','./tests/fixtures/after.json') == answer


def test_answer2():
    fin = open('./tests/fixtures/answer2.txt', 'r')
    answer = fin.read()
    assert generate_diff('./tests/fixtures/before2.json', './tests/fixtures/after2.json') == answer


def test_answer3():
    fin = open('./tests/fixtures/answer3.txt', 'r')
    answer = fin.read()
    assert generate_diff('./tests/fixtures/before3.json', './tests/fixtures/after3.json') == answer


def test_answer4():
    fin = open('./tests/fixtures/answer_complete_test.txt', 'r')
    answer = fin.read()
    assert generate_diff('./tests/fixtures/before_complete.json', './tests/fixtures/after_complete.json') == answer


def test_answer_plain():
    fin = open('./tests/fixtures/answer_plain.txt', 'r')
    answer = fin.read()
    assert generate_diff('./tests/fixtures/before.json','./tests/fixtures/after.json', format='plain') == answer


def test_answer2_plain():
    fin = open('./tests/fixtures/answer2_plain.txt', 'r')
    answer = fin.read()
    assert generate_diff('./tests/fixtures/before2.json', './tests/fixtures/after2.json', format='plain') == answer


def test_answer3_plain():
    fin = open('./tests/fixtures/answer3_plain.txt', 'r')
    answer = fin.read()
    assert generate_diff('./tests/fixtures/before3.json', './tests/fixtures/after3.json', format='plain') == answer


def test_answer4_plain():
    fin = open('./tests/fixtures/plain_answer_complexe.txt', 'r')
    answer = fin.read()
    assert generate_diff('./tests/fixtures/before_complete.json', './tests/fixtures/after_complete.json', format='plain') == answer
