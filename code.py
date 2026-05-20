import pandas as pd
from collections import Counter
import os

# ============================================================
# ENTER YOUR LOCAL FILE PATH HERE
# Example:
# file_path = r"C:\Users\YourName\Documents\assets.xlsx"
# ============================================================

file_path = r"PUT_YOUR_FILE_PATH_HERE"

# ============================================================
# CHECK IF FILE EXISTS
# ============================================================

if not os.path.exists(file_path):
    print("File not found.")
    exit()

# ============================================================
# LOAD FILE
# Supports:
#   - Excel (.xlsx)
#   - CSV (.csv)
# ============================================================

try:
    if file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)

    elif file_path.endswith(".csv"):
        df = pd.read_csv(file_path)

    else:
        print("Unsupported file format.")
        exit()

except Exception as e:
    print("Error reading file:", e)
    exit()

# ============================================================
# SHOW COLUMN NAMES
# ============================================================

print("\nAvailable Columns:")
print(df.columns.tolist())

# ============================================================
# CHANGE THESE COLUMN NAMES TO MATCH YOUR FILE
# ============================================================

MODEL_COLUMN = "Model"
VERSION_COLUMN = "Version"

# ============================================================
# CHECK REQUIRED COLUMNS
# ============================================================

required_columns = [MODEL_COLUMN, VERSION_COLUMN]

for col in required_columns:
    if col not in df.columns:
        print(f"\nMissing column: {col}")
        exit()

# ============================================================
# COUNT ASSET MODELS + VERSIONS
# ============================================================

grouped = (
    df.groupby([MODEL_COLUMN, VERSION_COLUMN])
    .size()
    .reset_index(name="Quantity")
)

# ============================================================
# DISPLAY RESULTS
# ============================================================

print("\nAsset Model Summary:\n")
print(grouped)

# ============================================================
# OPTIONAL: SAVE RESULTS
# ============================================================

output_file = "asset_model_summary.xlsx"

grouped.to_excel(output_file, index=False)

print(f"\nSummary saved to: {output_file}")
