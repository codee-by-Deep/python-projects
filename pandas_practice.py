### df.describe(),df.shape,df.info(),df.nunique(),df.shape,df.size,df.head(),df.tail(),df.sort_values(),df.sort_index(),df.drop_duplicates(),df.dropna(),df.fillna(),df.isnull(),df.notnull(),df.value_counts(),df.unique(),df.duplicated(),df.corr(),df.cov(),df.groupby(),df.agg(),df.apply(),df.map(),df.filter(),df.rename(),df.set_index(),df.reset_index()

import pandas as pd

df = pd.read_csv("sales.csv")
df.loc[1,['Quantity']] = 14
print(df)