import pandas as pd

# read csv and show some records
df = pd.read_csv('IT Salary Survey EU  2020.csv' , sep=",")
df.head()

# check column values
df.columns.values

# show number of rows and columns
df.shape

# check column data types and whether they're nullable or not
df.info()

# summary statistics i.e count, mean, standard deviation, minimum and maximum values and the quantiles of the data.
df.describe()
