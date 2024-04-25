import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel('upa.xlsx')

# Remove duplicate rows based on all columns
df.drop_duplicates(inplace=True)

# Save the DataFrame back to an Excel file
df.to_excel('upa.xlsx', index=False)
