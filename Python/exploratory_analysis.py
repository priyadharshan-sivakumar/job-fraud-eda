import pandas as pd
from scipy.stats import chi2_contingency

from data_loading import load_data
from data_cleaning import clean_data


def perform_eda(labelled_df):

    print("=" * 60)
    print("EXPLORATORY DATA ANALYSIS")
    print("=" * 60)

    # --------------------------------------------------
    # 1. Fraud label distribution
    # --------------------------------------------------

    print("\n1. Fraud Label Distribution")

    fraud_counts = labelled_df["fraudulent"].value_counts()
    fraud_percentages = (
        labelled_df["fraudulent"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
    )

    print("\nCounts:")
    print(fraud_counts)

    print("\nPercentages:")
    print(fraud_percentages)

    # --------------------------------------------------
    # 2. Employment type and fraud
    # --------------------------------------------------

    print("\n2. Employment Type vs Fraud")

    employment_fraud = (
        pd.crosstab(
            labelled_df["employment_type"],
            labelled_df["fraudulent"],
            normalize="index"
        )
        .mul(100)
        .round(2)
    )

    print(employment_fraud)

    # --------------------------------------------------
    # 3. Required experience and fraud
    # --------------------------------------------------

    print("\n3. Required Experience vs Fraud")

    experience_fraud = (
        pd.crosstab(
            labelled_df["required_experience"],
            labelled_df["fraudulent"],
            normalize="index"
        )
        .mul(100)
        .round(2)
    )

    print(experience_fraud)

    # --------------------------------------------------
    # 4. Required education and fraud
    # --------------------------------------------------

    print("\n4. Required Education vs Fraud")

    education_fraud = (
        pd.crosstab(
            labelled_df["required_education"],
            labelled_df["fraudulent"],
            normalize="index"
        )
        .mul(100)
        .round(2)
    )

    print(education_fraud)

    # --------------------------------------------------
    # 5. Industry and fraudulent postings
    # --------------------------------------------------

    print("\n5. Top Industries by Fraudulent Posting Count")

    fraudulent_industry = (
        labelled_df[labelled_df["fraudulent"] == 1]["industry"]
        .value_counts()
        .head(10)
    )

    print(fraudulent_industry)

    # --------------------------------------------------
    # 6. Recruitment indicators
    # --------------------------------------------------

    print("\n6. Recruitment Indicators vs Fraud")

    for col in [
        "has_company_logo",
        "has_questions",
        "telecommuting"
    ]:

        print(f"\nFraud label vs {col}")

        result = (
            pd.crosstab(
                labelled_df[col],
                labelled_df["fraudulent"],
                normalize="index"
            )
            .mul(100)
            .round(2)
        )

        print(result)

    # --------------------------------------------------
    # 7. Text feature analysis
    # --------------------------------------------------

    print("\n7. Text Feature Analysis")

    text_features = [
        "description_length",
        "description_word_count",
        "company_profile_length",
        "requirements_length"
    ]

    for feature in text_features:

        print(f"\n{feature}")

        print(
            labelled_df
            .groupby("fraudulent")[feature]
            .agg(["mean", "median", "min", "max"])
            .round(2)
        )

    # --------------------------------------------------
    # 8. Company logo fraud percentage
    # --------------------------------------------------

    print("\n8. Company Logo Fraud Percentage")

    logo_fraud = (
        labelled_df
        .groupby("has_company_logo")["fraudulent"]
        .mean()
        .mul(100)
        .round(2)
    )

    print(logo_fraud)

    # --------------------------------------------------
    # 9. Chi-Square test
    # --------------------------------------------------

    print("\n9. Chi-Square Test")

    table = pd.crosstab(
        labelled_df["has_company_logo"],
        labelled_df["fraudulent"]
    )

    chi2, p_value, dof, expected = chi2_contingency(table)

    print("Chi-square statistic:", round(chi2, 2))
    print("Degrees of freedom:", dof)
    print("P-value:", p_value)

    if p_value < 0.05:
        print(
            "Evidence of an association between "
            "company logo presence and the fraud label."
        )
    else:
        print(
            "No statistically significant association "
            "was found."
        )


if __name__ == "__main__":

    df = load_data()

    clean_df, labelled_df = clean_data(df)

    perform_eda(labelled_df)