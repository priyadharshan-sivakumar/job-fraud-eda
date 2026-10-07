import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from data_loading import load_data
from data_cleaning import clean_data


def create_visualizations(df, labelled_df):

    # Create visualization folder
    output_folder = "Visualizations"

    # --------------------------------------------------
    # 1. Missing values before cleaning
    # --------------------------------------------------

    missing_pct = (
        df.isnull()
        .mean()
        .mul(100)
        .sort_values(ascending=False)
    )

    missing_pct = missing_pct[missing_pct > 0]

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=missing_pct.values,
        y=missing_pct.index
    )

    plt.title("Missing Values Before Data Cleaning")
    plt.xlabel("Missing Values (%)")
    plt.ylabel("Columns")
    plt.tight_layout()

    plt.savefig(
        f"{output_folder}/missing_values_before_cleaning.png",
        dpi=300
    )

    plt.show()

    # --------------------------------------------------
    # 2. Genuine vs Fraudulent postings
    # --------------------------------------------------

    plt.figure(figsize=(7, 5))

    sns.countplot(
        data=labelled_df,
        x="fraudulent"
    )

    plt.title("Distribution of Genuine and Fraudulent Job Postings")
    plt.xlabel("Fraud Label")
    plt.ylabel("Number of Job Postings")

    plt.xticks(
        [0, 1],
        ["Genuine", "Fraudulent"]
    )

    plt.tight_layout()

    plt.savefig(
        f"{output_folder}/genuine_vs_fraudulent_postings.png",
        dpi=300
    )

    plt.show()

    # --------------------------------------------------
    # 3. Fraud percentage by employment type
    # --------------------------------------------------

    employment_fraud = (
        pd.crosstab(
            labelled_df["employment_type"],
            labelled_df["fraudulent"],
            normalize="index"
        )
        .mul(100)
        .round(2)
    )

    if 1 in employment_fraud.columns:

        fraud_percentage = employment_fraud[1].sort_values(
            ascending=False
        )

        plt.figure(figsize=(10, 6))

        sns.barplot(
            x=fraud_percentage.values,
            y=fraud_percentage.index
        )

        plt.title("Fraud Percentage by Employment Type")
        plt.xlabel("Fraudulent Postings (%)")
        plt.ylabel("Employment Type")

        plt.tight_layout()

        plt.savefig(
            f"{output_folder}/fraud_percentage_by_employment_type.png",
            dpi=300
        )

        plt.show()

    # --------------------------------------------------
    # 4. Company logo vs fraud label
    # --------------------------------------------------

    plt.figure(figsize=(7, 5))

    sns.countplot(
        data=labelled_df,
        x="has_company_logo",
        hue="fraudulent"
    )

    plt.title("Company Logo Presence and Fraud Label")
    plt.xlabel("Has Company Logo")
    plt.ylabel("Number of Job Postings")

    plt.tight_layout()

    plt.savefig(
        f"{output_folder}/company_logo_vs_fraud_label.png",
        dpi=300
    )

    plt.show()

    # --------------------------------------------------
    # 5. Job description length
    # --------------------------------------------------

    plt.figure(figsize=(8, 6))

    sns.boxplot(
        data=labelled_df,
        x="fraudulent",
        y="description_word_count"
    )

    plt.title("Job Description Length by Fraud Label")
    plt.xlabel("Fraud Label")
    plt.ylabel("Description Word Count")

    plt.xticks(
        [0, 1],
        ["Genuine", "Fraudulent"]
    )

    plt.tight_layout()

    plt.savefig(
        f"{output_folder}/job_description_length_by_fraud_label.png",
        dpi=300
    )

    plt.show()

    # --------------------------------------------------
    # 6. Fraud proportion across industries
    # --------------------------------------------------

    top_industries = (
        labelled_df["industry"]
        .value_counts()
        .head(10)
        .index
    )

    industry_fraud = (
        labelled_df[
            labelled_df["industry"].isin(top_industries)
        ]
        .groupby("industry")["fraudulent"]
        .mean()
        .mul(100)
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 7))

    sns.barplot(
        x=industry_fraud.values,
        y=industry_fraud.index
    )

    plt.title(
        "Fraudulent Proportion Across Major Industries"
    )

    plt.xlabel("Fraudulent Postings (%)")
    plt.ylabel("Industry")

    plt.tight_layout()

    plt.savefig(
        f"{output_folder}/fraud_proportion_across_industries.png",
        dpi=300
    )

    plt.show()


if __name__ == "__main__":

    df = load_data()

    clean_df, labelled_df = clean_data(df)

    create_visualizations(df, labelled_df)