# =========================================
# Sales Data Pipeline (Production Version)
# =========================================

import pandas as pd
import os
import logging

# -----------------------------------------
# Setup Logging
# -----------------------------------------

# Create logs folder
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Pipeline started")


try:
    # -----------------------------------------
    # STEP 1: READ DATA
    # -----------------------------------------
    logging.info("Reading input file")

    df = pd.read_csv("input/sales.csv")

    # -----------------------------------------
    # STEP 2: CLEAN DATA
    # -----------------------------------------
    logging.info("Cleaning data")

    df["amount"] = df["amount"].fillna(0).astype(int)

    # -----------------------------------------
    # STEP 3: TRANSFORM DATA
    # -----------------------------------------
    logging.info("Transforming data")

    df["tax"] = df["amount"] * 0.10
    df["total"] = df["amount"] + df["tax"]

    # -----------------------------------------
    # STEP 4: SAVE OUTPUT
    # -----------------------------------------
    logging.info("Saving output")

    os.makedirs("output", exist_ok=True)

    df.to_csv("output/processed_sales.csv", index=False)

    logging.info("Pipeline completed successfully")

    print("Pipeline completed successfully ✅")


except Exception as e:
    logging.error(f"Error occurred: {e}")
    print("Error occurred ❌:", e)