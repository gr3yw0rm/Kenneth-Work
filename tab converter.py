import pandas as pd

filename = 'D500_IT0008vtest.txt'

# reads as tab delimited file
data = pd.read_csv(filename, skiprows=0, sep='\\t', index_col=False, engine='python')

# removes quotes from data
data = data.replace('"', '', regex=True).replace('    "', '', regex=True)

# exports data to excel
new_filename = filename.replace('.txt', '.xlsx')
data.to_excel(new_filename, index=False)


'''
Copyright by Calvin M. Del Rosario
'''