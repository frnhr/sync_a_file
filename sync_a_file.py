#!/usr/bin/env python

from __future__ import print_function


FROM_DIR = 'rebelmouse'
TO_DIR = 'remote'
DELETE_RETRIES = 5

IGNORE_PATTERNS = (
    r'^.idea',
    r'^.git/',
    r'.pyc$',
    r'___jb_bak___$',
    r'___jb_old___$',
)


# ------------------------------------------------------------- #
import sys
import os
import shutil
import re
import datetime

def _base_dir():
    # return os.getcwd()  # working directory
    return os.path.dirname(os.path.abspath(__file__))  # directory of the script

def _from_dir(additional_path=''):
    return os.path.join(_base_dir(), FROM_DIR, additional_path)

def _to_dir(additional_path=''):
    return os.path.join(_base_dir(), TO_DIR, additional_path)

def _match_ignore(path):
    for pattern in IGNORE_PATTERNS:
        if re.search(pattern, path):
            return True
    return False

def _print(content, end="\n"):
    sys.stdout.write("{}".format(content))
    sys.stdout.write("{}".format(end))
    sys.stdout.flush()

def _delete(path):
    for i in range(1, DELETE_RETRIES + 1):
        try:
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)
        except OSError as e:
            _print("OS error: {}".format(e))
            _print("retrying {}/{}".format(i, DELETE_RETRIES))
        else:
            if i > 1:
                print("  deleted.")
            break  # for
    if i == DELETE_RETRIES:
        _print("giving up...")

def main(args):
    filepath = args[0]
    relative_path = re.sub(r'^{}'.format(_from_dir()), r'', filepath)
    if _match_ignore(relative_path):
        return
    from_path = _from_dir(relative_path).strip()
    to_path = _to_dir(relative_path).strip()
    _print(datetime.datetime.now(), end=" ")
    _print(from_path, end=" ")
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
    _print(".")

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass
