# Changelog

## [0.1.5] - 2025-05-29

### Added

- GitHub Actions CI workflows for linting (ruff) on every push and running tests on pull requests to main.
- Automated release workflow: build, changelog extraction, and PyPI publishing on tag push.
- Logging-based cleanup in test fixtures for better error visibility.

### Changed

- Refactored API endpoint URLs in all major components to include versioning (e.g., `/v1/`).
- Improved error handling: sender now raises detailed exceptions with request/response info.
- Updated duplication strategy and activity test fixtures for robustness and cleanup.

### Fixed

- Linting issues and improved code style to pass ruff checks.
- Test discovery and configuration for pytest.
