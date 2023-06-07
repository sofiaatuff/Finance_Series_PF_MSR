import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import os
from pathlib import Path 

cwd = Path.cwd()

# we are now working with the new and imporved formatted data
data = pd.read_csv("../data/formatted_activity.csv")
df =data

# we want to know how much was spent in total
def calculate_total_amount(df, amount): 
    total_amount = df['Amount'].sum()
    return total_amount

total_amount = calculate_total_amount(df, 'Amount')

# Print the total amount
print("Total amount:", total_amount)

# lets split each card member's total
condition = df['Card Member'] == "ST"
st = df[condition]
ct = df[-condition]

#Lets create seperate DataFrames for each member to use later
dfst = pd.DataFrame(st)
sfct = pd.DataFrame(ct)

# now we want to know how much each cardmember spent
total_spent_st =st['Amount'].sum()
print("ST spent a total of: ", total_spent_st)

total_spent_ct = ct["Amount"].sum()
print("CT spent a total of: ", total_spent_ct)


# now we want to know the top spent catagory
top_spent = df.sort_values(by='Amount', ascending=False)
top_5 = top_spent.head(5)
print("The top 5 expensive purchases were: ")
top_5

#Now lets break it down by categories
grouped_df = df.groupby('Category')

for group_name, group_df in grouped_df: 
    print(f"Group: {group_name}")
    print(group_df)
    print()