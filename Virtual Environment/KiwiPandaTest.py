# ============================= PANDA LIBRARY PRACTISE =============================


import pandas as pd

# DF = dataframes
# DF will read the excel file using panda with given file name
df = pd.read_csv('kiwi_data.csv')

# prints the csv file using panda
print(df.to_string())


# prints row data from given index - starts at zero
print("\n",df.loc[0])

# Get column data [name of column from csv file - must be exact and is case sensitive]
species_column = df['Species']
gender_column = df['Gender']
weight_column = df['Weight(kg)']
height_column = df['Height(cm)']
location_column = df['Location']

# choosings with column to printing - using variable
print(species_column)
