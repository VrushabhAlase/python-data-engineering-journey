import pandas as pd
import os
import logging
import sys

# -----------------------------------------
# Setup Logging
# -----------------------------------------

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Pipeline started")

try:
    # -----------------------------------------
    # STEP 1: GET INPUT FILE
    # -----------------------------------------

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "input/sales.csv"

    logging.info(f"Using input file: {input_file}")

    # -----------------------------------------
    # STEP 2: READ DATA
    # -----------------------------------------

    df = pd.read_csv(input_file)

    # -----------------------------------------
    # STEP 3: CLEAN DATA
    # -----------------------------------------

    df["amount"] = df["amount"].fillna(0).astype(int)

    # -----------------------------------------
    # STEP 4: TRANSFORM
    # -----------------------------------------

    df["tax"] = df["amount"] * 0.10
    df["total"] = df["amount"] + df["tax"]

    # -----------------------------------------
    # STEP 5: SAVE OUTPUT
    # -----------------------------------------

    os.makedirs("output", exist_ok=True)

    output_file = "output/processed_sales.csv"
    df.to_csv(output_file, index=False)

    logging.info("Pipeline completed successfully")
    print("Pipeline completed successfully ✅")

except Exception as e:
    logging.error(f"Error occurred: {e}")
    print("Error occurred ❌:", e)