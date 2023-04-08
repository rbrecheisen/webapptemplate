import os
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='new name for this project', type=str)
    args = parser.parse_args()
    print(args)

    # - check <name> is not 'template'
    # - copy folder 'template' to <name>
    # - run renaming tool


if __name__ == '__main__':
    main()
