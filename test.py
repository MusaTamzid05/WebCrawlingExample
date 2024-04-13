import pandas as pd

# List of dictionaries with the same keys
data_A = [{'name': 'John', 'age': 30, 'city': 'New York'},
          {'name': 'Jane', 'age': 25, 'city': 'Los Angeles'}]

data_B = [{'name': 'Mike', 'age': 35, 'city': 'Chicago'},
          {'name': 'Lucy', 'age': 28, 'city': 'Miami'}]

# Create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

# Write data to sheet 'A'
df_A = pd.DataFrame(data_A)
df_A.to_excel(writer, sheet_name='A', index=False)

# Write data to sheet 'B'
df_B = pd.DataFrame(data_B)
df_B.to_excel(writer, sheet_name='B', index=False)

# Save the Excel file
writer.close()
