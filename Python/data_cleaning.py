import pandas as pd
from data_loading import load_data


def clean_data(df):
    """
    Clean the combined job-posting dataset
    and prepare the labelled dataset for analysis.
    """

    clean_df = df.copy()

    # Remove exact duplicate rows
    clean_df = clean_df.drop_duplicates()

    # Identify text columns
    text_columns = clean_df.select_dtypes(include="object").columns

    # Remove extra spaces
    for col in text_columns:
        clean_df[col] = clean_df[col].str.strip()

        # Convert blank strings to NaN
        clean_df[col] = clean_df[col].replace("", pd.NA)

    # Convert fraudulent column to numeric
    clean_df["fraudulent"] = pd.to_numeric(
        clean_df["fraudulent"],
        errors="coerce"
    )

    # Fill missing categorical/text values
    fill_values = {
        "department": "unknown",
        "salary_range": "not_mentioned",
        "company_profile": "Not_Applicable",
        "description": "Not_Applicable",
        "requirements": "Not_Applicable",
        "benefits": "Not_Applicable",
        "employment_type": "Unspecified",
        "required_experience": "Unspecified",
        "required_education": "Unspecified",
        "industry": "unknown",
        "function": "Unspecified"
    }

    for col, value in fill_values.items():
        if col in clean_df.columns:
            clean_df[col] = clean_df[col].fillna(value)

    # Create labelled dataset
    labelled_df = clean_df.dropna(
        subset=["fraudulent"]
    ).copy()

    labelled_df["fraudulent"] = labelled_df["fraudulent"].astype(int)

    # Text-based features
    labelled_df["description_length"] = (
        labelled_df["description"]
        .fillna("")
        .str.len()
    )

    labelled_df["description_word_count"] = (
        labelled_df["description"]
        .fillna("")
        .str.split()
        .str.len()
    )

    labelled_df["company_profile_length"] = (
        labelled_df["company_profile"]
        .fillna("")
        .str.len()
    )

    labelled_df["requirements_length"] = (
        labelled_df["requirements"]
        .fillna("")
        .str.len()
    )

    return clean_df, labelled_df


if __name__ == "__main__":

    df = load_data()

    clean_df, labelled_df = clean_data(df)

    print("Final cleaned dataset shape:", clean_df.shape)
    print("Labelled dataset shape:", labelled_df.shape)

    print("\nFraud label distribution:")
    print(labelled_df["fraudulent"].value_counts())

    print("\nRemaining duplicate rows:")
    print(clean_df.duplicated().sum())

    print("\nMissing values:")
    print(clean_df.isnull().sum())