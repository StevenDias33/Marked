#!/usr/bin/env python

import sys
from os.path import join, dirname, exists

# Use the local markdown2.py if we are in the source tree.
source_tree_markdown2 = join(dirname(__file__), "..", "lib", "markdown2.py")
if exists(source_tree_markdown2):
    sys.path.insert(0, dirname(source_tree_markdown2))
    try:
        from markdown2 import main
    finally:
        del sys.path[0]
else:
    from markdown2 import main

if __name__ == "__main__":
    sys.exit(main(sys.argv))
