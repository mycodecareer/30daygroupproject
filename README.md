# 30daygroupproject

[![CI and Release](https://github.com/mycodecareer/30daygroupproject/actions/workflows/ci_release.yml/badge.svg)](https://github.com/mycodecareer/30daygroupproject/actions/workflows/ci_release.yml)

This is the repository for the SDR 30 day builder's challenge group project. It is a recipe app with a react frontend and a python flask backend.

## Contributing

See our [Contributors Guide](./CONTRIBUTING)

### Minimal Dev Setup

This project uses the following languages:

- NodeJS
- Python3

For these languages, this project used the following package managers:

- npm and yarn
- pip

For code style, this project relies on the following linters:

- Prettier
- Black
- Flake8
- Yamllint
- Markdownlint

### Install git hooks

This project utilizes git hooks to proactively lint the codebase. Before contributing, install the git hooks with th following command:

```bash
make install-hooks
```

This will run the linters before executing a `git commit`.

## React Frontend

See [Frontend README](./frontend/README.md)

## Flask Backend

See [Backend README](./backend/README.md)
