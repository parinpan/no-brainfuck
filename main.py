import sys
from interpreter import brainfuck_reader


def main():
    print(brainfuck_reader(sys.argv[1]))


if __name__ == '__main__':
    main()
