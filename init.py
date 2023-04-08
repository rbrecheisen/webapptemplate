import shutil
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='new name for this project', type=str)
    args = parser.parse_args()
    print(args)

    if args.name == 'template':
        raise RuntimeError('new name cannot be "template"')
    shutil.copytree('template', args.name)

    # rename files and content where necessary


if __name__ == '__main__':
    main()
