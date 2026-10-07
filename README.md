# Exploratory Data Analysis of Online Job Postings to Understand Patterns Associated with Recruitment Fraud

## Project Information

### Project Title
**Exploratory Data Analysis of Online Job Postings to Understand Patterns Associated with Recruitment Fraud**

### Industry Name
**Recruitment / Employment**

### Problem Statement
Online job platforms contain genuine employment opportunities as well as fraudulent postings. This project uses exploratory data analysis, descriptive statistics, data visualisation, and statistical analysis to examine job-posting characteristics and identify patterns associated with the recorded fraudulent label.

### Proposed Solution / Analysis Questions
The project combines two job-posting dataset files and performs data quality assessment, data cleaning, data preparation, exploratory data analysis, visualization, and statistical analysis.

The analysis focuses on:

- Genuine vs. fraudulent job postings
- Employment type and fraudulent postings
- Industry and fraudulent postings
- Company logo presence and fraud labels
- Screening questions and fraud labels
- Telecommuting availability and fraud labels
- Job description length and fraud labels
- Company profile length and requirements length
- Association between company-logo presence and the fraudulent label using a Chi-Square test

### Dataset Name

- `fake_job_postings.csv`
- `Job_Fraudlent_Cleaned_Dataset.csv`

> `Job_Fraudlent_Cleaned_Dataset.csv` is the filename used in the project code. The project combines both files using `pd.concat()`.

### Dataset Source
The project code loads the datasets from local CSV files. No external dataset source URL is specified in the project notebook.

### Dataset Size
After combining the two CSV files, the dataframe contains:

- **35,479 records**
- **18 columns**

The 18 columns are:

| No. | Column | Description |
|---:|---|---|
| 1 | `job_id` | Unique identifier assigned to each job posting |
| 2 | `title` | Title or position name of the job |
| 3 | `location` | Geographic location of the job |
| 4 | `department` | Department associated with the job |
| 5 | `salary_range` | Salary or compensation range provided in the posting |
| 6 | `company_profile` | Information describing the recruiting company |
| 7 | `description` | Detailed job description |
| 8 | `requirements` | Skills, qualifications, and requirements |
| 9 | `benefits` | Benefits or additional information offered |
| 10 | `telecommuting` | Indicates whether telecommuting is available |
| 11 | `has_company_logo` | Indicates whether the posting contains a company logo |
| 12 | `has_questions` | Indicates whether screening questions are included |
| 13 | `employment_type` | Type of employment |
| 14 | `required_experience` | Required level of professional experience |
| 15 | `required_education` | Educational qualification required |
| 16 | `industry` | Industry associated with the job |
| 17 | `function` | Functional area or job category |
| 18 | `fraudulent` | Target variable indicating the recorded fraud label |

### Target Variable

The primary target variable is **`fraudulent`**:

- `0` — Genuine
- `1` — Fraudulent
- `NaN` — Missing/unknown fraud label

The initial dataset inspection showed:

- **28,425** genuine records
- **1,455** fraudulent records
- **5,599** records with missing fraud labels
- **269** exact duplicate rows

After the cleaning and preparation steps used in the notebook, the analysis dataframe contained **29,577 rows and 18 columns**.

---

## Tools & Technologies

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Seaborn
- SciPy

---

## Project Workflow

**Industry Selection → Problem Identification → Dataset Collection → Data Cleaning → Data Transformation → Data Analysis → Data Visualization → Insights → Recommendations**

### Workflow Used in the Notebook

**Raw Dataset → Data Loading → Initial Inspection → Data Quality Assessment → Data Cleaning → Data Preparation → Exploratory Data Analysis → Data Visualization → Key Findings → Conclusion**

---

## Data Cleaning & Preparation

The notebook performs the following data preparation steps:

- Copies the loaded dataframe for cleaning
- Removes exact duplicate rows
- Strips extra spaces from text columns
- Converts blank text values to missing values
- Converts the `fraudulent` column to numeric values
- Keeps missing fraud labels as unknown instead of treating them as genuine
- Creates a labelled dataset by excluding rows with missing `fraudulent` values
- Creates text-based features from:
  - `description`
  - `company_profile`
  - `requirements`

