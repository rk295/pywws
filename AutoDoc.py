#!/usr/bin/env python

import os
import pydoc
import sys

def AutoDoc():
    doc_dir = 'doc/auto'
    if not os.path.isdir(doc_dir):
        os.mkdir(doc_dir)
    wd = os.getcwd()
    for file in os.listdir('./'):
        base, ext = os.path.splitext(file)
        if ext != '.py':
            continue
        pydoc.writedoc(base)
        src_file = base + '.html'
        if not os.path.exists(src_file):
            continue
        # post-process pydoc output to clean up some of its eccentricities
        dest_file = os.path.join(doc_dir, src_file)
        src = open(src_file, 'r')
        dest = open(dest_file, 'w')
        for line in src:
            for a, b in (
                (os.path.join(wd, file), os.path.join('../..', file)),
                ('"."', '../index.html'),
                ):
                if a in line:
                    line = line.replace(a, b)
            dest.write(line)
        dest.close()
        src.close()
        os.unlink(src_file)
    return 0
if __name__ == "__main__":
    sys.exit(AutoDoc())