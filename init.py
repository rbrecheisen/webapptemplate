import os
import fnmatch
import shutil
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='new name for this project', type=str)
    parser.add_argument('output_dir', help='output directory to store new project files')
    args = parser.parse_args()

    if args.name == 'template':
        raise RuntimeError('new name cannot be "template"')    
    shutil.copytree('template', args.output_dir)

    os.rename(os.path.join(args.output_dir, 'webapp'), os.path.join(args.output_dir, args.name))
    os.rename(os.path.join(args.output_dir, f'{args.name}/webapp'), os.path.join(args.output_dir, f'{args.name}/{args.name}'))

    for root, dirs, files in os.walk(os.path.join(args.output_dir, args.name)):
        for f_name in fnmatch.filter(files, '*.py'):
            f_path = os.path.join(root, f_name)
            with open(f_path, 'r') as f:
                s = f.read()
            s = s.replace('webapp', args.name)



if __name__ == '__main__':
    main()
