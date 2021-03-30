#!/usr/bin/env python3

import os
import sys

import re
import unidecode

def get_file():
    f = []
    mypath = os.getcwd()
    for (dirpath, dirnames, filenames) in os.walk(mypath):
        f.extend(filenames)
        break

    return f

def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '_', text)

def arq(name):

    file_name, ext_name = (os.path.splitext(name))

    old_file = name

    slug ="{}{}".format(slugify(file_name), ext_name)

    new_file = slug

    if new_file not in get_file():
        print("{}{} => {}".format(file_name, ext_name, new_file))
        os.rename(old_file, new_file )


if len(sys.argv) == 1:
    print("""Error:
        This not have file
        Usage is:
          slug <filename1.ext> ... <filename2.ext>
        or
          slug -all """)

else:
    if "-all" in sys.argv:
        sys.argv.remove("-all")

        for name in get_file():
            arq(name)

    else:
        arq(sys.argv[-1])
