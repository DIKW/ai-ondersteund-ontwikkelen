#!/usr/bin/env bash
set -euo pipefail

PYTHONPATH=src python -m change_request_tracker.cli demo