The text features include:

- `description_length`
- `description_word_count`
- `company_profile_length`
- `requirements_length`

---

## Data Analysis & Visualization

### 1. Dataset Structure and Data Quality Analysis

The project examines:

- Dataset shape
- Column names
- Data types
- Descriptive statistics
- Missing values
- Missing-value percentages
- Exact duplicate rows
- Duplicate job IDs
- Fraud-label distribution
- Unique values for important categorical columns

### 2. Fraud Label Distribution

The cleaned analysis dataframe contains:

| Fraud Label | Count | Percentage |
|---|---:|---:|
| Genuine | 22,805 | 95.11% |
| Fraudulent | 1,173 | 4.89% |

### 3. Categorical Analysis

The notebook analyzes:

- `employment_type`
- `required_experience`
- `required_education`
- `industry`
- `function`

### 4. Recruitment Indicator Analysis

The project uses cross-tabulation to examine fraud labels against:

- `has_company_logo`
- `has_questions`
- `telecommuting`

### 5. Text Feature Analysis

The project calculates and compares:

- Description character length
- Description word count
- Company profile length
- Requirements length

The notebook compares these features between genuine and fraudulent postings.

### 6. Statistical Analysis

A **Chi-Square Test of Association** is performed between:

- `has_company_logo`
- `fraudulent`

The notebook output reports:

- **Chi-square statistic:** 1592.44
- **Degrees of freedom:** 1
- **P-value:** 0.0

The notebook therefore reports **evidence of an association between company-logo presence and the fraudulent label** at the 0.05 significance level.

---

## Visualization Screenshots

The notebook contains the following visualizations:

### 1. Missing Values Before Data Cleaning

<img width="1184" height="674" alt="01_Missing_Values_Before_Data_Cleaning" src="https://github.com/user-attachments/assets/c569259b-e78c-4c5f-89ee-e7c7888b1276" />

### 2. Distribution of Genuine and Fraudulent Job Postings

<img width="684" height="574" alt="02_Genuine_vs_Fraudulent_Job_Postings" src="https://github.com/user-attachments/assets/6210999c-bb41-4c25-9d26-fbfadfd649a4" />

### 3. Fraud Percentage by Employment Type

<img width="984" height="674" alt="03_Fraud_Percentage_by_Employment_Type" src="https://github.com/user-attachments/assets/1b7917bf-bcb2-4c54-9acc-371cb908c614" />

### 4. Company Logo Presence and Fraud Label

<img width="684" height="574" alt="04_Company_Logo_Presence_and_Fraud_Label" src="https://github.com/user-attachments/assets/19718ac4-cdb3-4def-8c2e-0e652e578c54" />

### 5. Job Description Length by Fraud Label

<img width="884" height="574" alt="05_Job_Description_Length_by_Fraud_Label" src="https://github.com/user-attachments/assets/706a2a0d-be02-4a05-b597-c002996d7aa4" />

### 6. Fraudulent Proportion Across the 10 Most Common Industries

<img width="1184" height="674" alt="06_Fraudulent_Proportion_Across_Major_Industries" src="https://github.com/user-attachments/assets/f0bf281c-c1ff-4470-804c-8dec7438c5e7" />

### 7. Screening Questions and Fraud Label

<img width="2970" height="1774" alt="07_Screening_Questions_and_Fraud_Label" src="https://github.com/user-attachments/assets/9aefef34-8db6-43ce-b027-f881bcf79b9b" />

### 8. Telecommuting Availability and Fraud Label

<img width="2970" height="1774" alt="08_Telecommuting_Availability_and_Fraud_Label" src="https://github.com/user-attachments/assets/e98480f4-3cf3-4dc5-9d02-129325de9ce9" />

> Rename the image references above to the actual screenshot filenames when the visualization images are uploaded to GitHub.

