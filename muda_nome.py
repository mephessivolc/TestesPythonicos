#!/usr/bin/env python3

import os
import sys

import re
import unidecode

def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '_', text)

if len(sys.argv) == 1:
    raise ValueError("This not have file")

file_name = os.path.splitext(sys.argv[-1])

old_file = sys.argv[1]

slug ="{}{}".format(slugify(file_name[0]), file_name[1])

new_file = slug

os.rename(old_file, new_file )
