import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import os
from pathlib import Path 

cwd = Path.cwd()
data = pd.read_csv("../data/formatted_activity.csv")
df = data

keep_columns = ['Card Member', 'Amount', 'Category']
df2 = df[keep_columns]

# Bar plot 
plt.figure(figsize=(10, 6))
df.groupby('Card Member')['Amount'].sum().plot(kind='bar')
plt.xlabel('Card Member')
plt.ylabel('Total Amount')
plt.title('Total Amount Spent per Card Member')
plt.savefig('../plots/bar_amt_cm.png')

# Pie chart of amount spent by each member
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
df = df[df['Amount'] >= 0]  # Filter out negative values

plt.figure(figsize=(8, 8))
amount_by_member = df.groupby('Card Member')['Amount'].sum()
plt.pie(amount_by_member, labels=amount_by_member.index, autopct='%1.1f%%')
plt.title('Amount Distribution by Card Member')
plt.savefig('../plots/pie_amt_cm.png')


#Pie chart for amount dist. by category
plt.figure(figsize=(12, 12))
df.groupby('Category')['Amount'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.ylabel('')
plt.title('Amount Distribution by Category')
plt.savefig('../plots/pie_amt_cat.png')

# Line Plot for total amount my category
plt.figure(figsize=(10, 6))
df.groupby('Category')['Amount'].sum().plot(kind='line', marker='o')
plt.xlabel('Category')
plt.ylabel('Total Amount')
plt.title('Total Amount by Category')
plt.xticks(rotation=45)
plt.savefig('../plots/line_amt_cat.png')


# Scatter Plot 
# Assign numeric values to categories
category_values = np.arange(len(df['Category'].unique()))
category_mapping = {category: value for value, category in enumerate(df['Category'].unique())}
df['Category_Num'] = df['Category'].map(category_mapping)

# Assign colors based on 'Card Member' column
colors = np.where(df['Card Member'] == 'Member A', 'red', 'blue')

plt.figure(figsize=(12, 12))
plt.scatter(df['Category_Num'], df['Amount'], c=colors)
plt.xlabel('Category')
plt.ylabel('Amount')
plt.title('Amount vs. Category')
plt.xticks(ticks=category_values, labels=category_mapping.keys(), rotation=45)
plt.savefig('../plots/scatter_amt_cat.png')