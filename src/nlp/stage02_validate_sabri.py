"""
stage02_validate_case.py
(EDIT YOUR COPY OF THIS FILE)

Source: raw JSON object
Sink: validated JSON object

Purpose

  Inspect JSON structure and validate that the data is usable.

Analytical Questions

- What is the top-level structure of the JSON data?
- What keys are present in each record?
- What data types are associated with each field?
- Does the data meet expectations for transformation?

Notes

Following our process, do NOT edit this _case file directly,
keep it as a working example.

In your custom project, copy this _case.py file and
append with _yourname.py instead.

Then edit your copied Python file to:
- inspect the JSON structure for your API,
- validate required keys and types,
- confirm the data is usable for your analysis.
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
from typing import Any


def run_validate(
    json_data: Any,
    LOG: logging.Logger,
) -> list[dict]:

    LOG.info("========================")
    LOG.info("STAGE 02: VALIDATE starting...")
    LOG.info("========================")

    # Handle DummyJSON structure
    if isinstance(json_data, dict):
        json_data = json_data.get("products", [])

    LOG.info("JSON STRUCTURE INSPECTION:")
    LOG.info(f"Top-level type: {type(json_data).__name__}")

    if isinstance(json_data, list) and len(json_data) > 0:
        first_record = json_data[0]

        LOG.info(f"Keys in first record: {list(first_record.keys())}")

        LOG.info("Field types:")
        for key, value in first_record.items():
            LOG.info(f"{key}: {type(value).__name__}")

    if not isinstance(json_data, list):
        raise ValueError("Expected JSON data to be a list of records.")

    if len(json_data) == 0:
        raise ValueError("Expected at least one record.")

    if not all(isinstance(record, dict) for record in json_data):
        raise ValueError("Expected each record to be a dictionary.")

    required_keys = {"title", "price", "category"}

    for record in json_data:
        if not required_keys.issubset(record.keys()):
            raise ValueError(f"Missing required keys in record: {record}")

    LOG.info("Validation passed.")
    LOG.info("Sink: validated JSON object")

    return json_data
