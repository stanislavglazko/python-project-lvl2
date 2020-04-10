from gendiff.cli import parse_args
from gendiff import generate_diff


def main():
    print(generate_diff(parse_args().first_file, parse_args().second_file,
                        parse_args().format))


if __name__ == '__main__':
    main()
