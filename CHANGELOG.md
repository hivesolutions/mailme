# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

* New `dockerx.yml` GitHub Actions workflow that builds multi-arch (`linux/amd64`, `linux/arm64/v8`) images, pushes to `hivesolutions/mailme` on Docker Hub with provenance and SBOM, and triggers the `mailme` deployment in `infra-bemisc` on tag pushes
* `AGENTS.md` with contributor and AI-agent guidelines (formatting, testing, Conventional Commits, release process), and a `CLAUDE.md` pointer that redirects Claude Code to `AGENTS.md`

### Changed

* Modernized `Dockerfile`: switched base image to `python:alpine`, converted all `ENV` directives to the `KEY=VALUE` form, collapsed the install steps into a single `RUN` with `--no-cache-dir`, and dropped privileges to a non-root `mailme` user
* Bumped `actions/checkout` from `v4` to `v6` across all workflows

### Fixed

*

## [0.1.5] - 2025-03-04

### Added

* Added support for `style_css` allowing for custom CSS styles

## [0.1.4] - 2024-04-21

### Changed

* Bumped packages

## [0.1.3] - 2024-01-17

### Added

* More parameters to the `Message` structure

## [0.1.2] - 2024-01-17

### Fixed

* Extra `lib` based deployment

## [0.1.1] - 2024-01-17

### Changed

* Ran restructure to allow `black` code format

## [0.1.0] - 2023-11-26

### Added

* Support for the `attachments` field in the `Message` structure
