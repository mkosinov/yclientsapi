# Changelog

## [0.1.22] - 2026-01-14

### Fixed

- Fixed Pydantic validation error in `StaffData.schedule_till`: field can now be `None` (moved to end of class to satisfy dataclass field ordering requirements)
- Fixed Pydantic validation error in `ActivityResponse.data.staff.user_id`: field can now be `None` (moved to end of class to satisfy dataclass field ordering requirements)

## [0.1.6] - 2025-05-30

### Added

- Added full set of CRUD operations in the service_category component: `list`, `get`, `create`, `update`, `delete`. Added schemas to pass correct payload and validate responses. Implemented integration tests for these methods.

### Changed

- Fixes in CI workflow

## [0.1.5] - 2025-05-29

### Added

- GitHub Actions CI workflows for linting (ruff) on every push and running tests on pull requests to main.
- Automated release workflow: build, changelog extraction, and PyPI publishing on tag push.
- Logging-based cleanup in test fixtures for better error visibility.
- Split CI into separate workflows for pull requests and commits to main branch.
- Coverage reporting instructions and badge in README.
- Updated test documentation to reflect current test and coverage setup.
- Extended service_category component: added create, update, and delete methods.
- Added Pydantic dataclasses for service category create/update requests.
- Added fixtures and integration tests for service_category CRUD operations.

### Changed

- Refactored API endpoint URLs in all major components to include versioning (e.g., `/v1/`).
- Improved error handling: sender now raises detailed exceptions with request/response info.
- Updated duplication strategy and activity test fixtures for robustness and cleanup.
- Removed the safe test system; tests now clean up after themselves where applicable.

### Fixed

- Linting issues and improved code style to pass ruff checks.
- Test discovery and configuration for pytest.
