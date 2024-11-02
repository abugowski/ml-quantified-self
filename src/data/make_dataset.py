import pandas as pd
from glob import glob

# --------------------------------------------------------------
# Read single CSV file
# --------------------------------------------------------------

single_file_acc = pd.read_csv(
    "../../data/raw/MetaMotion/A-bench-heavy_MetaWear_2019-01-14T14.22.49.165_C42732BE255C_Accelerometer_12.500Hz_1.4.4.csv"
)

# the same for gyroscope
single_file_gyro = pd.read_csv(
    "../../data/raw/MetaMotion/A-bench-heavy_MetaWear_2019-01-14T14.22.49.165_C42732BE255C_Gyroscope_25.000Hz_1.4.4.csv"
)
# --------------------------------------------------------------
# List all data in data/raw/MetaMotion
# --------------------------------------------------------------
# list all data files in data/raw/MetaMotion
files = glob("../../data/raw/MetaMotion/*.csv")
# len(files)

# --------------------------------------------------------------
# Extract features from filename
# --------------------------------------------------------------
f = files[1]
participant = f.split("-")[0].split("/")[-1]  # participant
label = f.split("-")[1]  # label
category = f.split("-")[2].split("_")[0].rstrip("123")  # category


# read file and add above features to the dataframe
# Add participant, label and category to the dataframe

df = pd.read_csv(f)
df["participant"] = participant
df["label"] = label
df["category"] = category


# --------------------------------------------------------------
# Read all files
# --------------------------------------------------------------
# extract features from all files names
acc_df = pd.DataFrame()
gyro_df = pd.DataFrame()

acc_set = 1
gyro_set = 1

for f in files:
    participant = f.split("-")[0].split("/")[-1]  # participant
    label = f.split("-")[1]  # label
    category = f.split("-")[2].split("_")[0].rstrip("123")  # category

    # # read file and add above features to the dataframe
    df = pd.read_csv(f)
    df["participant"] = participant
    df["label"] = label
    df["category"] = category

    if "Accelerometer" in f:
        df["set"] = acc_set
        acc_set += 1
        acc_df = pd.concat([acc_df, df])

    if "Gyroscope" in f:
        df["set"] = gyro_set
        gyro_set += 1
        gyro_df = pd.concat([gyro_df, df])

# --------------------------------------------------------------
# Working with datetimes
# --------------------------------------------------------------


# --------------------------------------------------------------
# Turn into function
# --------------------------------------------------------------


# --------------------------------------------------------------
# Merging datasets
# --------------------------------------------------------------


# --------------------------------------------------------------
# Resample data (frequency conversion)
# --------------------------------------------------------------

# Accelerometer:    12.500HZ
# Gyroscope:        25.000Hz


# --------------------------------------------------------------
# Export dataset
# --------------------------------------------------------------
