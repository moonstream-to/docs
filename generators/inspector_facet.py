import os
import sys

SCRIPT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.realpath(os.path.dirname(SCRIPT_DIR))
INSPECTOR_FACET_README_PATH = os.path.join(BASE_DIR, "inspector-facet", "README.md")
INSPECTOR_FACET_DOCS_PATH = os.path.join(BASE_DIR, "docs", "tooling", "inspector-facet.md")

if not os.path.isfile(INSPECTOR_FACET_README_PATH):
    if os.path.isfile(INSPECTOR_FACET_DOCS_PATH):
        print("Could not find README for Inspector Facet in git submodule. Deleting Inspector Facet documentation from this repository...")
        os.remove(INSPECTOR_FACET_DOCS_PATH)

    print("No further actions necessary.")
    sys.exit(0)

with open(INSPECTOR_FACET_README_PATH, "r") as ifp, open(INSPECTOR_FACET_DOCS_PATH, "w") as ofp:
    docs_content = ifp.read()

    tags_content = """---
tags:
  - tooling
  - python
  - library
  - cli
  - EIP2535
---


"""

    ofp.write(tags_content)
    ofp.write(docs_content)

print(f"Inspector Facet documentation generated from {INSPECTOR_FACET_README_PATH} and written to {INSPECTOR_FACET_DOCS_PATH}.")
