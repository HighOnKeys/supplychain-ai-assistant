import pandas as pd

# 1. LOAD DATA


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# 2. BASIC CLEANING


def basic_cleaning(df):

   # Convert Date column
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.ffill()

    return df

# 3. STANDARDIZE COLUMN NAMES


def standardize_columns(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df

# 4. CREATE TIME FEATURES


def create_time_features(df):
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["day_of_week"] = df["date"].dt.dayofweek
    return df

# 5. FEATURE ENGINEERING


def create_features(df):

    # Revenue calculation
    df["revenue"] = df["units_sold"] * df["price"]
    return df

# 6. SORT DATA


def sort_data(df):
    df = df.sort_values(by="date")
    return df

# 7. SAVE CLEANED DATA


def save_data(df, path="data/processed/cleaned_data.csv"):
    df.to_csv(path, index=False)

# 8. FULL PIPELINE FUNCTION


def process_data(file_path):
    df = load_data(file_path)
    df = basic_cleaning(df)
    df = standardize_columns(df)
    df = create_time_features(df)
    df = create_features(df)
    df = sort_data(df)
    save_data(df)

    return df
