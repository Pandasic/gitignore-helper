import argparse
import sys
import os
import json

from collections import OrderedDict

ROOT = os.path.dirname(os.path.abspath(__file__))


class Conf:
    source_path = ""
    default = []


def loadConf():
    conf_path = os.path.join(ROOT, "conf.json")
    if os.path.exists(conf_path):
        with open(conf_path,'r') as fs:
            conf = json.load(fs)
            for k, v in conf.items():
                setattr(Conf, k, v)


def get_args():
    parser = argparse.ArgumentParser(description="get and combine .gitignore files")
    parser.add_argument(
        "-l",
        "--list",
        dest="list",
        action="store_true",
        help="show all gitignore files",
    )
    parser.add_argument("items", nargs="*", help="all .gitignore files in source")
    args = parser.parse_args()
    return args


def fix_path(s):
    if s.endswith(".gitignore"):
        return os.path.join(Conf.source_path, s)
    else:
        return os.path.join(Conf.source_path, s + ".gitignore")


def get_lists():
    for f in os.listdir(Conf.source_path):
        if f.endswith(".gitignore"):
            print(f.replace(".gitignore", ""))


def gen_gitignore(items):
    ignore_names = [fix_path(f) for f in items]

    if len(ignore_names) == 0:
        print("no ignore file name input, exit")
        sys.exit()

    if os.path.exists(".gitignore"):
        ignore_names = [".gitignore"] + ignore_names
    ignore_lines = OrderedDict()

    for ignore_name in ignore_names:
        if os.path.exists(ignore_name):
            with open(ignore_name, "r") as fs:
                for row in fs.readlines():
                    ignore_lines[row] = None
        else:
            print(f"{ignore_name} not exits, please check path or name is valid or not")
            sys.exit()

    check_sign = True
    if os.path.exists(".gitignore"):
        check_sign = (
            input(".gitignore file exist, do you wanna append to it?(y/N)").lower()
            == "y"
        )

    if check_sign:
        with open(".gitignore", "w") as fs:
            for row in ignore_lines:
                fs.write(row)
            else:
                print(".gitignore file has been created successfully")
    else:
        print(".gitignore file append is canceled")


def main():
    args = get_args()
    loadConf()
    if args.list:
        get_lists()
    else:
        gen_gitignore(Conf.default + args.items)


if __name__ == "__main__":
    main()
