# moonstream-docs
Moonstream documentation

## Setup

Update all git submodules:

```
git submodule  update --init --recursive
```

Create a Python environment if necessary, then:

```
pip install -U -r requirements.txt
```

## Development

To run documentation server:

```
mkdocs serve
```

This will host the docs site at http://localhost:8000

Override this using the `--dev-addr` argument as follows: `--dev-addr 0.0.0.0:1337`.

## Production build

This will produce the static doc site in the `site/` directory:

```
mkdocs build
```
