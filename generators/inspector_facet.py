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

existing_content = ""
if os.path.isfile(INSPECTOR_FACET_DOCS_PATH):
    with open(INSPECTOR_FACET_DOCS_PATH, "r") as ifp:
        existing_content = ifp.read()

with open(INSPECTOR_FACET_README_PATH, "r") as ifp:
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

    # Enforce idempotence of generated file to play nice with "mkdocs serve" live reload.
    content = f"{tags_content}{docs_content}"
    if content == existing_content:
        print(f"No changes to write to {INSPECTOR_FACET_DOCS_PATH}.")
        sys.exit(0)

    with open(INSPECTOR_FACET_DOCS_PATH, "w") as ofp:
        ofp.write(content)

print(f"Inspector Facet documentation generated from {INSPECTOR_FACET_README_PATH} and written to {INSPECTOR_FACET_DOCS_PATH}.")
