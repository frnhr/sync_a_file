#!/usr/bin/env python

from __future__ import print_function


FROM_DIR = 'local'
TO_DIR = 'remote'
DELETE_RETRIES = 5


# ------------------------------------------------------------- #
import sys
import os
import shutil
import re

def _base_dir():
    # return os.getcwd()  # working directory
    return os.path.dirname(os.path.abspath(__file__))  # directory of the script

def _from_dir(additional_path=''):
    return os.path.join(_base_dir(), FROM_DIR, additional_path)

def _to_dir(additional_path=''):
    return os.path.join(_base_dir(), TO_DIR, additional_path)

def _delete(path):
    for i in range(1, DELETE_RETRIES + 1):
        try:
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)
        except OSError as e:
            print("OS error: {}".format(e))
            print("retrying {}/{}".format(i, DELETE_RETRIES))
        else:
            if i > 1:
                print("  deleted.")
            break  # for
    if i == DELETE_RETRIES:
        print("giving up...")

def main(args):
    filepath = args[0]
    relative_path = re.sub(r'^{}'.format(_from_dir()), r'', filepath)
    from_path = _from_dir(relative_path).strip()
    to_path = _to_dir(relative_path).strip()
    print(from_path, end=" ")
    if os.path.isfile(from_path):
        shutil.copy2(from_path, to_path)
        # @TOOD if we replace a file with a directory of exactly the same name, then kaboom!
    elif os.path.isdir(from_path):
        if os.path.exists(to_path):
            _delete(to_path)
        shutil.copytree(from_path, to_path)
    else:
        if os.path.exists(to_path):
            _delete(to_path)
    print(".")

if __name__ == '__main__':
    main(sys.argv[1:])
