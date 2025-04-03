import pandas as pd

# Load the CSV files
description_df = pd.read_csv('symptom_description.csv')
precaution_df = pd.read_csv('symptom_precaution.csv')
severity_df = pd.read_csv('symptom_severity.csv')

# Display the data
print(description_df.head())
print(precaution_df.head())
print(severity_df.head())
