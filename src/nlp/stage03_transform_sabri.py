"""
stage03_transform_case.py
(EDIT YOUR COPY OF THIS FILE)

Source: validated JSON object
Sink: Polars DataFrame

Purpose

  Transform validated JSON data into a structured format.

Analytical Questions

- Which fields are needed from the JSON data?
- How can records be normalized into tabular form?
- What derived fields would support analysis?

Notes

Following our process, do NOT edit this _case file directly,
keep it as a working example.

In your custom project, copy this _case.py file and
append with _yourname.py instead.

Then edit your copied Python file to:
- extract the fields needed for your analysis,
- normalize records into a consistent structure,
- create any derived fields required.
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging

import polars as pl


def run_transform(
    json_data: list[dict],
    LOG: logging.Logger,
) -> pl.DataFrame:

    LOG.info("========================")
    LOG.info("STAGE 03: TRANSFORM starting...")
    LOG.info("========================")

    records = []

    for record in json_data:
        item = {
            "id": record.get("id"),
            "title": record.get("title"),
            "price": record.get("price"),
            "category": record.get("category"),
            "brand": record.get("brand"),
            "rating": record.get("rating"),
            "stock": record.get("stock"),
            "discount_percentage": record.get("discountPercentage"),
        }
        records.append(item)

    df = pl.DataFrame(records)

    LOG.info("Transformation complete.")
    LOG.info(f"DataFrame shape: {df.shape}")
    LOG.info("DataFrame preview:")
    LOG.info(f"\n{df.head(5)}")
    LOG.info("Sink: Polars DataFrame created")

    return df
