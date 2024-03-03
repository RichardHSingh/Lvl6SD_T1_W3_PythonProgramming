#======================= PANDA LIBRARY TEST ============================================

import pandas as pd

# DF = dataframes
# DF will read the excel file using panda with given file name
df = pd.read_csv('temperatures_auckland_data.csv')

# prints the csv file using panda
print(df.to_string())


# prints row data from given index - starts at zero
print("\n",df.loc[0])

# Get column data [name of column from csv file  - must be exact and is case sensitive]
ts_column = df['TS']
max_column = df['Tmax']
mix_column = df['Tmin']

print(ts_column)
