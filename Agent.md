# Agent Instructions

## Project Overview

This library implements a convenient interface for the YCLIENTS web service API.
It provides a clean, type-safe interface for managing salon and beauty business operations including appointments, services, staff, and more.

- Repository: https://github.com/mkosinov/yclientsapi
- PyPI: https://pypi.org/project/poor_yclientsapi/

## Technical Stack

- **Language**: Python 3.12+
- **Package Manager**: Poetry
- **Linting**: Ruff
- **Testing**: pytest
- **HTTP Client**: httpx
- **Serialization**: pydantic, orjson

## Key Features

- Authentication management
- CRUD operations for YCLIENTS entities (services, staff, activities, records, etc.)
- Comprehensive error handling with detailed exceptions
- Type hints throughout the codebase
- Integration testing suite
- Logging support with optional custom logger injection

## Architecture Principles

- Clean separation of concerns
- Modular component design (each API domain in its own component)
- Consistent error handling patterns
- Type safety as a first-class concern

## Development Standards

- Follow PEP 8 and modern Python conventions
- Use type hints for all public APIs
- Implement tests for new functionality
- Maintain backward compatibility
- Document all public interfaces
- Run ruff for linting before committing

## Workflow for Code Changes

**IMPORTANT: Never commit directly to `main` or `master` branch. Always create a separate branch for your work.**

1. Create a new branch with a descriptive name reflecting the work being done.
   Example: `git checkout -b fix/pydantic-validation` or `git checkout -b feature/webhook-handler`
2. Make your changes in this branch. When making changes, update the library version in `pyproject.toml`.
3. Commit your changes to the branch.
4. Push the new branch to GitHub: `git push -u origin <branch-name>`
5. Create a Pull Request targeting `main` (or `master`).
6. After pushing, check the status of the latest GitHub Actions using `gh run list`.
7. If any workflows fail, review the errors and fix issues related to your changes.

## Publishing

To publish a new version of the library to PyPI, an automatic workflow detects the new version in `pyproject.toml` and triggers the release.

## Useful Links

- YCLIENTS Developers: https://yclients.com/appstore/developers
- YCLIENTS API Docs: https://developers.yclients.com/