---

## Key Insights

1. **Dataset composition:** The combined dataset initially contained **35,479 records and 18 columns**. The initial inspection identified **269 exact duplicate rows** and **5,599 missing values in the `fraudulent` column**.

2. **Fraud-label distribution:** After the cleaning and preparation steps used in the notebook, the analysis dataframe contained **29,577 records**. Of these, **22,805 (95.11%)** were labelled genuine and **1,173 (4.89%)** were labelled fraudulent.

3. **Industry pattern:** Among the fraudulent postings, the largest number belonged to the **`unknown` industry (373)**, followed by **Oil & Energy (141)**, **Hospital & Health Care (74)**, **Marketing and Advertising (70)**, and **Accounting (67)**.

4. **Company logo:** The fraud percentage calculated by company-logo presence was **15.98% for postings without a company logo** and **2.10% for postings with a company logo**.

5. **Job description length:** Genuine postings had a median description length of **147 words**, while fraudulent postings had a median of **114 words**. The mean word counts were **170.73** for genuine postings and **157.35** for fraudulent postings.

6. **Text characteristics:** The notebook also compares company-profile and requirements lengths between genuine and fraudulent postings. The median company-profile length was **595 characters for genuine postings** and **7 characters for fraudulent postings**. The median requirements length was **483 characters for genuine postings** and **249 characters for fraudulent postings**.

7. **Statistical analysis:** The Chi-Square test between company-logo presence and the fraudulent label produced a **chi-square statistic of 1592.44**, with **1 degree of freedom** and a **p-value of 0.0**. The notebook reports evidence of an association between the two variables.

---

## Recommendations

Based on the actual findings in the notebook:

- Job-posting analysis can include **company-logo presence as one recruitment-related indicator** when examining patterns associated with the recorded fraud label.
- Job descriptions, company profiles, and requirements can be examined as **text-based characteristics** when studying differences between genuine and fraudulent postings.
- Industry-level fraud proportions should be interpreted together with the **number of postings in each industry**, particularly where the industry is recorded as `unknown`.
- Missing fraud labels should remain separate from genuine labels because missing values do not provide evidence that a posting is genuine.

> These recommendations describe the observed patterns in this EDA project and do not imply that any individual characteristic proves that a job posting is fraudulent.

---

## Project Folder Structure

```text
Fraudlent-Job-Posting-Data-Analysis/
│
├── README.md
│
├── Dataset/
│   ├── fake_job_postings.csv
│   └── Job_Fraudlent_Cleaned_Dataset.csv
│
├── Notebook/
│   └── Fraudlent Job Posting Data Analysis project.ipynb
│
└── Visualizations/
    ├── missing_values_before_cleaning.png
    ├── genuine_vs_fraudulent_postings.png
    ├── fraud_percentage_by_employment_type.png
    ├── company_logo_vs_fraud_label.png
    ├── job_description_length_by_fraud_label.png
    ├── fraud_proportion_across_industries.png
    ├── screening_questions_vs_fraud_label.png
    └── telecommuting_vs_fraud_label.png
```

> The visualization filenames shown above are descriptive placeholders because the notebook itself does not provide uploaded image filenames. Replace them with the actual filenames when the screenshots are added to GitHub.

---

## Conclusion

This project performs Exploratory Data Analysis on online job-posting data to examine characteristics associated with recorded recruitment-fraud labels.

The analysis includes data-quality assessment, duplicate and missing-value handling, fraud-label preparation, categorical analysis, recruitment-indicator analysis, text-feature analysis, visualization, and Chi-Square statistical testing.

The results identify differences between genuine and fraudulent postings in areas such as company-logo presence and text characteristics. The analysis describes associations within the available data and does not establish that any single characteristic causes a job posting to be fraudulent.

---

## Author

- **Name:** Priyadharshan Sivakumar
- **Student ID:** AF05311608
- **Organization:** Anudip Foundation
- **Course:** AIML
- **Batch Code:** ANP-D7444
