import json
from gendiff.generate_diff import generate_diff


def test_answer():
    fin = open('./tests/fixtures/answer.txt', 'r')
    answer = fin.read()
    assert generate_diff('before.json', 'after.json') == answer


def test_answer2():
    fin = open('./tests/fixtures/answer2.txt', 'r')
    answer = fin.read()
    assert generate_diff('before2.json', 'after2.json') == answer


def test_answer3():
    fin = open('./tests/fixtures/answer3.txt', 'r')
    answer = fin.read()
    assert generate_diff('before3.json', 'after3.json') == answer
