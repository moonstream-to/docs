import os
import sys

SCRIPT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.realpath(os.path.dirname(SCRIPT_DIR))

# Submodule READMEs
ENTITY_README_PATH = os.path.join(BASE_DIR, "entity", "README.md")
ENTITY_CLIENT_LIBRARY_PATH = os.path.join(BASE_DIR, "entity", "clients", "python", "README.md")

# Moonstream docs files
DOCS_ENTITY_PATH = os.path.join(BASE_DIR, "docs", "engine", "entity.md")

if not os.path.isfile(ENTITY_README_PATH) or not os.path.isfile(ENTITY_CLIENT_LIBRARY_PATH):
    if os.path.isfile(DOCS_ENTITY_PATH):
        print("Could not find README for Entity in git submodule. Deleting Entity documentation from this repository...")
        os.remove(DOCS_ENTITY_PATH)

    print("No further actions necessary.")
    sys.exit(0)

existing_content = ""
if os.path.isfile(DOCS_ENTITY_PATH):
    with open(DOCS_ENTITY_PATH, "r") as ifp:
        existing_content = ifp.read()

content = """---
tags:
  - alpha
  - data
  - entity
  - overview
  - schemes
  - cli
  - library
---


"""

with open(ENTITY_README_PATH, "r") as ifp:
    readme_content = ifp.read()
    print(readme_content)
    content += readme_content
with open(ENTITY_CLIENT_LIBRARY_PATH, "r") as ifp:
    client_lib_content = ifp.read()
    content += client_lib_content

# Enforce idempotence of generated file to play nice with "mkdocs serve" live reload.
if content == existing_content:
    print(f"No changes to write to {DOCS_ENTITY_PATH}.")
    sys.exit(0)
with open(DOCS_ENTITY_PATH, "w") as ofp:
    ofp.write(content)

print(
    f"Entity documentation generated from {ENTITY_README_PATH}, {ENTITY_CLIENT_LIBRARY_PATH} "
    f"and written to {DOCS_ENTITY_PATH}."
)
