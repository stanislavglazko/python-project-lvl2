from gendiff.generate_diff import generate_diff
from gendiff.parsers import parser


def main():
    print(generate_diff(parser().first_file, parser().second_file))


if __name__ == '__main__':
    main()
