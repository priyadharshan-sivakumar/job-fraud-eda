import pandas as pd
from pathlib import Path


def load_data():
    """
    Load and combine the two job-posting CSV files.
    """

    project_root = Path(__file__).resolve().parent.parent
    dataset_path = project_root / "Dataset"

    raw_file = dataset_path / "Job_Fraudlent_Raw_Dataset_final.csv"
    second_file = dataset_path / "Job_Fraudlent_Cleaned_Dataset_final.csv"

    df1 = pd.read_csv(raw_file)
    df2 = pd.read_csv(second_file)

    df = pd.concat([df1, df2], ignore_index=True)

    print("Dataset 1 shape:", df1.shape)
    print("Dataset 2 shape:", df2.shape)
    print("Combined dataset shape:", df.shape)

    return df


if __name__ == "__main__":
    df = load_data()

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nDataset information:")
    print(df.info())