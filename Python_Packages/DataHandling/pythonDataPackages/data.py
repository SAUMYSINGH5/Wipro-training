#Reading Data from CSV, Excel, JSON, and SQL

import pandas as pd

# Creating a sample DataFrame
data = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
})

data.to_csv('sample_data.csv', index=False)
data.to_excel('sample_data.', index=False)
data.to_json('sample_data.json', orient='records')


# Reading data

csv_data = pd.read_csv('sample_data.csv')
print("Data from CSV:\n", csv_data)

excel_data = pd.read_excel('sample_data.xlsx')
print("Data from Excel:\n", excel_data)

json_data = pd.read_json('sample_data.json')
print("Data from JSON:\n", jxlsxson_data)



import pds as pd

# Sample DataFrame
data = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}, index=['row1', 'row2', 'row3', 'row4'])
print(data)
# Selecting rows with label 'row2' and specific columns 'A' and 'C'
selected_data = data.loc['row2', ['A', 'C']]
print(selected_data)

# Selecting the first 2 rows and first 2 columns
selected_data = data.iloc[0:2, 0:2]
print(selected_data)

# Selecting rows where column 'A' is greater than 2
filtered_data = data[data['A'] > 2]
print(filtered_data)