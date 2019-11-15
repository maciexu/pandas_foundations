# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:37:47 2019

@author: mengx
"""

import pandas as pd

cerealdf=pd.read_csv(r'C:\Users\mengx\Documents\python_learn\cereal\925f08febd10b40b8b5e-61013864f780e43a99349cc1e31fc89b39d862c0\cereal.csv')
print(cerealdf.head(5))

cerealdf.info()
cerealdf.iloc[10:20, 0:5]

print(cerealdf['Calories'].dtypes)
print(cerealdf['Fiber'].dtypes)
print(cerealdf['Fat'].dtypes)

print(cerealdf['Fat'][0] + cerealdf['Fat'][1])



#list_label=[]
#df.columns=list_label
cerealdf.columns.values[2]='typeee'


cities=['Manheim', 'Preston park', 'Biglerville', 'Indiana', 'Curwensville', 
        'Crown', 'Harveys lake', 'Mineral springs', 'Cassville', 'Hannastown', 
        'Saltsburg', 'Tunkhannock', 'Pittsburgh', 'Lemasters', 'Great bend']
state = 'PA'
# Construct a dictionary: data
data = {'state':state, 'city':cities}

# Construct a DataFrame from dictionary data: df
pennsylvania = pd.DataFrame(data)

# Print the DataFrame
print(pennsylvania)

first2cols=['Cereal Name', 'Manufacturer']
first2col=cerealdf[first2cols]
out=first2col.iloc[10:20, :]
print(out)

out_csv='out.csv'
out.to_csv(out_csv)



# Read the raw file as-is: df1
df1 = pd.read_csv(r'C:\Users\mengx\Documents\python_learn\messy_stock_data.tsv.txt')

# Print the output of df1.head()
print(df1.head(5))

# Read in the file with the correct parameters: df2
df2 = pd.read_csv(r'C:\Users\mengx\Documents\python_learn\messy_stock_data.tsv.txt', delimiter=' ', header=3, comment='#')

# Print the output of df2.head()
print(df2.head(5))

# Save the cleaned up DataFrame to a CSV file without the index
df2.to_csv('file_clean', index=False)

# Save the cleaned up DataFrame to an excel file without the index C:\Users\mengx
df2.to_excel('file_clean.xlsx', index=False)



# Create a list of the new column labels: new_labels
new_labels =['NAME', 'jan', 'feb', 'mar', 'apr', 'may', 'jn', 'jl', 'agu', 'sep', 'oct', 'nov', 'dec']

# Read in the file, specifying the header and names parameters: df2
df3 = pd.read_csv(r'file_clean', header=0, index_col=0, names=new_labels)








