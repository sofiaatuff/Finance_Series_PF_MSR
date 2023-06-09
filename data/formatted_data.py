import numpy as np
import pandas as pd
import os
import re
from pathlib import Path


cwd = Path.cwd()

data = pd.read_excel('activity.xlsx')

# lets look at all the columns and only keep the necessary ones
df = pd.DataFrame(data)
columns_to_keep = ['Date', 'Description', 'Card Member', 'Amount','Category']
df = df[columns_to_keep]


 # Change card member names to initials
df['Card Member'] = df['Card Member'].str.split().apply(lambda x: ''.join([word[0] for word in x]))
 

 # description too long, shorten it to the first three words
df['Description'] = df['Description'].str.split().apply(lambda x: ' '.join(x[:3]))

# lets remove any payments or credit which would come up as negative 
df['Amount'] = df['Amount'].apply(lambda x: x if x > 0 else 0)


#save as a new formatted csv file
df.to_csv('formatted_activity.csv', index=False)